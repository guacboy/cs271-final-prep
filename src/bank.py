import random

def on_shuffle_choices(choices: list) -> list:
    random.shuffle(choices)
    return choices

question_bank = {
    "Module 1": {
        "some tag": {
            "Q1": {
                "question": "|",
                "answer": "some answer",
                "function": lambda: on_shuffle_choices([
                    "a", "b", "c", "d"]),
                "format": "radio",
            },
        },
        "another some tag": {
            "Q2": {
                "question": "|",
                "answer": "another some answer",
                "function": lambda: on_shuffle_choices([
                    "a", "b", "c", "d"]),
                "format": "radio",
            },
        },
    },
    "Module 2": {
        "another tag": {
            "Q1": {
                "question": "|",
                "answer": "another answer",
                "function": lambda: on_shuffle_choices([
                    "a", "b", "c", "d"]),
                "format": "radio",
            },
        },
    },
}