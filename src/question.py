import random
import requests
from faker import Faker

WORD_WEBSITE = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")

faker = Faker()

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
    
def on_randomize_select_that_apply_question(correct_answers: list,
                                            incorrect_answers: list) -> list:
    """
    Creates a random select that apply question given the
    list of correct answers and list of incorrect answers.
    """
    
    random.shuffle(correct_answers)
    random.shuffle(incorrect_answers)
    
    amount_of_correct_choices = random.randint(1, len(correct_answers))
    correct_choices = []
    # stores a random amount of correct choices into a list
    # (at least one correct answer will in the list)
    for i in range(amount_of_correct_choices):
        correct_choices.append(correct_answers[i])
    
    # if the amount of correct answers < 8
    if len(incorrect_answers) < 8:
        # then set that amount as the maximum
        maximum_amount_of_choices = len(incorrect_answers)
    # if the amount of correct answers >= 8,
    else:
        # the set 8 as the maximum
        maximum_amount_of_choices = 8
    
    incorrect_choices = []    
    # fills the rest of the list with incorrect choices
    for i in range(maximum_amount_of_choices - amount_of_correct_choices):
        incorrect_choices.append(incorrect_answers[i])
        
    # formatted as a 2D list
    answer = [correct_choices] + [incorrect_choices]
    
    return answer

