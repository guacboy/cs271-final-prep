import random

MULTIPLE_CHOICE = "multiple choice"
TRUE_OR_FALSE = "true or false"
FREE_RESPONSE = "free response"
SELECT_THAT_APPLY = "select that apply"

def on_shuffle_choices(choices: list) -> list:
    random.shuffle(choices)
    return choices

question_bank = {
    "Module 1": {
        "some tag": {
            "Q1": {
                "question": "some tag q1",
                "answer": {"a"},
                "function": lambda: on_shuffle_choices([
                    "a", "test answer", "c", "d",]),
                "format": SELECT_THAT_APPLY,
            },
        },
        "another some tag": {
            "Q2": {
                "question": "another some tag q2",
                "answer": "a",
                "function": None,
                "format": FREE_RESPONSE,
            },
        },
    },
    "Module 2": {
        "another tag": {
            "Q1": {
                "question": "another tag q1",
                "answer": "a",
                "function": None,
                "format": TRUE_OR_FALSE,
            },
            "Q2": {
                "question": "another tag q2",
                "answer": {
                    "a", "d"},
                "function": lambda: on_shuffle_choices([
                    "a", "what not to do at a stop light", "c", "d", "e", "f"]),
                "format": SELECT_THAT_APPLY,
            },
        },
    },
}