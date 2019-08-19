import json
import random


def get_adorable_avatar(email, size_pixels, border_radius=50):
    size_pixels = int(min(max(size_pixels, 40), 285))
    border_radius = int(min(max(border_radius, 0), 50)) # ???
    return f"https://avatars.adorable.io/{size_pixels}/{email}.png"

border_radius

def load():
    with open('data.js') as fh:
        data = json.load(fh)
    return random.shuffle(data)

