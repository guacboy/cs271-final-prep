import random

MULTIPLE_CHOICE = "multiple choice"
TRUE_OR_FALSE = "true or false"
FREE_RESPONSE = "free response"
SELECT_THAT_APPLY = "select that apply"
MATCH_TO_ANSWER = "match to answer"

question_bank = {
    "Module 1": {
        "some tag": {
            "Q1": {
                "details": {
                    "some question": {
                        "step 1": "answer1",
                        "step 2": "answer2",
                        "step 3": "answer3",
                        "step 4": "answer4",
                    }
                },
                "format": MATCH_TO_ANSWER,
            },
        },
        "another some tag": {
            "Q1": {
                "details": {
                    "some question": [
                        [
                            "this is correct",
                            "this is also correct",
                            "pick this one",
                        ],
                        [
                            "this is incorrect",
                            "this is also incorrect",
                            "do not pick this one",
                        ]
                    ]
                },
                "format": SELECT_THAT_APPLY,
            },
        },
        "another tag": {
            "Q1": {
                "details": {
                    "some question": "reponse1",
                    "another question": "reponse2",
                    "no question": "reponse3",
                    "yes question": "reponse4",
                },
                "format": MULTIPLE_CHOICE,
            },
        },
    },
}