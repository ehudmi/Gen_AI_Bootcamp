import os
import json
import random
from typing import Dict, Any
from dotenv import load_dotenv
from smolagents import CodeAgent, HfApiModel, tool

load_dotenv()

# Using HfApiModel for better stability with the free-tier serverless API
model = HfApiModel(
    model_id="meta-llama/Llama-3.2-3B-Instruct",
    token=os.getenv("HF_TOKEN")
)

# Global state for simplicity
DISTRIBUTION_HISTORY = {}

@tool
def check_history(penguin_name: str) -> Dict[str, Any]:
    """
    Check the recent resource distribution history for a specific penguin.

    Args:
        penguin_name: The name of the penguin to check history for.
    """
    history = DISTRIBUTION_HISTORY.get(penguin_name, [])
    recent_food = sum(h["food"] for h in history[-3:]) if history else 0
    has_tool = any(h["has_tool"] for h in history) if history else False
    return {"recent_food": recent_food, "has_tool": has_tool}

@tool
def record_distribution(penguin_name: str, food: int, has_tool: bool) -> str:
    """
    Record the distribution of resources.

    Args:
        penguin_name: The name of the penguin receiving resources.
        food: The amount of food given.
        has_tool: Whether a tool was provided.
    """
    if penguin_name not in DISTRIBUTION_HISTORY:
        DISTRIBUTION_HISTORY[penguin_name] = []
    DISTRIBUTION_HISTORY[penguin_name].append({"food": food, "has_tool": has_tool})
    return f"Recorded: {penguin_name} got {food} food and {'a' if has_tool else 'no'} tool"

@tool
def find_food(penguin_name: str, method: str) -> int:
    """
    Return a small random food yield. 

    Args:
        penguin_name: The name of the penguin searching for food.
        method: The method used ('fishing' or 'foraging').
    """
    if method == "fishing":
        yield_amount = random.randint(2, 7)
    else:
        yield_amount = random.randint(0, 3)
    return yield_amount

class ScientistAgent:
    def __init__(self, initial_food_supply: int = 20, refresh_interval: int = 5) -> None:
        # CodeAgent is more robust for small models than ToolCallingAgent
        self.agent = CodeAgent(
            tools=[check_history, record_distribution],
            model=model,
            add_base_tools=False
        )
        self.initial_food_supply = initial_food_supply
        self.food_supply = initial_food_supply
        self.tool_available = True
        self.refresh_interval = refresh_interval
        self.turn_counter = 0

    def refresh_resources(self):
        self.food_supply = self.initial_food_supply
        self.tool_available = True
        print("\n🔄 Scientist Resources Refreshed!")

    def respond_to_action(self, penguin: 'PenguinAgent', penguin_action: Dict[str, Any]) -> None:
        self.turn_counter += 1
        if self.turn_counter % self.refresh_interval == 0:
            self.refresh_resources()

        history = check_history(penguin.name)
        
        # We ask the agent to decide, then use final_answer to return the result
        prompt = f"""
                Penguin {penguin.name} took action: {penguin_action}
                History: {history['recent_food']} recent food.
                Scientist Resources: {self.food_supply} food, Tool available: {self.tool_available}

                You can use 'check_history' if needed, but your GOAL is to decide what to give.
                Return your decision by calling final_answer() with a dict:
                final_answer({{"give_food": 2, "give_tool": False}})
                """
        
        response = self.agent.run(prompt)

        try:
            # CodeAgent's run returns the final_answer directly
            decision = response if isinstance(response, dict) else json.loads(str(response))
            food = min(int(decision.get('give_food', 0)), self.food_supply)
            tool_to_give = bool(decision.get('give_tool', False)) and self.tool_available

            if food > 0:
                self.food_supply -= food
                penguin.food += food
            if tool_to_give:
                penguin.has_tool = True
                self.tool_available = False

            record_distribution(penguin.name, food, tool_to_give)
            print(f"Scientist gave {penguin.name}: {food} food, Tool: {tool_to_give}")
        except Exception as e:
            print(f"Error processing scientist's response: {e}")
class PenguinAgent:
    def __init__(self, name: str) -> None:
        # We remove tools from here so the penguin doesn't execute them itself
        # It should only DESCRIBE what it wants to do
        self.agent = CodeAgent(tools=[], model=model, add_base_tools=False)
        self.name = name
        self.food = 0
        self.has_tool = False

    def take_action(self) -> Dict[str, Any]:
        """Penguin decides on an action each round."""
        prompt = f"""
                You are Penguin {self.name} with {self.food} food.
                IMPORTANT: You have NO python tools available (do not try to call search(), inventory(), etc.).
                Just decide on your next action.
                You must return your answer by calling final_answer() with a dict:
                final_answer({{"action": "find_food", "method": "fishing"}})
                """
        
        response = self.agent.run(prompt)

        # Safety check: handle if the agent still returns a string or weird object
        if isinstance(response, dict):
            return response
        
        # If it returns a string that looks like a dict, try to parse it
        try:
            if isinstance(response, str):
                # Replace single quotes with double quotes for valid JSON
                return json.loads(response.replace("'", '"'))
        except Exception:
            pass
            
        return {"action": "find_food", "method": "foraging"} # Default safe fallback
def run_simulation():
    scientist = ScientistAgent()
    penguins = [PenguinAgent(f"Penguin{i}") for i in range(2)] # Reduced to 2 for faster testing

    print("\nStarting Simulation...")
    for round_idx in range(3):
        print(f"\nROUND {round_idx + 1}")
        for penguin in penguins:
            action = penguin.take_action()
            print(f"{penguin.name} chose: {action}")

            if action.get("action") == "find_food":
                food_found = find_food(penguin.name, action.get("method", "foraging"))
                penguin.food += food_found
                print(f"{penguin.name} found {food_found} food.")

            scientist.respond_to_action(penguin, action)

if __name__ == "__main__":
    run_simulation()
    run_simulation()