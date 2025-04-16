import random

MULTIPLE_CHOICE = "multiple choice"
TRUE_OR_FALSE = "true or false"
FREE_RESPONSE = "free response"

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
                "format": MULTIPLE_CHOICE,
            },
        },
        "another some tag": {
            "Q2": {
                "question": "|",
                "answer": "a",
                "function": None,
                "format": FREE_RESPONSE,
            },
        },
    },
    "Module 2": {
        "another tag": {
            "Q1": {
                "question": "|",
                "answer": "a",
                "function": None,
                "format": TRUE_OR_FALSE,
            },
        },
    },
}