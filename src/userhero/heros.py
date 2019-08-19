import json
import random


def load():
    with open('data.js') as fh:
        data = json.load(fh)

    return random.shuffle(data)