class Question():
    # TRUE OR FALSE
    def mod1_data_representation_q1() -> str:
        question_dict = {
            "0": "positive",
            "1": "negative",
        }
        
        question_chosen, answer_chosen, answer = on_randomize_true_false_question(question_dict)
            
        # include the random selection into the question
        question = f"If an integer's sign bit is {question_chosen}, the integer is {answer_chosen}."
        
        return question, answer
    
    # TRUE OR FALSE
    def mod1_data_representation_q2() -> str:
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
        # creates a list of words between 5-10 characters
        words_to_be_chosen = [
            word for word in WORD_WEBSITE.text.splitlines()
            if len(word) >= 5 and len(word) <= 10
        ]
        # then selects a random word from the above list
        word_chosen = random.choice(words_to_be_chosen)
        
        # include the random selection into the question
        question = f"How many bytes does it take to represent the following set of characters in ASCII:\n{word_chosen}"
        answer = str(len(word_chosen))
        
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
        
        question = "Which of the following are components of the Control Unit?"
        answer = on_randomize_select_that_apply_question(correct_answers,
                                                         incorrect_answers)
        
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
        
        incorrect_answers = []
        # iterates through all the register types
        for choices in registers_dict.values():
            # and through all the registers
            for choice in choices:
                # if the register is not the correct answer
                if choice not in correct_answers:
                    # add it to the possible list of choices
                    incorrect_answers.append(choice)
        
        # include the random selection into the question
        question = f"Which of the following are valid {register_chosen} register references?"
        answer = on_randomize_select_that_apply_question(correct_answers,
                                                         incorrect_answers)

        return question, answer
    
    # SELECT THAT APPLY
    def mod2_identifiers_q1():
        correct_answers = [
            "can be 1 to 247 characters (no spaces)",
            "are not case sensitive",
            "can start with (and include) letters (A..Z, a..z)",
            "can start with (and include) underscore (_), @, ?, or $",
            "can also include (after the first character) numerical digits",
            "cannot be a reserved word",
        ]
        incorrect_answers = [
            "can contains spaces",
            "are case sensitive",
            "can start with numerical digits",
            "can be a reserved word",
        ]
        
        question = "Identifier names.."
        answer = on_randomize_select_that_apply_question(correct_answers,
                                                         incorrect_answers)
        
        return question, answer
    
    # FREE RESPONSE
    # TODO: fix format; create a code segment question type
    def mod2_memory_addresses_q2() -> str:
        name_chosen = faker.name() # creates a random name
        size_chosen = random.randint(10, 25)
        starting_memory_andress = random.randint(1, 9)
        
        code_segment = f"myName BYTE '{name_chosen}',0" \
            f"\npromptName BYTE {str(size_chosen)} DUP(0)" \
            f"\npromptAge DWORD ?" \
            f"\npromptDate DWORD ?" \
            f"\nelaspedTime WORD ?"
        
        # selects a random identifier to be answered
        identifier_chosen = random.choice([
            "promptAge", "promptDate", "elaspedTime",
        ])
        
        added_amount = 0 # added calculation of digital storage
        if identifier_chosen == "promptDate":
            added_amount = 4
        elif identifier_chosen == "elaspedTime":
            added_amount = 8
        
        # adds together the memory address
        # then converts to hex and uppercase letters
        hex_value = hex((len(name_chosen) + 1) + size_chosen + added_amount).upper()
        
        question = f"{code_segment}\n\nWhat is the hexadecimal address of {identifier_chosen} if the data segment starts at memory address {starting_memory_andress}000h?"
        answer = f"{starting_memory_andress}0{hex_value[2:]}h"
        
        return question, answer
    
    # SELECT THAT APPLY
    def mod2_composition_of_an_instruction_q5():
        instructions_dict = {
            "XCHG": [
                ".. mem, reg", ".. reg, mem",
                ".. reg, reg"
            ],
            "MOV": [
                ".. reg, mem", ".. mem, reg",
                ".. reg, reg", ".. mem, imm",
                ".. reg, imm",
            ],
            "ADD": [
                 ".. reg, reg", ".. mem, reg",
                 ".. reg, imm", ".. mem, imm",
                 ".. reg, mem", ".. accum, imm",
            ],
        }
        # selects a random instruction
        instruction_to_be_chosen = [
            register for register in instructions_dict.keys()
        ]
        instruction_chosen = random.choice(instruction_to_be_chosen)
        
        # stores the correct answers of the chosen instruction type
        correct_answers = instructions_dict[instruction_chosen]
        
        incorrect_answers = [] + [
            ".. mem, mem", ".. imm, reg",
            ".. imm, imm",
        ]
        # iterates through all the register types
        for choices in instructions_dict.values():
            # and through all the instructions
            for choice in choices:
                # if the register is not the correct answer
                if choice not in correct_answers:
                    # add it to the possible list of choices
                    incorrect_answers.append(choice)
        
        # include the random selection into the question
        question = f"Which of the following are valid uses of the {instruction_chosen} instruction?"
        answer = on_randomize_select_that_apply_question(correct_answers,
                                                         incorrect_answers)
        
        return question, answer
    
    # FREE RESPONSE
    def mod2_instruction_mnemonics_q3() -> str:
        first_integer = random.randint(1, 9)
        second_integer = random.randint(1, 9)
        
        code_segment = f"MOV val, {first_integer}" \
            f"\nCMP val, {second_integer}"
        
        carry_flag = 0 # set if result requires a borrow
        zero_flag = 0 # set if the result is zero
        sign_flag = 0 # set if the result is negative
        compare_integers = first_integer - second_integer
        
        # if the result is a negative
        if compare_integers < 0:
            carry_flag = 1
            sign_flag = 1
        # if the result is a zero
        if compare_integers == 0:
            zero_flag = 1
        
        question = f"{code_segment}\n\nWhat are the correct values of the Carry, Zero, and Sign flags after the following instructions execute?\n\nNOTE: Type the answer in order separated by a comma. For example: 1,0,1 is equivalent to Carry = 1, Zero = 0, Sign = 1."
        answer = f"{carry_flag},{zero_flag},{sign_flag}"
        
        return question, answer
    
    # FREE RESPONSE
    def mod2_instruction_mnemonics_q5() -> str:
        first_integer = random.randint(1, 9)
        second_integer = random.randint(1, 9)
        third_integer = random.randint(1, 9)
        
        code_segment = f"MOV EAX, {first_integer}" \
            f"\nMOV EBX, {second_integer}" \
            f"\nMOV ECX, {third_integer}" \
            f"\nADD EAX, EBX" \
            f"\nSUB EAX, ECX" \
        
        # ADD EAX with EBX, then SUB EAX with ECX
        eax_result = first_integer + second_integer - third_integer
        
        question = f"{code_segment}\n\nAfter the MASM code is executed, what are the decimal values in the EAX, EBX, and ECX?\n\nNOTE: Type the answer in order separated by a comma. For example: 2,5,0 is equivalent to EAX = 1, EBX = 0, ECX = 1."
        answer = f"{eax_result},{second_integer},{third_integer}"
        
        return question, answer
    
    # FREE RESPONSE
    def mod2_instruction_mnemonics_q6() -> str:
        first_integer = random.randint(25, 100)
        second_integer = random.randint(2, 10)
        
        code_segment = f"MOV EAX, {first_integer}" \
            f"\nMOV EBX, {second_integer}" \
            f"\nMOV EDX, 0" \
            f"\nDIV EBX" \
        
        # DIV EAX with EBX
        eax_result = int(first_integer / second_integer)
        edx_result = first_integer % second_integer
        
        question = f"{code_segment}\n\nAfter the MASM code is executed, what are the decimal values in the EAX, EBX, and EDX?\n\nNOTE: Type the answer in order separated by a comma. For example: 2,5,0 is equivalent to EAX = 1, EBX = 0, EDX = 1."
        answer = f"{eax_result},{second_integer},{edx_result}"
        
        return question, answer