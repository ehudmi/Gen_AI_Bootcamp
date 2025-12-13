from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Tuple
import math
import random


WIN_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),  # rows
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),  # cols
    (0, 4, 8),
    (2, 4, 6),  # diagonals
]


def print_board(board: List[str]) -> None:
    """
    Board indices:
      1 | 2 | 3
     ---+---+---
      4 | 5 | 6
     ---+---+---
      7 | 8 | 9
    """

    def cell(i: int) -> str:
        return board[i] if board[i] != " " else str(i + 1)

    rows = [
        f" {cell(0)} | {cell(1)} | {cell(2)} ",
        f" {cell(3)} | {cell(4)} | {cell(5)} ",
        f" {cell(6)} | {cell(7)} | {cell(8)} ",
    ]
    sep = "---+---+---"
    print(rows[0])
    print(sep)
    print(rows[1])
    print(sep)
    print(rows[2])


def winner(board: List[str]) -> Optional[str]:
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board: List[str]) -> bool:
    return winner(board) is None and all(x != " " for x in board)


def available_moves(board: List[str]) -> List[int]:
    return [i for i, v in enumerate(board) if v == " "]


@dataclass(frozen=True)
class AIConfig:
    # mode = "perfect" (minimax) or "easy" (makes mistakes)
    mode: str = "perfect"
    # In easy mode, probability that AI chooses a non-optimal move.
    blunder_rate: float = 0.30
    rng_seed: Optional[int] = None


class TicTacToeAI:
    def __init__(self, ai_mark: str, human_mark: str, config: AIConfig):
        self.ai = ai_mark
        self.human = human_mark
        self.config = config
        self.rng = random.Random(config.rng_seed)

    def choose_move(self, board: List[str]) -> int:
        moves = available_moves(board)

        if self.config.mode == "easy":
            # Sometimes intentionally blunder
            if self.rng.random() < self.config.blunder_rate:
                return self.rng.choice(moves)

            # Otherwise: play "smart enough" (but still not full minimax):
            # 1) win if possible
            m = self._winning_move(board, self.ai)
            if m is not None:
                return m
            # 2) block if needed
            m = self._winning_move(board, self.human)
            if m is not None:
                return m
            # 3) take center, then corners, then edges
            if board[4] == " ":
                return 4
            for i in [0, 2, 6, 8]:
                if board[i] == " ":
                    return i
            return self.rng.choice(moves)

        # Perfect mode: minimax (unbeatable)
        best_score = -math.inf
        best_move = moves[0]
        for m in moves:
            board[m] = self.ai
            score = self._minimax(board, is_ai_turn=False)
            board[m] = " "
            if score > best_score:
                best_score = score
                best_move = m
        return best_move

    def _winning_move(self, board: List[str], mark: str) -> Optional[int]:
        for m in available_moves(board):
            board[m] = mark
            if winner(board) == mark:
                board[m] = " "
                return m
            board[m] = " "
        return None

    def _minimax(self, board: List[str], is_ai_turn: bool) -> int:
        """
        Returns a score from AI's perspective:
          +1 : AI win
           0 : draw
          -1 : AI loss
        """
        w = winner(board)
        if w == self.ai:
            return 1
        if w == self.human:
            return -1
        if is_draw(board):
            return 0

        moves = available_moves(board)

        if is_ai_turn:
            best = -math.inf
            for m in moves:
                board[m] = self.ai
                best = max(best, self._minimax(board, is_ai_turn=False))
                board[m] = " "
            return int(best)
        else:
            best = math.inf
            for m in moves:
                board[m] = self.human
                best = min(best, self._minimax(board, is_ai_turn=True))
                board[m] = " "
            return int(best)


def read_human_move(board: List[str]) -> int:
    while True:
        raw = input("Your move (1-9): ").strip()
        if not raw.isdigit():
            print("Please enter a number from 1 to 9.")
            continue
        pos = int(raw) - 1
        if pos < 0 or pos > 8:
            print("Please enter a number from 1 to 9.")
            continue
        if board[pos] != " ":
            print("That square is taken. Choose another.")
            continue
        return pos


def main() -> None:
    print("Tic Tac Toe")
    print("You are X, AI is O.")
    print("Enter moves using 1-9 positions as shown on the board.")
    print()

    # Change mode to "easy" if you want a winnable AI.
    config = AIConfig(mode="perfect", blunder_rate=0.35, rng_seed=None)
    board = [" "] * 9

    human = "X"
    ai = "O"
    bot = TicTacToeAI(ai_mark=ai, human_mark=human, config=config)

    human_turn = True  # human goes first

    while True:
        print_board(board)
        print()

        if human_turn:
            move = read_human_move(board)
            board[move] = human
        else:
            move = bot.choose_move(board)
            board[move] = ai
            print(f"AI plays: {move + 1}")

        w = winner(board)
        if w is not None:
            print()
            print_board(board)
            print()
            print(f"{'You' if w == human else 'AI'} win!")
            return

        if is_draw(board):
            print()
            print_board(board)
            print()
            print("Draw.")
            return

        human_turn = not human_turn
        print()


if __name__ == "__main__":
    main()
