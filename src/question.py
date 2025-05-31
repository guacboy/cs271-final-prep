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
    def mod1_data_arithmetics_q1() -> str:
        arithmetic_chosen = random.choice([
            "unsigned addition",
            "signed subtraction",
        ])
        
        # if the arithmetic is addition
        if arithmetic_chosen == "unsigned addition":
            arithmetic_dict = {
                "  00010111" \
                "\n+ 01011101": "01110100",
                "  10000111" \
                "\n+ 01110001": "11111000",
                "  10111010" \
                "\n+ 10110001": "1101011",
                "  10111011" \
                "\n+ 00110001": "11101100",
                "  1A2F" \
                "\n+ 4742": "6171",
                "  2C19" \
                "\n+ 570B": "8324",
                "  2C25" \
                "\n+ 574B": "8370",
            }
        # if the arithmetic is subtraction
        elif arithmetic_chosen == "signed subtraction":
            arithmetic_dict = {
                "  01011101" \
                "\n- 00011000": "01110100",
                "  10110110" \
                "\n- 00010001": "10100101",
                "  10010110" \
                "\n- 01111001": "00011101",
                "  4742" \
                "\n- 1A2F": "2D13",
                "  C48A" \
                "\n- AACC": "19BE",
                "  6A6F" \
                "\n- 1F89": "4AE6",
            }
        
        # selects a random problem and result
        question_to_be_chosen = [
            (problem, result) for (problem, result) in arithmetic_dict.items()
        ]
        question_chosen = random.choice(question_to_be_chosen)
        problem_chosen = question_chosen[0]
        result_chosen = question_chosen[1]
        
        # include the random selections into the question
        question = f"Compute the following {arithmetic_chosen}.\n\n{problem_chosen}\n\nNOTE: Do not include commas or spaces. For example: 11001100"
        answer = result_chosen
        
        return question, answer
    
    # FIXME: last digit not rounding properly
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
        question = f"How many bits are there in {str(size_of_storage)}{storage_type_chosen}?" \
            "\n\nNOTE: For answers larger than 10 digits, " \
            "only include the first 10 digits rounded to the nearest integer." \
            "\nFor example: 1.2345678905 * 10^20 will be equivalent to 1234567891"
        answer = str(size_of_storage * storage_type_dict[storage_type_chosen] * 8)
        
        # if the answer contains greater than 10 digits
        if len(answer) > 10:
            # round up to nearest integer
            if int(answer[10]) >= 5:
                answer = answer.replace(answer[9], str(int(answer[9]) + 1))
            
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
        
        question = f"{code_segment}\n\nWhat are the correct values of the Carry, Zero, and Sign flags after the following instructions execute?\n\nNOTE: Type the answer in order separated by a comma (no spaces). For example: 1,0,1 is equivalent to Carry = 1, Zero = 0, Sign = 1"
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
        
        question = f"{code_segment}\n\nAfter the MASM code is executed, what are the decimal values in the EAX, EBX, and ECX?\n\nNOTE: Type the answer in order separated by a comma (no spaces). For example: 2,5,0 is equivalent to EAX = 1, EBX = 0, ECX = 1."
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
        
        question = f"{code_segment}\n\nAfter the MASM code is executed, what are the decimal values in the EAX, EBX, and EDX?\n\nNOTE: Type the answer in order separated by a comma (no spaces). For example: 2,5,0 is equivalent to EAX = 1, EBX = 0, EDX = 1."
        answer = f"{eax_result},{second_integer},{edx_result}"
        
        return question, answer
    
    # TRUE OR FALSE
    def mod3_jumps_q1() -> str:
        question_dict = {
            "Conditional branching": "results vary on the outcome of a logical condition",
            "Unconditional branching": "results do not vary on the outcome of a logical condition",
        }
        
        question_chosen, answer_chosen, answer = on_randomize_true_false_question(question_dict)
            
        # include the random selection into the question
        question = f"{question_chosen} means {answer_chosen}."
        
        return question, answer
    
    # FREE RESPONSE
    def mod3_jumps_q5() -> str:
        first_value = random.randint(1, 9)
        second_value = random.randint(1, 9)
        jcond_chosen = random.choice([
            "G", "L",
        ])
        
        code_segment = ".data" \
            "\nyes BYTE 'Yes',0" \
            "\nno BYTE 'No',0" \
            "\n\n.code" \
                f"\nMOV EAX, {first_value}" \
                f"\nCMP EAX, {second_value}" \
                f"\nJ{jcond_chosen} _printYes" \
                "\nMOV EDX, OFFSET no" \
                "\nJMP _finished" \
            "\n\n_printYes:" \
                "\nMOV EDX, OFFSET yes" \
            "\n\n_finished:" \
                "\nCALL WriteString" \
        
        # if jcond is JG, then
        if jcond_chosen == "G":
            # if the first value > second value
            if first_value > second_value:
                answer = "Yes"
            # if the first value <= second value
            else:
                answer = "No"
        # if jcond is JL, then
        if jcond_chosen == "L":
            # if the first value < second value
            if first_value < second_value:
                answer = "Yes"
            # if the first value >= second value
            else:
                answer = "No"
        
        question = f"{code_segment}\n\nGiven the above MASM code, what is printed to the console window?"
        
        return question, answer
    
    # TRUE OR FALSE
    def mod3_loops_q1() -> str:
        question_dict = {
            "Post-test loop": "execute one-or-more times; the control condition must therefore be checked immediately after the first execution of the loop body",
            "Pre-test loop": "execute zero-or-more times; the control condition must therefore be checked before the first execution of the loop body",
        }
        
        question_chosen, answer_chosen, answer = on_randomize_true_false_question(question_dict)
            
        # include the random selection into the question
        question = f"{question_chosen} will {answer_chosen}."
        
        return question, answer
    
    # FREE RESPONSE
    def mod3_loops_q4() -> str:
        eax_value = random.randint(1, 9)
        ebx_value = random.randint(1, 9)
        ecx_value = random.randint(2, 4)
        change_value = random.randint(1, 2)
        instruction_chosen = random.choice([
            "ADD", "SUB"
        ])
        
        code_segment = f"MOV EAX, {eax_value}" \
            f"\nMOV EBX, {ebx_value}" \
            f"\nMOV ECX, {ecx_value}" \
            f"\n\n_{instruction_chosen.lower()}Value:" \
                f"\n{instruction_chosen} EAX, EBX" \
                f"\n{instruction_chosen} EBX, {change_value}" \
                f"\nLOOP _{instruction_chosen.lower()}Value" \
                "\nMOV result, EAX"
        
        # iterates ECX amount
        for i in range(ecx_value):
            # if instruction is to add,
            if instruction_chosen == "ADD":
                # adds EAX with EBX
                eax_value += ebx_value
                # adds EBX with the changed value
                ebx_value += change_value
            # if instruction is to subtract,
            elif instruction_chosen == "SUB":
                # subtracts EAX with EBX
                eax_value -= ebx_value
                # subtracts EBX with the changed value
                ebx_value -= change_value
        
        answer = str(eax_value)
        
        question = f"{code_segment}\n\nSuppose that 'result' is declared as DWORD. Given the above MASM code, what is the value stored in the memory location named 'result'?"
        
        return question, answer
    
    # FREE RESPONSE
    def mod4_endianness_q6() -> str:
        endian_chosen = random.choice([
            "big-endian", "little-endian"
        ])
        
        hex_value = "".join(
            random.choice("0123456789ABCDEF")
            for i in range(8)
        )
        
        answer = ""
        # if little endian,
        if endian_chosen == "little-endian":
            # then set the answer in reverse human-readable order
            for i in range(len(hex_value) - 1, 0, -2):
                answer += f"{hex_value[i - 1]}{hex_value[i]}"
        # if big endian, 
        elif endian_chosen == "big-endian":
            # then set the answer in human-readable order
            answer = hex_value
        
        question = f"Given the value, {hex_value}h, what is the hex value stored in memory on a {endian_chosen} system?\n\nNOTE: Do not include 'h' in your answer. For example: FFFB29B8"
        
        return question, answer
    
    # TRUE OR FALSE
    def mod4_endianness_q7() -> str:
        question_dict = {
            "x86-64 systems": "little-endian",
            "internet": "big-endian",
        }
        
        question_chosen, answer_chosen, answer = on_randomize_true_false_question(question_dict)
            
        # include the random selection into the question
        question = f"The {question_chosen} default to {answer_chosen} byte ordering."
        
        return question, answer
    
    # FREE RESPONSE
    def mod4_endianness_q9() -> str:
        endian_chosen = random.choice([
            "big-endian", "little-endian"
        ])
        
        decimal_value_list = []
        hex_value_list = []
        for i in range(3):
            hex_value = "".join(
                random.choice("0123456789ABCDEF")
                for i in range(random.choice([2, 4]))
            )
            hex_value_list.append(hex_value)
            decimal_value_list.append(int(hex_value, 16)) # hex -> decimal
        
        code_segment = f"someArray WORD {decimal_value_list[0]}, " \
            f"{decimal_value_list[1]}, " \
            f"{decimal_value_list[2]} "
        
        answer = ""
        # if little endian,
        if endian_chosen == "little-endian":
            # iterates through the list of hex values
            for i in range(len(hex_value_list)):
                # and set the answer in reverse human-readable order
                # (does not set the list in reverse order,
                # only the value inside the list)
                for j in range(len(hex_value_list[i]) - 1, 0, -2):
                    answer += f"{hex_value_list[i][j - 1]}{hex_value_list[i][j]}"
        # if big endian, 
        elif endian_chosen == "big-endian":
            # then set the answer in human-readable order
            answer = "".join(hex_value_list)
        
        question = f"{code_segment}\n\nGiven the data segment, what is the hex value stored in memory on a {endian_chosen} system?\n\nNOTE: Do not include 'h' in your answer. For example: FFFB29B8"
        
        return question, answer
    
    # SELECT THAT APPLY
    def mod4_ieee_754_floating_point_q3():
        sign_chosen = random.choice([
            "positive", "negative"
        ])
        positive_values = [
            "0", "1", "2", "3", "4", "5", "6", "7"
        ]
        negative_values = [
            "8", "9", "A", "B", "C", "D", "E", "F"
        ]
        
        correct_answers = []
        incorrect_answers = []
        for i in range(8):
            # if there are currently no correct answers,
            # then add at least one correct answer
            if len(correct_answers) <= 0:
                # if creating a positive value
                if sign_chosen == "positive":
                    hex_value = f"{"".join(
                        random.choice("01234567"))}" \
                            f"{"".join(
                        random.choice("0123456789ABCDEF")
                        for i in range(random.randint(3, 7))
                    )}h"
                # if creating a negative value
                elif sign_chosen == "negative":
                    hex_value = f"{"".join(
                        random.choice("89ABCDEF"))}" \
                            f"{"".join(
                        random.choice("0123456789ABCDEF")
                        for i in range(random.randint(3, 7))
                    )}h"
            # if there is already at least one correct answer,
            else:
                # then create a random hex value
                hex_value = f"{"".join(
                    random.choice("0123456789ABCDEF")
                    for i in range(random.randint(4, 8))
                )}h"

            # if sign looking for is positive
            # and the first hex value is also positive,
            if (sign_chosen == "positive"
                and hex_value[0] in positive_values):
                # then add as a correct answer
                correct_answers.append(hex_value)
            # if sign looking for is negative
            # and the first hex value is also negative
            elif (sign_chosen == "negative"
                and hex_value[0] in negative_values):
                # then add as a correct answer
                correct_answers.append(hex_value)
            # if sign looking for doesn't match with the first hex value,
            else:
                # then add as an incorrect answer
                incorrect_answers.append(hex_value)
        
        question = f"Without decoding, indicate which of the following IEEE 754 single-precision values represent a {sign_chosen} values."
        answer = on_randomize_select_that_apply_question(correct_answers,
                                                         incorrect_answers)
        
        return question, answer
    
    # FREE RESPONSE
    def mod4_ieee_754_floating_point_q4() -> str:
        conversion_chosen = random.choice([
            "encoding", "decoding"
        ])
        
        hex_dict = {
            "42AA4000": "85.125",
            "C1A98000": "-21.1875",
            "42E48000": "114.25",
            "3EA00000": "0.3125",
            "C2032000": "-32.78125",
            "C19B8000": "-19.4375",
            "C3FC3000": "-504.375",
            "C4C83400": "-1,601.625",
        }
        
        # hex_value_chosen = random.choice([
        #     "42AA4000",
        #     "C1A98000"
        # ])
    
        # # if IEEE 754 floating-point -> decimal floating-point
        # # hex -> binary
        # binary_value = bin(int(hex_value_chosen, 16))[2:].zfill(len(hex_value_chosen) * 4)
        # sign_bit = binary_value[0]
        # biased_exponent = binary_value[1:9]
        # normalized_mantissa = binary_value[9:]
        
        # # exponent's binary -> decimal
        # exponent_decimal_value = 0
        # power = 0
        # for bit in biased_exponent[::-1]:
        #     if bit == "1":
        #         exponent_decimal_value += 2**power
        #     power += 1
        # debiased_exponent = exponent_decimal_value - 127
        
        # zero_bit_count = len(normalized_mantissa)
        # # drops any trailing zeros in the normalized mantissa
        # for bit in normalized_mantissa[::-1]:
        #     if bit == "1":
        #         mantissa_string = normalized_mantissa[:zero_bit_count]
        #         break
        #     zero_bit_count -= 1  
        # # front-pad the mantissa with 1.  
        # mantissa_string = f"1.{mantissa_string}"
        
        # # converts the string into a list excluding the decimal point
        # mantissa_list = [
        #         bit for bit in mantissa_string
        #         if bit != "."
        #     ]
        # # moves the decimal point in accordance to the debiased exponent
        # mantissa_list.insert(debiased_exponent + 1, ".")
        
        # whole_mantissa_string = ""
        # fraction_mantissa_string = ""
        # is_decimal_point_found = False
        # # reverts the list into a string
        # for bit in mantissa_list:
        #     # if the bit is a decimal point,
        #     if bit == ".":
        #         # update that the decimal point has been found
        #         is_decimal_point_found = True
        #         # and continue loop
        #         continue
        #     # if the decimal point has already been iterated
        #     if is_decimal_point_found:
        #         fraction_mantissa_string += bit
        #     # if the decimal point has not been iterated yet
        #     else:
        #         whole_mantissa_string += bit
                
        # # binary -> decimal
        # whole_decimal_value = 0
        # whole_power = 0
        # # sums together the decimal whole value
        # for bit in whole_mantissa_string[::-1]:
        #     if bit == "1":
        #         whole_decimal_value += 2**whole_power
        #     whole_power += 1
        
        # # sums together the decimal fraction value
        # # (also including the decimal whole value)
        # fraction_decimal_value = 0
        # fraction_power = -1
        # for bit in fraction_mantissa_string:
        #     if bit == "1":
        #         fraction_decimal_value += 2**fraction_power
        #     fraction_power -= 1
        
        # # if the sign bit was 1,
        # if sign_bit == "1":
        #     # then the final value is negative
        #     whole_decimal_value *= -1
        
        # # formats the decimal values together
        # final_decimal_value = f"{whole_decimal_value}.{str(fraction_decimal_value)[2:]}"
        
        # # if IEEE 754 floating-point -> decimal floating-point
        # if conversion_chosen == "decoding": 
        #     # then set the answer to the final decimal value
        #     answer = final_decimal_value
        
        # # if decimal floating-point -> IEEE 754 floating-point
        # if conversion_chosen == "encoding":
        #     # then use the now "confirmed to not contain a repeating decimal" decimal value
        #     # and convert decimal -> binary
        #     whole_binary_value_list = []
        #     while whole_decimal_value != 0:
        #         # adds the remainder to the list
        #         whole_binary_value_list.append(whole_decimal_value % 2)
        #         # divide by two and get the whole number
        #         whole_decimal_value = int(whole_decimal_value / 2)
            
        #     whole_binary_value = ""
        #     # iterates through the list in reverse
        #     for bit in whole_binary_value_list[::-1]:
        #         whole_binary_value += str(bit)
                    
        #     fraction_binary_value = ""
        #     while fraction_decimal_value != 0:
        #         fraction_decimal_value = fraction_decimal_value * 2
        #         # add the whole number value from the fraction decimal result
        #         fraction_binary_value += str(int(fraction_decimal_value))
        #         # repeat the calculation with only the decimal portion
        #         fraction_decimal_value = abs(fraction_decimal_value) % 1
            
        #     # format the binary value
        #     binary_value = f"{whole_binary_value}.{fraction_binary_value}"
            
        #     # TODO: finish encoding
            
        #     answer = ""
        
        # selects a random question from the question bank
        question_to_be_chosen = [
            (hex, decimal) for (hex, decimal) in hex_dict.items()
        ]
        question_chosen = random.choice(question_to_be_chosen)
        hex_value_chosen = question_chosen[0]
        decimal_value_chosen = question_chosen[1]
        
        # if decimal floating-point -> IEEE 754 floating-point
        if conversion_chosen == "encoding":
            answer = hex_value_chosen
            
            convert_from = f"decimal floating-point, {decimal_value_chosen},"
            convert_to = "single-precision IEEE 754 floating-point hexadecimal"
        # if IEEE 754 floating-point -> decimal floating-point
        elif conversion_chosen == "decoding":
            answer = decimal_value_chosen
            
            convert_from = f"single-precision IEEE 754 floating-point hexadecimal, {hex_value_chosen},"
            convert_to = "decimal floating-point"
        
        question = f"Convert {convert_from} to {convert_to}.\n\nNOTE: Do not include 'h' in your answer and don't front-pad the final hex value. For example: F3B96000"
        
        return question, answer
    
    # FREE RESPONSE
    def mod5_runtime_stack_q1() -> str:
        first_hex_value = f"{"".join(
            random.choice("0123456789ABCDEF")
            for i in range(1))}"
        last_hex_value = random.randint(4, 5)
              
        instruction_chosen = random.choice([
            "PUSH", "POP"
        ])
        
        four_byte_registers = [
            "EAX", "EBX", "ECX", "EDX",
        ]
        two_byte_registers = [
            "AX", "BX", "CX", "DX",
        ]
        registers_to_be_chosen = four_byte_registers + two_byte_registers
        register_chosen = random.choice(registers_to_be_chosen)
        
        # if the register is 4 byte in size
        if register_chosen in four_byte_registers:
            register_size = 4
        # if the register is 2 byte in size
        elif register_chosen in two_byte_registers:
            register_size = 2
        
        # if the instruction is PUSH,
        if instruction_chosen == "PUSH":
            # then subtract the last hex value by the register's size
            answer = f"00{first_hex_value + str(last_hex_value - register_size)}"
        # if the instruction is POP,
        elif instruction_chosen == "POP":
            # then add the last hex value by the register's size
            answer = f"00{first_hex_value + str(last_hex_value + register_size)}"
        
        question = f"Assume ESP = 00{first_hex_value + str(last_hex_value)}h, and then {instruction_chosen} {register_chosen} is executed. What is the new value of ESP?\n\nNOTE: Do not include 'h' in your answer. For example: 00F4"
        
        return question, answer
    
    # TRUE OR FALSE
    def mod5_runtime_stack_q3() -> str:
        question_dict = {
            "pushed": "decremented",
            "popped": "incremented",
        }
        
        question_chosen, answer_chosen, answer = on_randomize_true_false_question(question_dict)
            
        # include the random selection into the question
        question = f"In the IA32 architecture, ESP is {answer_chosen} each time data is {question_chosen} onto the stack."
        
        return question, answer
    
    # FREE RESPONSE
    def mod5_runtime_stack_q4() -> str:
        eax_value = random.randint(1, 100)
        ebx_value = random.randint(1, 100)
        ecx_value = random.randint(1, 100)
        edx_value = random.randint(1, 100)
        register_chosen = random.choice([
            "EAX", "EBX", "ECX", "EDX"
        ])
        
        push_instruction_list = [
            ["PUSH EAX", eax_value],
            ["PUSH EBX", ebx_value],
            ["PUSH ECX", ecx_value],
            ["PUSH EDX", edx_value],
        ]
        pop_instruction_list = [
            "POP ECX",
            "POP EDX",
            "POP EBX",
            "POP EAX",
        ]
        # to keep track of newly assigned values
        pop_instruction_dict = {
            "POP ECX": ecx_value,
            "POP EDX": edx_value,
            "POP EBX": ebx_value,
            "POP EAX": eax_value,
        }
        
        random.shuffle(push_instruction_list)
        random.shuffle(pop_instruction_list)
        
        # inserts the execution point at a random location
        # within the pop instructions
        pop_instruction_list.insert(
            random.randint(0, len(pop_instruction_list) - 1),
            "; Execution Point B"
        )
        
        push_instruction_string = f"{push_instruction_list[0][0]}" \
            f"\n{push_instruction_list[1][0]}" \
            f"\n{push_instruction_list[2][0]}" \
            f"\n{push_instruction_list[3][0]}"
                
        pop_instruction_string = f"{pop_instruction_list[0]}" \
            f"\n{pop_instruction_list[1]}" \
            f"\n{pop_instruction_list[2]}" \
            f"\n{pop_instruction_list[3]}" \
            f"\n{pop_instruction_list[4]}"
        
        code_segment = f"MOV EAX, {eax_value}" \
            f"\nMOV EBX, {ebx_value}" \
            f"\nMOV ECX, {ecx_value}" \
            f"\nMOV EDX, {edx_value}" \
            "\n; Execution Point A" \
            f"\n{push_instruction_string}" \
            f"\n{pop_instruction_string}" \
        
        hex_value = f"{"".join(
            random.choice("0123456789ABCD")
            for i in range(4))}"
        decimal_value = int(hex_value, 16) # hex -> decimal
        # subtract 16 to the decimal value because
        # four "push instructions" will have already been performed
        decimal_value -= 16
        
        # creates a list of the register values
        # in the order it was "pushed" into the stack
        answer_stack = [
            value[1] for value in push_instruction_list
        ]
        # iterates through the pop instruction order
        for instruction in pop_instruction_list:
            # if the instruction is an execution point,
            if instruction == "; Execution Point B":
                # then convert decimal value into hex value
                final_hex_value = hex(decimal_value)[2:].upper()
                # and stop the loop
                break
            # otherwise, assign the register with the last value
            # of the above list
            pop_instruction_dict[instruction] = answer_stack.pop()
            # "pop instruction" increments the ESP by 4
            decimal_value += 4
        
        question = f"{code_segment}\n\nAssume ESP = {hex_value}h at Execution Point A. At Execution Point B, what is the decimal value in {register_chosen}, the hexadecimal value in ESP, and the decimal value in [ESP]?\n\nNOTE: Type the answer in order separated by a comma (no spaces) and o not include 'h' in your answer. For example: 7,1C2F,99"
        answer = f"{pop_instruction_dict["POP " + register_chosen]},{final_hex_value},{answer_stack[-1]}"
        
        return question, answer
    
    # SELECT THAT APPLY
    def mod5_runtime_stack_q5():
        correct_answers = [
            "PUSH",
            "RET",
            "POP",
            "CALL",
        ]
        incorrect_answers = [
            "ADD",
            "SUB",
            "MOV",
            "JMP",
            "CLD",
            "CMP",
            "INC",
            "DEC",
            "LOOP",
        ]
        
        question = "Which of the following instructions always modify the ESP register?"
        answer = on_randomize_select_that_apply_question(correct_answers,
                                                         incorrect_answers)
        
        return question, answer
    
    # TRUE OR FALSE
    def mod6_parity_bits_q1() -> str:
        question_dict = {
            "even": "even",
            "odd": "odd",
        }
        
        question_chosen, answer_chosen, answer = on_randomize_true_false_question(question_dict)
            
        # include the random selection into the question
        question = f"An {question_chosen} parity system requires an {answer_chosen} number of '1'-bits for parity."
        
        return question, answer
    
    # TRUE OR FALSE
    def mod6_parity_bits_q2() -> str:
        parity_chosen = random.choice([
            "odd", "even",
        ])
        
        bits_chosen_list = []
        # creates a list of zeros and ones
        for i in range(4):
            for j in range(4):
                bits_chosen_list.append(random.choice("01"))
            # adds a space between every four bits,
            # except for after the last four
            if i < 3:
                bits_chosen_list.append(" ")
        # joins the list together to create a string
        bits_chosen = "".join(bits_chosen_list)
        
        one_count = 0
        # counts for every bit = 1
        for bit in bits_chosen:
            if bit == "1":
                one_count += 1
        
        # if odd-parity and even # of 1 bits
        if parity_chosen == "odd" and one_count % 2 == 0:
            answer = "True"
        # if even-parity and odd # of 1 bits
        elif parity_chosen == "even" and one_count % 2 != 0:
            answer = "True"
        # otherwise,
        else:
            answer = "False"
            
        # include the random selection into the question
        question = f"Given an {parity_chosen}-parity system which checks parity 16 bits at a time, the following data would be flagged as having an error.\n\n{bits_chosen}"
        
        return question, answer
    
    # FREE RESPONSE
    def mod7_referencing_stack_passed_parameters_q1():
        ebx = []
        # generates random values
        for i in range(6):
            ebx.append("".join(
                random.choice("0123456789ABCDEF")
                for i in range(2)))
            
        edx = []
        # generates random values
        for i in range(13):
            edx.append("".join(
                random.choice("0123456789ABCDEF")
                for i in range(2)))
        
        ebx_string = ""
        # converts the ebx array into a string
        for i in range(0, len(ebx), 2):
            ebx_string += ebx[i + 1]
            ebx_string += ebx[i]
            
            # if it is the last idx,
            if i == len(ebx) - 2:
                # then add the hex radix
                ebx_string += "h"
            # if an even idx (aka. for every two hex values)
            # and it is not the last idx,
            elif (i % 2 == 0
                and i <= len(ebx) - 2):
                # then add the hex radix and comma
                ebx_string += "h, "
                
        edx_string = ""
        # converts the edx array into a string
        for i in range(0, len(edx), ):
            edx_string += edx[i]
            
            # if it is the last idx,
            if i == len(edx) - 1:
                # then add the hex radix
                edx_string += "h"
            # if it is not the last idx,
            elif (i < len(edx)):
                # then add the hex radix and comma
                edx_string += "h, "
        
        code_segment = ".data" \
            f"\nmyArr1 WORD {ebx_string}" \
            f"\nmyArr2 BYTE {edx_string}" \
            "\n\n.code" \
            "\nmain PROC" \
            "\nMOV EBX, OFFSET myArr1" \
            "\nMOV EDX, OFFSET myArr2" \
            "\nexit" \
            "\nmain ENDP"
        
        register_type_chosen = random.choice(["AL", "AX", "EAX"])
        register_chosen = random.choice(["EBX", "EDX"])
        register_offset_chosen = random.randint(1, 6)
        
        # if it is *this* specific register,
        if register_type_chosen == "AL":
            # then assign the register storage size
            array_value_length = 1
        elif register_type_chosen == "AX":
            array_value_length = 2
        elif register_type_chosen == "EAX":
            array_value_length = 4
        
        # if EBX was chosen
        # and the register offset and register storage size > ebx array,
        if (register_chosen == "EBX"
            and register_offset_chosen + array_value_length > len(ebx)):
            # then combine ebx and edx into one array 
            array = ebx + edx
        # if EBX was chosen,
        elif register_chosen == "EBX":
            # then assign to ebx array
            array = ebx
        # if EDX was chosen,
        elif register_chosen == "EDX":
            # then assign to edx array
            array = edx
        
        answer = []
        # start: register offset, stop: register offset + register storage size
        for i in range(register_offset_chosen, register_offset_chosen + array_value_length):
            answer.append(array[i])
            
        answer.reverse()
        answer = "".join(answer)
        
        question = f"{code_segment}\n\nGiven the above data segment, what is the hex value after 'MOV {register_type_chosen}, [{register_chosen}+{str(register_offset_chosen)}]' is performed'?\n\nNOTE: Do not include 'h' in your answer. For example: 00F4"
        
        return question, answer
    
    # FREE RESPONSE
    def mod7_operators_q2():
        array = []
        # generates random values
        for i in range(6):
            array.append("".join(
                random.choice("0123456789ABCDEF")
                for i in range(2)))
                
        array_string = ""
        # converts the array array into a string
        for i in range(0, len(array), ):
            array_string += array[i]
            
            # if it is the last idx,
            if i == len(array) - 1:
                # then add the hex radix
                array_string += "h"
            # if it is not the last idx,
            elif (i < len(array)):
                # then add the hex radix and comma
                array_string += "h, "
        
        var_storage_chosen = random.choice(["DWORD", "WORD", "BYTE"])
        
        # if it is *this* specific variable storage,
        if var_storage_chosen == "DWORD":
            # then assign the variable storage size
            var_storage = 4
        elif var_storage_chosen == "WORD":
            var_storage = 2
        elif var_storage_chosen == "BYTE":
            var_storage = 1
            
        code_segment = ".data" \
            f"\nmyPtrCheck BYTE {array_string}" \
            "\n\n.code" \
            "\nmain PROC" \
            "\n; ..." \
            f"\nMOV EAX, {var_storage_chosen} PTR myPtrCheck" \
            "\n; Execution Point A" \
            "\n; ..." \
            "\nexit" \
            "\nmain ENDP"
        
        answer = []
        for i in range(0, var_storage):
            answer.append(array[i])
            
        answer.reverse()
        answer = "".join(answer)
        
        question = f"{code_segment}\n\nGiven the above data segment, what hexadecimal value does EAX contain at Execution Point A?\n\nNOTE: Do not include 'h' in your answer. For example: 00F4"
        
        return question, answer
    
    # FREE RESPONSE
    def mod7_operators_q3():
        length_chosen = random.randint(4, 8)
        array = []
        # generates random values
        for i in range(length_chosen):
            array.append(random.randint(1, 9999))
                
        array_string = ""
        # converts the array array into a string
        for i in range(0, len(array), ):
            array_string += str(array[i])

            # if it is not the last idx,
            if (i < len(array) - 1):
                # then add a spacing and a comma
                array_string += ", "
        
        var_storage_chosen = random.choice(["DWORD", "WORD", "BYTE"])
        
        # if it is *this* specific variable storage,
        if var_storage_chosen == "DWORD":
            # then assign the variable storage size
            var_storage = 4
        elif var_storage_chosen == "WORD":
            var_storage = 2
        elif var_storage_chosen == "BYTE":
            var_storage = 1
            
        code_segment = ".data" \
            f"\nidArray {var_storage_chosen} {array_string}" \
            f"\nidLength DWORD LENGTHOF idArray" \
            f"\nidSize DWORD SIZEOF idArray" \
            f"\nidType DWORD TYPE idArray" \
        
        subquestion_chosen = random.choice(["LENGTHOF", "SIZEOF", "TYPE"])
        # if it is *this* subquestion,
        if subquestion_chosen == "LENGTHOF":
            # then assign the respective answer
            answer = str(len(array))
            # and its subquestion string
            subquestion_string = "idLength"
        elif subquestion_chosen == "SIZEOF":
            answer = str(len(array) * var_storage)
            subquestion_string = "idSize"
        elif subquestion_chosen == "TYPE":
            answer = str(var_storage)
            subquestion_string = "idType"
        
        question = f"{code_segment}\n\nGiven the above data segment, what value does {subquestion_string} contain, in decimal?"
        
        return question, answer
    
    # FREE RESPONSE
    def mod7_operators_q4():
        length_chosen = random.randint(4, 8)
        array = []
        # generates random values
        for i in range(length_chosen):
            array.append(random.randint(1, 9999))
                
        array_string = ""
        # converts the array array into a string
        for i in range(0, len(array), ):
            array_string += str(array[i])

            # if it is not the last idx,
            if (i < len(array) - 1):
                # then add a spacing and a comma
                array_string += ", "
        
        # selects a random integer to be used as an idx
        idx_chosen = random.randint(1, length_chosen - 1)
        
        code_segment = ".data" \
            f"\nidArray DWORD {array_string}" \
            f"\nidLength DWORD LENGTHOF idArray" \
            f"\nidSize DWORD SIZEOF idArray" \
            f"\nidType DWORD TYPE idArray" \
            "\n\n.code" \
            "\nmain PROC" \
            "\n; ..." \
            "\nMOV ESI, OFFSET idArray" \
            f"\nMOV EAX, [ESI+{idx_chosen}*TYPE idArray]" \
            "\n; Execution Point A" \
            "\n; ..." \
            "\nexit" \
            "\nmain ENDP"
            
        answer = str(array[idx_chosen])
        
        question = f"{code_segment}\n\nGiven the above data segment, what value does EAX contain at Execution Point A?"
        
        return question, answer
    
    # FREE RESPONSE
    def mod7_stack_frames_q1():
        # creates a list of words between 5-10 characters
        words_to_be_chosen = [
            word for word in WORD_WEBSITE.text.splitlines()
            if len(word) >= 5 and len(word) <= 10
        ]
        
        variable_type_to_be_chosen = [
            "BYTE", "WORD", "DWORD",
        ]
        
        variable_dict = {
            "x": ["", ""],
            "y": ["", ""],
            "z": ["", ""],
        }
        
        answer = 0
        for var in variable_dict:
            variable_chosen = random.choice(variable_type_to_be_chosen)
            
            # if it is *this* variable type,
            if variable_chosen == "BYTE":
                # selects a random word from the word list,
                word_chosen = random.choice(words_to_be_chosen)
                # assigns the variable to its respective value
                variable_dict[var][0] = f"{variable_chosen} '{word_chosen.capitalize()}',0"
                # and expected code,
                variable_dict[var][1] = f"OFFSET {var}"
                
                # and increments the answer to its respective value
                answer += 4
            elif variable_chosen == "WORD":
                variable_dict[var][0] = f"{variable_chosen} {random.randint(10, 99)}"
                variable_dict[var][1] = var
                
                answer += 2
            elif variable_chosen == "DWORD":
                variable_dict[var][0] = f"{variable_chosen} {random.randint(100000, 999999)}"
                variable_dict[var][1] = var
                
                answer += 4
        answer = str(answer)
        
        code_segment = ".data" \
            f"\nx {variable_dict["x"][0]}" \
            f"\ny {variable_dict["y"][0]}" \
            f"\nz {variable_dict["z"][0]}" \
            "\n\n.code" \
            "\nmain PROC" \
            f"\nPUSH {variable_dict["x"][1]}" \
            f"\nPUSH {variable_dict["y"][1]}" \
            f"\nPUSH {variable_dict["z"][1]}" \
            "\nCALL someProcedure" \
            "\nINC EAX" \
            "\nMOV EBX, z" \
            "\nXOR EAX, EBX" \
            "\nexit" \
            "\nmain ENDP"
        
        question = f"{code_segment}\n\nGiven the above data segment, inside someProcedure, what numerical operand should be used with the RET instruction?\n\nNOTE: RET n, what should n be? For example: 10"
        
        return question, answer
    
    # FREE RESPONSE
    def mod7_stack_frames_q2():
        return_value_chosen = random.randint(4, 10)
        answer = str(return_value_chosen + 4)
        
        question = f"The following instruction will increment the stack pointer (ESP) by how many bytes?\n\nRET {return_value_chosen}"
        
        return question, answer
    
    # SELECT THAT APPLY
    def mod8_string_primitives_q2():
        register_chosen = random.choice([
            "ESI", "EDI", "ESI and EDI"
        ])
        
        is_plural = ""
        if register_chosen == "ESI":
            correct_answers = [
                "LODSB",
                "MOVSB",
                "CMPSB",
            ]
            incorrect_answers = [
                "STOSB",
                "SCASB",
            ]
        elif register_chosen == "EDI":
            correct_answers = [
                "CMPSB",
                "MOVSB",
                "SCASB",
                "STOSB",
            ]
            incorrect_answers = [
                "LODSB",
            ]
        # if two registers were chosen, 
        elif register_chosen == "ESI and EDI":
            correct_answers = [
                "CMPSB",
                "MOVSB",
            ]
            incorrect_answers = [
                "LODSB",
                "STOSB",
                "SCASB",
            ]
            
            # then make the question plural
            is_plural = "s"
        
        question = f"Which of the following string primitives will modify the {register_chosen} register{is_plural}?"
        answer = [correct_answers] + [incorrect_answers]
        
        return question, answer
    
    # FREE RESPONSE
    def mod8_macros_vs_procedures_q9():
        byte_chosen = random.randint(1000, 9999)
        used_amount_chosen = random.randint(10, 99)
        macro_req_chosen = random.randint(10, 99)
        proc_req_chosen = random.randint(100, 999)
        proc_call_req_chosen = random.randint(10, 99)
        
        macro_answer = byte_chosen + (used_amount_chosen * macro_req_chosen)
        proc_answer = byte_chosen + proc_req_chosen + (used_amount_chosen * proc_call_req_chosen)
        answer = f"{macro_answer},{proc_answer}"
        
        question = f"Suppose that a program's data and executable code require {byte_chosen} bytes of memory. " \
            f"A new section of code must be added; it will be used with various values {used_amount_chosen} times " \
            f"during the execution of a program. When implemented as a macro, the macro code requires {macro_req_chosen} " \
            f"bytes of memory. When implemented as a procedure, the procedure code requires {proc_req_chosen} bytes " \
            f"(including parameter-passing, etc.), and each procedure call requires {proc_call_req_chosen} bytes. " \
            "\n\nHow many bytes of memory will the entire program require if the new code is added as a macro? as a procedure?" \
            "\n\nNOTE: Type the answer in order separated by a comma (no spaces). " \
            "For example: 1689,4804"
        
        return question, answer
    
    # FREE RESPONSE
    def mod9_infix_vs_postfix_q3():
        subquestion_dict = {
            "postfix": "infix",
            "infix": "postfix",
        }
        # selects a random subquestion;
        # either postfix -> infix or infix -> postfix
        subquestion_chosen = random.choice([
            key for key in subquestion_dict.keys()
        ])
        
        value_type_list = [
            "(", "operand",
        ]
        operator_list = [
            "^", "*", "/", "+", "-"
        ]
        
        postfix_equation_list = []
        is_done_with_equation = False
        # creates the equation
        while True:
            # if the equation list is empty (aka. the first value)
            if len(postfix_equation_list) <= 0:
                value_type_chosen = random.choice(value_type_list)
            # if the equation list > 15,
            elif len(postfix_equation_list) > 15:
                # then the last value should be an operand
                value_type_chosen = "operand"
                # and set to end the while loop
                is_done_with_equation = True
            # if the previous value in the equation list is an operator
            elif postfix_equation_list[-1] in operator_list:
                value_type_chosen = random.choice(value_type_list)
            # if the previous value in the equation list is an operand
            elif postfix_equation_list[-1].isdigit():
                value_type_chosen = "operator"
            
            # if the value type chosen is an open parenthesis,
            if value_type_chosen == "(":
                # then enclose the parentheses
                # with an operand, operator, operand, and operator (in order)
                # for example: (4 + 2) *
                postfix_equation_list.append("(")
                postfix_equation_list.append(str(random.randint(1, 15)))
                postfix_equation_list.append(random.choice(operator_list))
                postfix_equation_list.append(str(random.randint(1, 15)))
                postfix_equation_list.append(")")
                postfix_equation_list.append(random.choice(operator_list))
            elif value_type_chosen == "operand":
                postfix_equation_list.append(str(random.randint(1, 15)))
            elif value_type_chosen == "operator":
                postfix_equation_list.append(random.choice(operator_list))
            
            if is_done_with_equation:
                break
        
        order_of_precedence = {
            "^": 3,
            "*": 2, "/": 2,
            "+": 1, "-": 1,
        }
        
        answer = ""
        infix_equation_list = []
        operative_stack = [] # for tracking order of precendece
        for i in range(len(postfix_equation_list)):
            curr_value = postfix_equation_list[i]
            
            if curr_value.isdigit():
                if subquestion_chosen == "postfix":
                    answer += curr_value
                elif subquestion_chosen == "infix":
                    infix_equation_list.append(curr_value)
            # if the current value is an operator
            else:
                # if the operative stack is empty
                if len(operative_stack) <= 0:
                    operative_stack.append(curr_value)
                else:
                    # if the current value is an open parenthesis
                    if curr_value == "(":
                        operative_stack.append(curr_value)
                    # if the current value is a closed parenthesis,
                    elif curr_value == ")":
                        # then while the open parenthesis exists in the operative stack,
                        while "(" in operative_stack:
                            # pop the operative stack until the open parenthesis is encountered
                            removed_value = operative_stack.pop()
                            
                            # and add the removed value to the answer (excluding the open parenthesis)
                            if removed_value != "(":
                                if subquestion_chosen == "postfix":
                                    answer += removed_value
                                elif subquestion_chosen == "infix":
                                    infix_equation_list.append(removed_value)
                    else:
                        # if the previous value in the operative stack is an open parenthesis
                        if operative_stack[-1] == "(":
                            operative_stack.append(curr_value)
                        else:
                            # while the previous value in the operative stack is >= the current value
                            # (order of precendence determined via the dictionary above)
                            while (order_of_precedence[operative_stack[-1]] >= order_of_precedence[curr_value]
                                    and len(operative_stack) > 0):
                                removed_value = operative_stack.pop()
                                
                                if subquestion_chosen == "postfix":
                                    # pop the operative stack into the answer
                                    answer += removed_value
                                elif subquestion_chosen == "infix":
                                    infix_equation_list.append(removed_value)
                                
                                if len(operative_stack) <= 0:
                                    break
                            
                            # once the current value is greater than the previous value in the operative stack,
                            # add the current value to the operative stack
                            operative_stack.append(curr_value)

        # if there are still operators remaining in the operative stack,
        while len(operative_stack) > 0:
            removed_value = operative_stack.pop()
            
            if subquestion_chosen == "postfix":
                # add the entire stack to the answer
                answer += removed_value
            elif subquestion_chosen == "infix":
                infix_equation_list.append(removed_value)
        
        if subquestion_chosen == "postfix":
            equation_string = " ".join(postfix_equation_list)
        elif subquestion_chosen == "infix":
            equation_string = " ".join(infix_equation_list)
            answer = "".join(postfix_equation_list)
        
        question = f"Convert the following {subquestion_dict[subquestion_chosen]} expression to {subquestion_chosen}." \
            f"\n\n{equation_string}" \
            "\n\nNOTE: Do not include spaces. For example: 1242-*411+^/+"
        
        return question, answer
    
    # FREE RESPONSE
    def mod9_infix_vs_postfix_q4():
        value_type_list = [
            "(", "operand",
        ]
        operator_list = [
            "*", "/", "+", "-"
        ]
        
        postfix_equation_list = []
        is_done_with_equation = False
        # creates the equation
        while True:
            # if the equation list is empty (aka. the first value)
            if len(postfix_equation_list) <= 0:
                value_type_chosen = random.choice(value_type_list)
            # if the equation list > 15,
            elif len(postfix_equation_list) > 15:
                # then the last value should be an operand
                value_type_chosen = "operand"
                # and set to end the while loop
                is_done_with_equation = True
            # if the previous value in the equation list is an operator
            elif postfix_equation_list[-1] in operator_list:
                value_type_chosen = random.choice(value_type_list)
            # if the previous value in the equation list is an operand
            elif postfix_equation_list[-1].isdigit():
                value_type_chosen = "operator"
            
            # if the value type chosen is an open parenthesis,
            if value_type_chosen == "(":
                # then enclose the parentheses
                # with an operand, operator, operand, and operator (in order)
                # for example: (4 + 2) *
                postfix_equation_list.append("(")
                postfix_equation_list.append(str(random.randint(1, 9)))
                postfix_equation_list.append(random.choice(operator_list))
                postfix_equation_list.append(str(random.randint(1, 9)))
                postfix_equation_list.append(")")
                postfix_equation_list.append(random.choice(operator_list))
            elif value_type_chosen == "operand":
                postfix_equation_list.append(str(random.randint(1, 9)))
            elif value_type_chosen == "operator":
                postfix_equation_list.append(random.choice(operator_list))
            
            if is_done_with_equation:
                break
        
        order_of_precedence = {
            "*": 2, "/": 2,
            "+": 1, "-": 1,
        }
        
        infix_equation_list = []
        operative_stack = [] # for tracking order of precendece
        for i in range(len(postfix_equation_list)):
            curr_value = postfix_equation_list[i]
            
            if curr_value.isdigit():
                infix_equation_list.append(curr_value)
            # if the current value is an operator
            else:
                # if the operative stack is empty
                if len(operative_stack) <= 0:
                    operative_stack.append(curr_value)
                else:
                    # if the current value is an open parenthesis
                    if curr_value == "(":
                        operative_stack.append(curr_value)
                    # if the current value is a closed parenthesis,
                    elif curr_value == ")":
                        # then while the open parenthesis exists in the operative stack,
                        while "(" in operative_stack:
                            # pop the operative stack until the open parenthesis is encountered
                            removed_value = operative_stack.pop()
                            
                            # and add the removed value to the answer (excluding the open parenthesis)
                            if removed_value != "(":
                                infix_equation_list.append(removed_value)
                    else:
                        # if the previous value in the operative stack is an open parenthesis
                        if operative_stack[-1] == "(":
                            operative_stack.append(curr_value)
                        else:
                            # while the previous value in the operative stack is >= the current value
                            # (order of precendence determined via the dictionary above)
                            while (order_of_precedence[operative_stack[-1]] >= order_of_precedence[curr_value]
                                    and len(operative_stack) > 0):
                                infix_equation_list.append(operative_stack.pop())
                                
                                if len(operative_stack) <= 0:
                                    break
                            
                            # once the current value is greater than the previous value in the operative stack,
                            # add the current value to the operative stack
                            operative_stack.append(curr_value)

        # if there are still operators remaining in the operative stack,
        while len(operative_stack) > 0:
            infix_equation_list.append(operative_stack.pop())
        
        postfix_stack = []
        for i in range(len(infix_equation_list)):
            curr_value = infix_equation_list[i]
            
            if curr_value.isdigit():
                postfix_stack.append(curr_value)
            # if the current value is an operator
            else:
                left_value = float(postfix_stack[-2])
                right_value = float(postfix_stack.pop())
                
                if curr_value == "+":
                    result = left_value + right_value
                elif curr_value == "-":
                    result = left_value - right_value
                elif curr_value == "*":
                    result = left_value * right_value
                elif curr_value == "/":
                    result = left_value / right_value
                
                # reassign the left value in the postfix stack
                # with the current result
                postfix_stack[-1] = result
        
        answer = str(round(float(postfix_stack[0]), 1)) # round to nearest tenth
        equation_string = " ".join(infix_equation_list)
        
        question = f"Find the decimal value of the postfix expression." \
            f"\n\n{equation_string}" \
            "\n\nNOTE: Round answer to one decimal place. For example: 13.0"
        
        return question, answer
    
    # FREE RESPONSE
    def mod9_infix_vs_postfix_q7():
        value_type_list = [
            "(", "operand",
        ]
        operator_list = [
            "*", "/", "+", "-"
        ]
        letter_list = [
            "A", "B", "C", "D", "E",
            "F", "G", "H", "I", "J",
        ]
        
        postfix_equation_list = []
        is_done_with_equation = False
        # creates the equation
        while True:
            # if the equation list is empty (aka. the first value)
            if len(postfix_equation_list) <= 0:
                value_type_chosen = random.choice(value_type_list)
            # if the equation list > 10,
            elif len(postfix_equation_list) > 10:
                # then the last value should be an operand
                value_type_chosen = "operand"
                # and set to end the while loop
                is_done_with_equation = True
            # if the previous value in the equation list is an operator
            elif postfix_equation_list[-1] in operator_list:
                value_type_chosen = random.choice(value_type_list)
            # if the previous value in the equation list is an operand
            elif postfix_equation_list[-1].isalpha():
                value_type_chosen = "operator"
            
            # if the value type chosen is an open parenthesis,
            if value_type_chosen == "(":
                # then enclose the parentheses
                # with an operand, operator, operand, and operator (in order)
                # for example: (A + B) *
                postfix_equation_list.append("(")
                postfix_equation_list.append(letter_list.pop(0))
                postfix_equation_list.append(random.choice(operator_list))
                postfix_equation_list.append(letter_list.pop(0))
                postfix_equation_list.append(")")
                postfix_equation_list.append(random.choice(operator_list))
            elif value_type_chosen == "operand":
                postfix_equation_list.append(letter_list.pop(0))
            elif value_type_chosen == "operator":
                postfix_equation_list.append(random.choice(operator_list))

            if is_done_with_equation:
                break
        
        order_of_precedence = {
            "*": 2, "/": 2,
            "+": 1, "-": 1,
        }
        
        infix_equation_list = []
        operative_stack = [] # for tracking order of precendece
        for i in range(len(postfix_equation_list)):
            curr_value = postfix_equation_list[i]
            
            if curr_value.isalpha():
                infix_equation_list.append(curr_value)
            # if the current value is an operator
            else:
                # if the operative stack is empty
                if len(operative_stack) <= 0:
                    operative_stack.append(curr_value)
                else:
                    # if the current value is an open parenthesis
                    if curr_value == "(":
                        operative_stack.append(curr_value)
                    # if the current value is a closed parenthesis,
                    elif curr_value == ")":
                        # then while the open parenthesis exists in the operative stack,
                        while "(" in operative_stack:
                            # pop the operative stack until the open parenthesis is encountered
                            removed_value = operative_stack.pop()
                            
                            # and add the removed value to the answer (excluding the open parenthesis)
                            if removed_value != "(":
                                infix_equation_list.append(removed_value)
                    else:
                        # if the previous value in the operative stack is an open parenthesis
                        if operative_stack[-1] == "(":
                            operative_stack.append(curr_value)
                        else:
                            # while the previous value in the operative stack is >= the current value
                            # (order of precendence determined via the dictionary above)
                            while (order_of_precedence[operative_stack[-1]] >= order_of_precedence[curr_value]
                                    and len(operative_stack) > 0):
                                infix_equation_list.append(operative_stack.pop())
                                
                                if len(operative_stack) <= 0:
                                    break
                            
                            # once the current value is greater than the previous value in the operative stack,
                            # add the current value to the operative stack
                            operative_stack.append(curr_value)

        # if there are still operators remaining in the operative stack,
        while len(operative_stack) > 0:
            infix_equation_list.append(operative_stack.pop())
        
        infix_equation_into_code = ""
        postfix_stack = []
        for i in range(len(infix_equation_list)):
            curr_value = infix_equation_list[i]
            
            if curr_value.isalpha():
                infix_equation_into_code += f"\nFLD {curr_value}"
                postfix_stack.append(curr_value)
            # if the current value is an operator
            else:
                left_value = postfix_stack[-2]
                right_value = postfix_stack.pop()
                
                if curr_value == "+":
                    infix_equation_into_code += f"\nFADD"
                    result = f"{left_value}+{right_value}"
                elif curr_value == "-":
                    infix_equation_into_code += f"\nFSUB"
                    result = f"{left_value}-{right_value}"
                elif curr_value == "*":
                    infix_equation_into_code += f"\nFMUL"
                    result = f"{left_value}*{right_value}"
                elif curr_value == "/":
                    infix_equation_into_code += f"\nFDIV"
                    result = f"{left_value}/{right_value}"
                
                # reassign the left value in the postfix stack
                # as a closed parenthese equation
                postfix_stack[-1] = f"({result})"
        
        code_segment = "FINIT" \
            f"{infix_equation_into_code}" \
            "\nFSTP Z"
            
        answer = f"Z={postfix_stack[0]}"
        
        question = f"{code_segment}\n\nGiven the above MASM code, " \
            f"what is the expected output?" \
            "\n\nNOTE: Do not include spaces. For example: Z=A+(B-C)/(D*E)"
        
        return question, answer
    