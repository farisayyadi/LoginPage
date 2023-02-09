import random
import json


with open("german_2000.json") as file:
    items = json.load(file)


def get_random_sentence():
    return random.choice(items)
