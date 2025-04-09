import random

def some_tag() -> None:
    print("some tag")

def another_tag() -> None:
    print("another tag")

question_bank = {
    "Module 1": {
        "some tag": {
            "Q1": {
                "question": "some question",
                "answer": "some answer",
                "function": lambda: some_tag(),
                "format": None,
            },
        },
        "another some tag": {
            "Q2": {
                "question": "another some question",
                "answer": "another some answer",
                "function": lambda: some_tag(),
                "format": None,
            },
        },
    },
    "Module 2": {
        "another tag": {
            "Q1": {
                "question": "another question",
                "answer": "another answer",
                "function": lambda: another_tag(),
                "format": None,
            },
        },
    },
}