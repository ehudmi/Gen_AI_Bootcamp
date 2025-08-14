# Use the Chuck Norris API https://api.chucknorris.io/ to retrieve some jokes in a specific category
# Use every notion described in the lesson

import requests
from random import randint
import json

CATEGORIES = requests.get("https://api.chucknorris.io/jokes/categories").json()


def get_jokes():
    category = CATEGORIES[randint(0, len(CATEGORIES))]
    print(category)
    response = requests.get(
        f"https://api.chucknorris.io/jokes/random?category={category}"
    )
    data = response.json()
    print(data["value"])
    print(response.request.url)
    print(response.request.body)


get_jokes()
