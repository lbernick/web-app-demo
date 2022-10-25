NOISES = {
    "bird": "tweet",
    "cat": "meow",
    "cow": "moo",
    "dog": "woof",
    "dolphin": "so long, and thanks for all the fish",
    "duck": "quack",
    "fish": "blub",
    "frog": "ribbit",
    "mouse": "squeak",
    "sheep": "baa",
    "snake": "hiss",
}

DEFAULT_NOISE = "Unknown animal"


def speak(animal_name: str) -> str:
    return NOISES.get(animal_name, DEFAULT_NOISE) + "\n"
