import random

def on_shuffle_choices(choices: list) -> list:
    random.shuffle(choices)
    return choices

question_bank = {
    "Module 1": {
        "some tag": {
            "Q1": {
                "question": "|",
                "answer": "a",
                "function": lambda: on_shuffle_choices([
                    "a", "b", "c", "d",]),
                "format": "multiple",
            },
        },
        "another some tag": {
            "Q2": {
                "question": "|",
                "answer": "a",
                "function": None,
                "format": "true/false",
            },
        },
    },
    "Module 2": {
        "another tag": {
            "Q1": {
                "question": "|",
                "answer": "a",
                "function": lambda: on_shuffle_choices([
                    "a", "b", "c", "d",]),
                "format": "multiple",
            },
        },
    },
}