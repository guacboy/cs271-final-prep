import random
import string

def on_randomize_true_false_question(details_dict: dict) -> str:
    """
    Creates a random true or false question given the question details.
    """
    
    # selects a random question
    question_to_be_chosen = [
        question for question in details_dict.keys()
    ]
    question_chosen = random.choice(question_to_be_chosen)
    
    # selects a random answer
    answer_to_be_chosen = [
        answer for answer in details_dict.values()
    ]
    answer_chosen = random.choice(answer_to_be_chosen)
    
    # if the question matches with the answer
    if details_dict[question_chosen] == answer_chosen:
        # then the statement is true
        return question_chosen, answer_chosen, "True"
    # otherwise,
    else:
        # then the statement is false
        return question_chosen, answer_chosen, "False"

class Question():
    # TRUE OR FALSE
    def mod1_binary_octal_decimal_hexadecimal_q1() -> str:
        question_dict = {
            "0": "positive",
            "1": "negative",
        }
        
        question_chosen, answer_chosen, answer = on_randomize_true_false_question(question_dict)
            
        # include the random selection into the question
        question = f"If an integer's sign bit is {question_chosen}, the integer is {answer_chosen}."
        
        return question, answer
    
    # TRUE OR FALSE
    def mod1_binary_octal_decimal_hexadecimal_q2() -> str:
        question_dict = {
            "rightmost": "Least Significant Bit (LSB)",
            "leftmost": "Most Significant Bit (MSB)",
        }
        
        question_chosen, answer_chosen, answer = on_randomize_true_false_question(question_dict)
            
        # include the random selection into the question
        question = f"The {question_chosen} bit is the {answer_chosen}."
        
        return question, answer
    
    # FREE RESPONSE
    def mod1_large_value_prefixes_q2() -> str:
        # select a random size of digit storage
        size_of_storage = random.randint(1, 10)
        storage_type_dict = {
            "KB": 2**10,
            "MB": 2**20,
            "GB": 2**30,
            "TB": 2**40,
            "PB": 2**50,
            "EB": 2**60,
            "ZB": 2**70,
            "YB": 2**80,
        }
        storage_type_to_be_chosen = [
            storage for storage in storage_type_dict.keys()
        ]
        # select a random store type
        storage_type_chosen = random.choice(storage_type_to_be_chosen)
        
        # include the random selections into the question
        question = f"How many bits are there in {str(size_of_storage)}{storage_type_chosen}?\n\nNOTE: For answers larger than 10 digits, only include the first 10 digits.\nFor example, 1.234567890 * 10^20 will be equivalent to 1234567890"
        answer = str(size_of_storage * storage_type_dict[storage_type_chosen] * 8)
        
        # if the answer contains greater than 10 digits
        if len(answer) > 10:
            # include only the first 10 digits
            answer = answer[:10]
        
        return question, answer
    
    # FREE RESPONSE
    def mod1_character_data_type_q1() -> str:
        # chooses a random string length
        string_length = random.randint(5, 15)
        random_string = ""
        
        for s in range(string_length):
            # adds a random ascii character (upper or lower) into the random string
            random_string += random.choice(string.ascii_letters)
        
        # include the random selection into the question
        question = f"How many bytes does it take to represent the following set of characters in ASCII:\n{random_string}"
        answer = str(string_length)
        
        return question, answer
    
    # SELECT THAT APPLY
    def mod1_central_processing_unit_q4():
        correct_answers = [
            "Instruction Pointer",
            "Instruction Register",
            "Instruction Decoder",
            "Control Register",
            "Status Register"
        ]
        incorrect_answers = [
            "Multi-Purpose Register",
            "System Clock",
            "Address Bus",
            "Data Bus",
            "Control Bus",
            "Input/Output Bus",
            "Arithmetic/logic Unit",
            "Memory Address Register",
            "Memory Data Register",
        ]
        
        random.shuffle(correct_answers)
        random.shuffle(incorrect_answers)
        
        amount_of_correct_choices = random.randint(1, len(correct_answers))
        correct_choices = []
        # stores a random amount of correct choices into a list
        # (at least one correct answer will in the list)
        for i in range(amount_of_correct_choices):
            correct_choices.append(correct_answers[i])
        
        incorrect_choices = []
        # fills the rest of the list (maximum of 8) with incorrect choices
        for i in range(8 - amount_of_correct_choices):
            incorrect_choices.append(incorrect_answers[i])
        
        question = "Which of the following are components of the Control Unit?"
        answer = [correct_choices, incorrect_choices] # formatted as a 2D list
        
        return question, answer
    
    # SELECT THAT APPLY
    def mod1_sub_register_access_method_q1():
        registers_dict = {
            "32-bit": [
                "EAX", "EBX", "ECX", "EDX",
                "EBP", "ESI", "EDI", "ESP"
            ],
            "16-bit": [
                "AX", "BX", "CX", "DX",
                "BP", "SI", "DI", "SP"
            ],
            "upper 8-bit": [
                "AH", "BH", "CH", "DH",
            ],
            "lower 8-bit": [
                "AL", "BL", "CL", "DL",
            ],
        }
        # selects a random register type
        register_to_be_chosen = [
            register for register in registers_dict.keys()
        ]
        register_chosen = random.choice(register_to_be_chosen)
        
        # stores the correct answers of the chosen register type
        correct_answers = registers_dict[register_chosen]
        random.shuffle(correct_answers)
        
        choices_to_be_chosen = []
        # iterates through all the register types
        for choices in registers_dict.values():
            # and through all the registers
            for choice in choices:
                # if the register is not the correct answer
                if choice not in correct_answers:
                    # add it to the possible list of choices
                    choices_to_be_chosen.append(choice)
        random.shuffle(choices_to_be_chosen)
        
        amount_of_correct_choices = random.randint(1, len(correct_answers))
        correct_choices = []
        # stores a random amount of correct choices into a list
        # (at least one correct answer will in the list)
        for i in range(amount_of_correct_choices):
            correct_choices.append(correct_answers[i])
        
        incorrect_choices = []
        # fills the rest of the list (maximum of 8) with incorrect choices
        for i in range(8 - amount_of_correct_choices):
            incorrect_choices.append(choices_to_be_chosen[i])
        
        # include the random selection into the question
        question = f"Which of the following are valid {register_chosen} register references?"
        answer = [correct_choices, incorrect_choices] # formatted as a 2D list

        return question, answer
    