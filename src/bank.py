from question import Question

MULTIPLE_CHOICE = "multiple choice"
TRUE_OR_FALSE = "true or false"
FREE_RESPONSE = "free response"
SELECT_THAT_APPLY = "select that apply"
MATCH_TO_ANSWER = "match to answer"
MATCH_TO_ANSWER_RANDOMIZED = "match to answer randomized"

class Bank():
    """
    Modifies questions from the question bank.
    """
    
    def get_variant_question(question_variant: str,
                             question_chosen: str) -> str:
        """
        Creates questions with different variations
        (ex. How many bits are there in _?)
        """
        
        return question_variant.replace("_", question_chosen)    

# TODO: sort question bank

question_bank = {
    "Module 1": {
        "Language Hierarchy": {
            "Q1": {
                "details": {
                    "Match the Language Hierarchy to its order.": [
                        ["Level 4", "Natural Languages"],
                        ["Level 3", "High- or Low-level Programming Languages"],
                        ["Level 2", "Assembly Languages"],
                        ["Level 1", "Machine Language"],
                        ["Level 0", "Computer hardware"],
                    ]
                },
                "format": MATCH_TO_ANSWER,
            },
            "Q2": {
                "details": {
                    "Assembly Language instructions have a nearly _ correspondence with Machine Code.": "One-to-one",
                    "rpt1": "One-to-Many",
                    "rpt2": "Many-to-One",
                    "rpt3": "Many-to-Many",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q3": {
                "details": {
                    "Assembly Language (x86, RISC-V, …)": "False",
                    "assembler (MASM, NASM, FASM, …)": "True",
                },
                "variant": "A single computer architecture may have programs written for it using more than one _.",
                "format": TRUE_OR_FALSE,
            },
            "Q4": {
                "details": {
                    "High-level language (HLL)": "True",
                    "Assembly Language": "False",
                },
                "variant": "_ programs are portable to a variety of computer architectures.",
                "format": TRUE_OR_FALSE,
            },
            "Q5": {
                "details": {
                    "A program is considered portable if it _.": "can be executed on multiple platforms",
                    "rpt1": "can be quickly copied from conventional RAM into high-speed RAM",
                    "rpt2": "can be rewritten in a different programming language without losing its meaning",
                    "rpt3": "can be tightly coupled to one specific platform",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q6": {
                "details": {
                    "An Assembly Language is defined by the _": "Instruction Set Architecture (ISA)",
                    "rpt1": "Assembler (e.g. MASM)",
                    "rpt2": "Language Hierarchy Level",
                    "rpt3": "User",
                },
                "format": MULTIPLE_CHOICE,
            },
			"Q7": {
                "details": {
                    "Match the definition to its step in preparing and running an assembly language.": [
                        ["Assemble", "Converts assembly language to machine code"],
                        ["Link", "Merges multiple object files and libraries into a single executable"],
                        ["Load", "Loads the executable into memory"],
                        ["Compile", "Translates high-level source code into machine code"],
                    ]
                },
                "format": MATCH_TO_ANSWER,
            },
            "Q8": {
                "details": {
                    "What type of tool can convert ARM Assembly to x86 Assembly?": "Cross Assembler",
                    "rpt1": "Loader",
                    "rpt2": "Linker",
                    "rpt3": "Cross Compiler",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q9": {
                "details": {
                    "Compared to higher-level languages, which of the following are benefits of Assembly Language programming?": [
                        [
                            "Hands-on Code Optimization",
                            "Direct Manipulation of Memory",
                        ],
                        [
                            "Intuitive Programs",
                            "Integrated Tools",
                            "Ease of Use",
                        ]
                    ]
                },
                "format": SELECT_THAT_APPLY,
            },
        },
        "Instruction Set Architecture": {
            "Q1": {
                "details": {
                    "Match the definition to its instruction set architecture (ISA).": [
                        ["Register", "A data storage location"],
                        ["Instruction", "A 'control phase' for a computer"],
                        ["Operands", "An input or output value for the 'control phase'"],
                    ]
                },
                "format": MATCH_TO_ANSWER,
            },
        },
        "Data Representation": {
            "Q1": {
                "details": None,
                "variant": Question.mod1_data_representation_q1,
                "format": TRUE_OR_FALSE,
            },
            "Q2": {
                "details": None,
                "variant": Question.mod1_data_representation_q2,
                "format": TRUE_OR_FALSE,
            },
        },
        "Data Arithmetics": {
            "Q1": {
                "details": None,
                "variant": Question.mod1_data_arithmetics_q1,
                "format": FREE_RESPONSE,
            },
        },
        "Numerical Data Types": {
            "Q1": {
                "details": {
                    "BYTE": "0 to 2^(8)-1",
                    "SBYTE": "-2^(7) to 2^(7)-1",
                    "WORD": "0 to 2^(16)-1",
                    "SWORD": "-2^(15) to 2^(15)-1",
                    "DWORD": "0 to 2^(32)-1",
                    "SDWORD": "-2^(31) to 2^(31)-1",
                    "QWORD": "0 to 2^(64)-1",
                    "SQWORD": "-2^(63) to 2^(63)-1",
                    "OWORD": "0 to 2^(128)-1",
                    "SOWORD": "-2^(127) to 2^(127)-1",
                },
                "variant": "What are the smallest and largest values which can be represented with a _",
                "format": MULTIPLE_CHOICE,
            },
            "Q2": {
                "details": {
                    "BYTE": "8",
                    "SBYTE": "8",
                    "WORD": "16",
                    "SWORD": "16",
                    "DWORD": "32",
                    "SDWORD": "32",
                    "QWORD": "64",
                    "SQWORD": "64",
                    "OWORD": "128",
                    "SOWORD": "128",
                    "REAL4": "32",
                    "REAL8": "64",
                    "REAL10": "80",
                },
                "variant": "How many bits long is a(n) _ on x86 systems?",
                "format": FREE_RESPONSE,
            },
            "Q3": {
                "details": {
                    "BYTE": "1",
                    "SBYTE": "1",
                    "WORD": "2",
                    "SWORD": "2",
                    "DWORD": "4",
                    "SDWORD": "4",
                    "QWORD": "8",
                    "SQWORD": "8",
                    "OWORD": "16",
                    "SOWORD": "16",
                    "REAL4": "4",
                    "REAL8": "8",
                    "REAL10": "10",
                },
                "variant": "How many bytes long is a(n) _ on x86 systems?",
                "format": FREE_RESPONSE,
            },
            "Q4": {
                "details": {
                    "24": "16,777,215",
                    "20": "65,536",
                    "16": "32,767",
                    "12": "1,738",
                },
                "variant": "What is the largest unsigned integer that may be stored in _ bits?",
                "format": MULTIPLE_CHOICE,
            },
        },
        "Large Value Prefixes": {
            "Q1": {
                "details": {
                    "kilo (Ki)": "2^10",
                    "mega (Mi)": "2^20",
                    "giga (Gi)": "2^30",
                    "tera (Ti)": "2^40",
                    "peta (Pi)": "2^50",
                    "exa (Ei)": "2^60",
                    "zetta (Zi)": "2^70",
                    "yotta (Yi)": "2^80",
                },
                "variant": "What is the multiplier for _?\n\nNOTE: Use caret (^) to represent as power. For example: 2^5 will be read as '2 to the power of 5'.",
                "format": FREE_RESPONSE,
            },
            "Q2": {
                "details": None,
                "variant": Question.mod1_large_value_prefixes_q2,
                "format": FREE_RESPONSE,
            },
        },
        "Character Data Type": {
            "Q1": {
                "details": None,
                "variant": Question.mod1_character_data_type_q1,
                "format": FREE_RESPONSE,
            },
            "Q2": {
                "details": {
                    "smaller": "False",
                    "larger": "True",
                },
                "variant": "The ASCII code values for alphabetic letters are _ than decimal digits.",
                "format": TRUE_OR_FALSE,
            },
        },
        "Central Processing Unit": {
            "Q1": {
                "details": {
                    "Match the definition to its central processing unit (CPU).": [
                        ["System Clock", "A metronome for a computer"],
                        ["Register", "A container for data"],
                        ["Bus", "A pipeline for the transfer of data within a computer"],
                        ["Arithmetic/Logic Unit (ALU)", "Computes basic operations (such as addition, subtraction, and logical operators)"],
                        ["Control Unit", "Manages the flow of execution for programs"],
                        ["Memory I/O", "Reads/write information in main memory"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
            "Q2": {
                "details": {
                    "Match the definition to its bus.": [
                        ["Address Bus", "Transfers memory addresses from the CPU and out to memory (or other components)"],
                        ["Data Bus", "Transfers data between the CPU and RAM"],
                        ["Control Bus", "Uses signals to coordinate actions between different components"],
                        ["Input/Output (I/O) Bus", "Transfers data between the CPU and attached onboard or peripheral devices"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
            "Q3": {
                "details": {
                    "Match the definition to its control unit (CU).": [
                        ["Instruction Pointer (IP)", "Holds the memory address of the next instruction to be executed by the CPU"],
                        ["Instruction Register (IR)", "Holds the instruction currently being executed or decoded"],
                        ["Instruction Decoder", "Decodes the current instruction"],
                        ["Control Register", "Coordinates the execution of the instruction"],
                        ["Status Register", "Stores information about the current state of the processor or device"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
            "Q4": {
                "details": None,
                "variant": Question.mod1_central_processing_unit_q4,
                "format": SELECT_THAT_APPLY,
            },
            "Q5": {
                "details": {
                    "Match the definition to its memory I/O.": [
                        ["Memory Address Register (MAR)", "Holds the memory address of the data that the CPU is about to either fetch from or store to RAM"],
                        ["Memory Data Register (MDR)", "Holds data being transferred to or from the computer's RAM"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
            "Q6": {
                "details": {
                    "Caching refers to moving information from slower storage to faster storage.": "True",
                },
                "format": TRUE_OR_FALSE,
            },
            "Q7": {
                "details": {
                    "Which is the largest memory that resides on the actual CPU": "L1",
                    "rpt1": "L2",
                    "rpt2": "L3",
                    "rpt3": "L4",
                },
                "format": MULTIPLE_CHOICE,
            },
			"Q8": {
                "details": {
                    "What is the width of the address and data buses?": "32 bits",
                    "rpt1": "16 bits",
                    "rpt2": "32 bytes",
                    "rpt3": "16 bytes",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q9": {
                "details": {
                    "A primary limitation on the speed of internal communication on a machine is the width of the internal bus.": "True",
                },
                "format": TRUE_OR_FALSE,
            },
            "Q10": {
                "details": {
                    "The CPU clock cycle length is the only contributing factor to the speed of operations on a computer.": "False",
                },
                "format": TRUE_OR_FALSE,
            },
        },
        "Main Memory": {
            "Q1": {
                "details": {
                    "In a specific architecture, created by _, programs are stored in memory and executed according to an instruction execution cycle.": "John von Neumann",
                    "rpt1": "David Hilbert",
                    "rpt2": "Kurt Gödel",
                    "rpt3": "Albert Einstein",
                    "rpt4": "Leo Szilard",
                    "rpt5": "John G. Kemeny",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q2": {
                "details": {
                    "One major bottleneck is the data bus, because both the program instructions and the data must be retrieved from the same memory to be executed or used. A way to resolve this issue is _.": "Caching",
                    "rpt1": "Reloading",
                    "rpt2": "Stablizing",
                    "rpt3": "Terminating",
                },
                "format": MULTIPLE_CHOICE,
            },
        },
        "Instruction Execution Cycle": {
            "Q1": {
                "details": {
                    "Place the following steps of the instruction execution cycle into the correct order.": [
                        ["Step 1", "Fetch the instruction at the address in the IP into the IR"],
                        ["Step 2", "Increment the IP"],
                        ["Step 3", "Decode the instruction"],
                        ["Step 4", "If the instruction requires memory access, use a 'read' operation"],
                        ["Step 5", "Execute the instruction in the ALU and store the resultant operands"],
                        ["Step 6", "If the instruction requires memory access, use a 'write' operation"],
                        ["Step 7", "Set status register"],
                    ]
                },
                "format": MATCH_TO_ANSWER,
            },
            "Q2": {
                "details": {
                    "Place the following steps for a 'memory read' into the correct order.": [
                        ["Step 1", "Data is from the register copied into the ALU"],
                        ["Step 2", "The memory address is put into the MAR"],
                        ["Step 3", "The memory address is put on the address bus"],
                        ["Step 4", "Assert a 'memory read'"],
                        ["Step 5", "Data is copied from that particular memory cell and put on the data bus"],
                        ["Step 6", "Data is put into the MDR"],
                        ["Step 7", "Data is copied from the MDR into the ALU"],
                    ]
                },
                "format": MATCH_TO_ANSWER,
            },
        },
        "IA-32 Architecture": {
            "Q1": {
                "details": {
                    "Match the definition to its IA-32 architecture.": [
                        ["16-bit Segment Registers", "Hold specific segments of memory"],
                        ["32-bit General Purpose Registers", "Hold data and memory addresses"],
                        ["32-bit Instruction Pointer Registers (EIP)", "Hold the memory address of the next instruction to be fetched"],
                        ["32-bit Program Status and Control Registers (EFLAGS)", "Control the status of the processor"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
        },
		"Memory Management": {
            "Q1": {
                "details": {
                    "How much memory can be addressed in Real-address mode?": "1 MB",
                    "rpt1": "16 MB",
                    "rpt2": "640 K",
                    "rpt3": "4 GB",
                },
                "format": MULTIPLE_CHOICE,
            },
        },
		"Modes of Operation": {
            "Q1": {
                "details": {
                    "Which Operation Mode provides compatibility for legacy 8086 programs?": "Real-Address Mode",
                    "rpt1": "System Management Mode",
                    "rpt2": "32-bit Protected Mode",
                    "rpt3": "Legacy Mode",
                },
                "format": MULTIPLE_CHOICE,
            },
        },
        "Registers: Special Purposes": {
            "Q1": {
                "details": {
                    "Match the definition to its register.": [
                        ["EAX", "Computes ALU operations that are stored in the lower 32-bits"],
                        ["EBX", "Acts as a general storage of values, pointers, arithmetic operands, etc."],
                        ["EDX", "Computes ALU operations that are stored in the upper 32-bits"],
                        ["ECX", "Acts as a counter"],
                        ["ESI", "Holds the address of the memory location to be to be read"],
                        ["EDI", "Holds the address of the memory location to be to be overwritten"],
                        ["ESP", "Points to the top of the stack addresses"],
                        ["EBP", "Points to the bottom of the stack addresses"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
        },
        "Sub-registers: Access Method": {
            "Q1": {
                "details": None,
                "variant": Question.mod1_sub_register_access_method_q1,
                "format": SELECT_THAT_APPLY,
            },
        },
        "Status Flags": {
            "Q1": {
                "details": {
                    "Set indicates a bit value of _, and cleared indicates a bit value of _.": "1, 0",
                    "rpt1": "0, 1",
                    "rpt2": "1, 1",
                    "rpt3": "0, 0",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q2": {
                "details": {
                    "Match the definition to its status flag.": [
                        ["Auxiliary Carry", "Sets if arithmetic operation generates a carry or a borrow out of bit 3 of the result"],
                        ["Carry", "Sets if an unsigned arithmetic operation generates a carry or a borrow out of the most-significant bit of the result"],
                        ["Direction", "Sets the direction ESI or EDI are stepped when executing string processing instructions"],
                        ["Interrupt Enable", "Sets if hardware-generated interrupts will be issued"],
                        ["Overflow", "Sets if the result of a signed arithmetic operation is too large or too small"],
                        ["Parity", "Sets if the least-significant byte of the result contains an even number of 1 bits"],
                        ["Sign", "Sets if an arithmetic operation generates a negative result"],
                        ["Zero", "Sets if the result is zero"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
            "Q3": {
                "details": {
                    "Match the abbreviation to its status flag.": [
                        ["Auxiliary Carry", "AF/AC"],
                        ["Carry", "CF/CY"],
                        ["Direction", "UP"],
                        ["Interrupt Enable", "EI"],
                        ["Overflow", "OF/OV"],
                        ["Parity", "PF/PE"],
                        ["Sign", "SF/PL"],
                        ["Zero", "ZF/ZR"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
            "Q4": {
                "details": {
                    "In unsigned arithmetic, watch the carry flag to detect errors; the overflow flag tells you nothing interesting": "True",
                    "In signed arithmetic, watch the overflow flag to detect errors; the carry flag tells you nothing interesting": "True",
                    "In unsigned arithmetic, watch the overflow flag to detect errors; the carry flag tells you nothing interesting": "False",
                    "In signed arithmetic, watch the carry flag to detect errors; the overflow flag tells you nothing interesting": "False",
                },
                "format": TRUE_OR_FALSE,
            },
        }, 
        "Segment Registers": {
            "Q1": {
                "details": {
                    "Match the definition to its register.": [
                        ["CS", "Points to the program currently being executed"],
                        ["DS", "Points to the location where data is stored"],
                        ["ES/FS/GS", "Points to additional segments for data storage"],
                        ["SS", "Points to the read/write data"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
        },
    },
    "Module 2": {
        "Directives": {
            "Q1": {
                "details": {
                    "Match the definition to its directive.": [
                        [".data", "Marks beginning of the data segment"],
                        [".code", "Marks beginning of the code segment"],
                        [".stack", "Specifies the size of the runtime stack"],
                        ["INCLUDE", "Inserts source code from specified file"],
                        ["PROC", "Defines the start of a procedure"],
                        ["ENDP", "Defines the end of a procedure"],
                        ["MACRO", "Defines the start of a macro"],
                        ["ENDM", "Defines the end of a macro"],
                        ["END", "Marks the end of module"],
                        ["INVOKE", "Calls a procedure at address given by the expression"],
                        ["BYTE, WORD, DWORD, etc.", "Allocates memory space for 'variable' storage"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
            "Q2": {
                "details": {
                    "What does the END directive do?": [
                        [
                            "Sets the entry point (procedure) for the program",
                            "Marks the end of the module",
                            
                        ],
                        [
                            "Exits to the operating system",
                            "Terminates a loop",
                        ]
                    ]
                },
                "format": SELECT_THAT_APPLY,
            },
        },
        "Identifiers": {
            "Q1": {
                "details": None,
                "variant": Question.mod2_identifiers_q1,
                "format": SELECT_THAT_APPLY,
            },
            "Q2": {
                "details": {
                    "MASM is case-sensitive.": "False"
                },
                "format": TRUE_OR_FALSE,
            },
        },
        "Memory Addresses": {
            "Q1": {
                "details": {
                    "Groups of bytes in memory can only be interpreted a single way.": "False",
                },
                "format": TRUE_OR_FALSE,
            },
            "Q2": {
                "details": None,
                "variant": Question.mod2_memory_addresses_q2,
                "format": FREE_RESPONSE,
            },
        },
        "Composition of an Instruction": {
            "Q1": {
                "details": {
                    "Which is the correct composition of an instruction?": "[code_label:] mnemonic [operands] [;comment]",
                    "rpt1": "[mnemonic:] code_label [operands] [;comment]",
                    "rpt2": "[code_label:] operands [mnemonic] [;comment]",
                    "rpt3": "[comment:] mnemonic [operands] [;code_label]",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q2": {
                "details": {
                    "All instructions have operands.": "False",
                },
                "format": TRUE_OR_FALSE,
            },
            "Q3": {
                "details": {
                    "By default, code labels are visible only within the procedure in which they are assigned (created).": "True"
                },
                "format": TRUE_OR_FALSE,
            },
            "Q4": {
                "details": {
                    "In MASM all text following a semicolon (on the same line) is treated as a comment and ignored when the program is converted to machine code.": "True"
                },
                "format": TRUE_OR_FALSE,
            },
            "Q5": {
                "details": None,
                "variant": Question.mod2_composition_of_an_instruction_q5,
                "format": SELECT_THAT_APPLY,
            },
            "Q6": {
                "details": {
                    "ADD": "True",
                    "MUL": "False",
                },
                "variant": "The _ instruction must have an explicit destination operand",
                "format": TRUE_OR_FALSE,
            },
            "Q7": {
                "details": {
                    "Operands may be any of the following.": [
                        [
                            "register name",
                            "variable name (memory)",
                            "constant or constant expression"
                            
                        ],
                        [
                            "non-register reserved word",
                        ]
                    ]
                },
                "format": SELECT_THAT_APPLY,
            },
            "Q8": {
                "details": {
                    "Code labels may only appear on lines with no instructions.": "False"
                },
                "format": TRUE_OR_FALSE,
            },
        },
        "Instruction Mnemonics": {
            "Q1": {
                "details": {
                    "ADD": "True",
                    "SUB": "True",
                    "MOV": "True",
                    "JMP": "True",
                    "CLD": "True",
                },
                "variant": "_ is an example of an instruction mnemonic.",
                "format": TRUE_OR_FALSE,
            },
            "Q2": {
                "details": {
                    "Match the definition to its instruction mnemonic.": [
                        ["ADD", "Adds two values"],
                        ["SUB", "Subtracts one value from another"],
                        ["MOV", "Copies a value to another location"],
                        ["JMP", "Transfers program execution to a different memory address signified by a code label"],
                        ["CLD", "Clears the Direction Flag"],
                        ["CMP", "Compares two values"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
            "Q3": {
                "details": None,
                "variant": Question.mod2_instruction_mnemonics_q3,
                "format": FREE_RESPONSE,
            },
            "Q4": {
                "details": {
                    "eax = -dword1 + (edx - ecx) + 1": "mov eax,dword1\
                                                        neg eax\
                                                        mov ebx,edx\
                                                        sub ebx,ecx\
                                                        add eax,ebx\
                                                        inc eax",
                    "eax = dword1 + (edx - ecx) + 1": "mov eax,dword1\
                                                        mov ebx,edx\
                                                        sub ebx,ecx\
                                                        add eax,ebx\
                                                        inc eax",
                    "eax = -dword1 + (edx + ecx) + 1": "mov eax,dword1\
                                                        neg eax\
                                                        mov ebx,edx\
                                                        add ebx,ecx\
                                                        add eax,ebx\
                                                        inc eax",
                    "eax = dword1 + (edx + ecx) + 1": "mov eax,dword1\
                                                        mov ebx,edx\
                                                        add ebx,ecx\
                                                        add eax,ebx\
                                                        inc eax",
                },
                "variant": "Select the answer choice that best implements the following expression. Do not permit dword1, ECX, or EDX to be modified.\n\n_",
                "format": MULTIPLE_CHOICE,
            },
            "Q5": {
                "details": None,
                "variant": Question.mod2_instruction_mnemonics_q5,
                "format": FREE_RESPONSE,
            },
            "Q6": {
                "details": None,
                "variant": Question.mod2_instruction_mnemonics_q6,
                "format": FREE_RESPONSE,
            },
        },
        "Irvine Procedures": {
            "Q1": {
                "details": {
                    "Match the definition to its Irvine procedures.": [
                        ["ClrScr", "Clears the console window"],
                        ["CrLf", "Sets cursor to new line"],
                        ["ReadInt", "Reads a signed integer from keyboard"],
                        ["ReadDec", "Reads an unsigned integer from keyboard"],
                        ["ReadString", "Reads a string from keyboard"],
                        ["ReadChar", "Reads a single character from keyboard"],
                        ["WriteInt", "Writes a signed integer to the console window"],
                        ["WriteDec", "Writes an unsigned integer to the console window"],
                        ["WriteString", "Writes a string to the console window"],
                        ["WriteChar", "Writes a single ASCII character to the console window"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
        },
    },
    "Module 3": {
        "Instruction Mnemonics": {
            "Q1": {
                "details": {
                    "Match the definition to its instruction mnemonic.": [
                        ["INC", "Increments the value by one"],
                        ["DEC", "Decrements the value by one"],
                        ["LOOP", "Decrements ECX and repeats the code label until ECX is equal to zero"],
                        ["CALL", "Pushes the instruction pointer on the system stack and jumps to the beginning of the named procedure"],
                        ["RET", "Pops the top of the system stack (containing the return address) into the instruction pointer"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
        },
        "Jumps": {
            "Q1": {
                "details": None,
                "variant": Question.mod3_jumps_q1,
                "format": TRUE_OR_FALSE,
            },
            "Q2": {
                "details": {
                    "Match the definition to its Jcond instruction.": [
                        ["JCXZ", "jumps if CX = 0"],
                        ["JECXZ", "jumps if ECX = 0"],
                        ["JC", "jumps if CF = 1"],
                        ["JNC", "jumps if CF = 0"],
                        ["JO", "jumps if OF = 1"],
                        ["JNO", "jumps if OF = 0"],
                        ["JP", "jumps if PF = 1"],
                        ["JNP", "jumps if PF = 0"],
                        ["JS", "jumps if SF = 1"],
                        ["JNS", "jumps if SF = 0"],
                        ["JZ", "jumps if ZF = 1"],
                        ["JNZ", "jumps if ZF = 0"],
                        ["JGE", "jumps if op1 >= op2"],
                        ["JG", "jumps if op1 > op2"],
                        ["JLE", "jumps if op1 <= op2"],
                        ["JL", "jumps if op1 < op2"],
                        ["JAE", "jumps if op1 is above or equal to op2"],
                        ["JA", "jumps if op1 is above op2"],
                        ["JBE", "jumps if op1 is below or equal to op2"],
                        ["JB", "jumps if op1 is below op2"],
                        ["JE", "jumps if op1 equals to op2"],
                        ["JNE", "jumps if op1 is not equal to op2"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
            "Q3": {
                "details": {
                    "When branching in MASM, you will normally jump to a(n) _.": "code label",
                    "rpt1": "instruction pointer (EIP)",
                    "rpt2": "stack label",
                    "rpt3": "data label",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q4": {
                "details": {
                    "When implementing a conditional branch, the comparison is performed in the _ and the results are checkable by viewing individual bits in the _.": "arithmetic/logic unit (ALU), status register (EFLAGS)",
                    "rpt1": "status register (EFLAGS), arithmetic/logic unit (ALU)",
                    "rpt2": "floating point unit (FPU), status register (EFLAGS)",
                    "rpt3": "status register (EFLAGS), floating point unit (FPU)",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q5": {
                "details": None,
                "variant": Question.mod3_jumps_q5,
                "format": FREE_RESPONSE,
            },
        },
        "Loops": {
            "Q1": {
                "details": None,
                "variant": Question.mod3_loops_q1,
                "format": TRUE_OR_FALSE,
            },
            "Q2": {
                "details": {
                    "The jump destination associated with LOOP must be within _ bytes.": "[-128,+127]",
                    "rpt1": "[-255,+255]",
                    "rpt2": "[-inf,+inf]",
                    "rpt3": "user-defined",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q3": {
                "details": {
                    "When using the LOOP instruction, one should be wary of which common issues?": [
                        [
                            "Overwriting ECX's original value in a nested loop body without preserving its outer loop counter value",
                            "Modifying ECX directly within the loop body",
                            "Initializing ECX to a value less than or equal to zero",
                            "Too many instructions in the loop body",
                        ],
                        [
                            "Initializing ECX to a value greater than zero",
                            "ECX not decrementing properly in the LOOP instruction itself",
                        ]
                    ]
                },
                "format": SELECT_THAT_APPLY,
            },
            "Q4": {
                "details": None,
                "variant": Question.mod3_loops_q4,
                "format": FREE_RESPONSE,
            },
        },
    },
    "Module 4": {
        "Directives": {
            "Q1": {
                "details": {
                    "Match the definition to its directive.": [
                        ["=", "Defines a constant"],
                        ["$", "Used as the current location counter to find the address of the instruction or data label"],
                        ["EQU", "Allows full expressions and lines of assembly code to be copied inline"],
                        ["TEXTEQU", "Replaces the macro with the text or expression definition of the macro, all in a single text-substitution pass"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
        },
        "Equals-sign Directive": {
            "Q1": {
                "details": {
                    "Which of the following correctly defines a constant integer?": "DAYS_INTO_YEAR = 365",
                    "rpt1": "DAYS_INTO_YEAR DWORD 365",
                    "rpt2": "DAYS_INTO_YEAR EQU <MOV EAX, 365>",
                    "rpt3": "EQU DAYS_INTO_YEAR = 365",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q2": {
                "details": {
                    "The equals sign directive (=) may be used for both integer constants and string constants.": "False",
                },
                "format": TRUE_OR_FALSE,
            },
        },
        "EQU Directive": {
            "Q1": {
                "details": {
                    "may": "False",
                    "may not": "True",
                },
                "variant": "Identifiers associated with the EQU directive _ be redefined at any point in a program.",
                "format": TRUE_OR_FALSE,
            },
        },
        # FIXME: formatting issues with radiobutton
        "TEXTEQU Directive": {
            "Q1": {
                "details": {
                    "Which of the following correctly uses the TEXTEQU directive?": "OPTION TEXTEQU <'Pick me!',0>",
                    "rpt1": "TEXTEQU OPTION <'Pick me!',0>",
                    "rpt2": "TEXTEQU <'Pick me!',0> OPTION",
                    "rpt3": "<'Pick me!',0> TEXTEQU OPTION",
                },
                "format": MULTIPLE_CHOICE,
            },
        },
        "Endianness": {
            "Q1": {
                "details": {
                    "Arrays and strings are stored in the same order regardless of system endianness.": "True",
                    "Arrays and strings are stored in a specific order depending on the system endianness.": "False",
                },
                "format": TRUE_OR_FALSE,
            },
            "Q2": {
                "details": {
                    "System endianness affects _.": "byte-wise ordering",
                    "rp1": "memory page ordering",
                    "rp2": "bit-wise ordering",
                    "rp3": "array index ordering",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q3": {
                "details": {
                    "System endianness impacts _ data types": "multi-byte",
                    "rpt1": "multi-bit",
                    "rpt2": "string",
                    "rpt3": "array",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q4": {
                "details": {
                    "The byte-ordering scheme which stores integers in memory with the most significant byte at the lowest address is called _": "big endian",
                    "rpt1": "little endian ",
                    "rpt2": "byte-major",
                    "rpt3": "byte-minor",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q5": {
                "details": {
                    "The byte-ordering scheme which stores integers in memory with the least significant byte at the lowest address is called _": "little endian",
                    "rpt1": "big endian ",
                    "rpt2": "byte-major",
                    "rpt3": "byte-minor",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q6": {
                "details": None,
                "variant": Question.mod4_endianness_q6,
                "format": FREE_RESPONSE,
            },
            "Q7": {
                "details": None,
                "variant": Question.mod4_endianness_q7,
                "format": TRUE_OR_FALSE,
            },
            "Q8": {
                "details": {
                    "What is the minimum size of a data type, in bytes, to be impacted by system endianness?\n\nNOTE: Write your answer as a whole number. For example: 5": "2"
                },
                "format": FREE_RESPONSE,
            },
            "Q9": {
                "details": None,
                "variant": Question.mod4_endianness_q9,
                "format": FREE_RESPONSE,
            },
        },
        "IEEE 754 Floating Point": {
            "Q1": {
                "details": {
                    "Identify the sizes of the sign, biased exponent, and normalized mantissa for a Single Precision x86 floating point value.": "1,8,23",
                },
                "format": FREE_RESPONSE,
            },
            "Q2": {
                "details": {
                    "-12.65": "False",
                    "102.8046875": "True",
                },
                "variant": "The number _ can be represented exactly in IA-32 Floating Point Unit 32-bit IEEE 754 format.",
                "format": TRUE_OR_FALSE,
            },
            "Q3": {
                "details": None,
                "variant": Question.mod4_ieee_754_floating_point_q3,
                "format": SELECT_THAT_APPLY,
            },
            "Q4": {
                "details": None,
                "variant": Question.mod4_ieee_754_floating_point_q4,
                "format": FREE_RESPONSE,
            },
        },
    },
    "Module 5": {
        "Instruction Mnemonics": {
            "Q1": {
                "details": {
                    "Match the definition to its instruction mnemonic.": [
                        ["POPAD", "Pops all the 32-bit general-purpose registers from the system stack"],
                        ["POPA", "Pops all the 16-bit general-purpose registers from the system stack"],
                        ["POPFD", "Pops the top of the system stack into the EFLAGS register"],
                        ["POP", "Copies the data pointed to by the stack pointer into the operand, and then increments the stack pointer"],
                        ["PUSHAD", "Pushes all the 32-bit general-purpose registers into the system stack"],
                        ["PUSHA", "Pushes all the 16-bit general-purpose registers into the system stack"],
                        ["PUSHFD", "Pushes the top of the system stack into the EFLAGS register"],
                        ["PUSH", "Decrements the stack pointer, and then copies the operand into the stack at the location pointed to by the stack pointer"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
        },
        "Stack - Data Structure": {
            "Q1": {
                "details": {
                    "A stack is a data structure with a _ property.": [
                        [
                            "LIFO",
                            "FILO",
                        ],
                        [
                            "LILO",
                            "FIFO"
                        ]
                    ]
                },
                "format": SELECT_THAT_APPLY,
            },
        },
        "Runtime Stack": {
            "Q1": {
                "details": None,
                "variant": Question.mod5_runtime_stack_q1,
                "format": FREE_RESPONSE,
            },
            "Q2": {
                "details": {
                    "PUSH": "True",
                    "POP": "False",
                },
                "variant": "The _ instruction can have an immediate operand.",
                "format": TRUE_OR_FALSE,
            },
            "Q3": {
                "details": None,
                "variant": Question.mod5_runtime_stack_q3,
                "format": TRUE_OR_FALSE,
            },
            "Q4": {
                "details": None,
                "variant": Question.mod5_runtime_stack_q4,
                "format": FREE_RESPONSE,
            },
            "Q5": {
                "details": None,
                "variant": Question.mod5_runtime_stack_q5,
                "format": SELECT_THAT_APPLY,
            },
            "Q6": {
                "details": {
                    "Which of the following is true about the PUSH instruction?": "It decrements the stack pointer (by 2 or 4), and then copies the operand into the stack at the location pointed to by the stack pointer",
                    "rpt1": "It copies the operand into the stack at the location pointed to by the stack pointer, and then decrements the stack pointer (by 2 or 4)",
                    "rpt2": "It increments the stack pointer (by 2 or 4) and copies the operand into the stack at the location pointed to by the stack pointer",
                    "rpt3": "It increments the stack pointer by 1 and copies the operand into the stack at the location pointed to by the stack pointer",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q7": {
                "details": {
                    "Which of the following is true about the POP instruction?": "It copies the data pointed to by the stack pointer into the operand, and then increments the stack pointer (by 2 or 4)",
                    "rpt1": "It copies the data pointed to by the stack pointer into the operand, and then decrements the stack pointer (by 2 or 4)",
                    "rpt2": "It increments the stack pointer (by 2 or 4), and then copies the data pointed to by the stack pointer into the operand",
                    "rpt3": "It copies the data pointed to by the stack pointer into the operand, and then increments the stack pointer by 1",
                },
                "format": MULTIPLE_CHOICE,
            },
        },
        "Procedures": {
            "Q1": {
                "details": {
                    "The RET instruction pops the top of the system stack into the _?": "EIP",
                    "rpt1": "ESP",
                    "rpt2": "EBP",
                    "rpt3": "It does not pop the top of the system stack into a register",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q2": {
                "details": {
                    "pushes": "True",
                    "pops": "False",
                },
                "variant": "Mechanically speaking, the CALL instruction _ its return address on the stack and copies the called procedure's address into the instruction pointer.",
                "format": TRUE_OR_FALSE,
            },
            "Q3": {
                "details": {
                    "The CALL instruction functions similarly to _?": "Push, then Jump",
                    "rpt1": "Jump",
                    "rpt2": "Move, then Jump",
                    "rpt3": "Jump, then Push",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q4": {
                "details": {
                    "The stack frame inside a procedure is also known as the _?": "Activation Record",
                    "rpt1": "Activation Stack",
                    "rpt2": "Procedure Frame",
                    "rpt3": "Program Record",
                    "rpt4": "Local storage",
                    "rpt5": "Stack record",
                    "rpt6": "Heap record",
                    "rpt7": "Peripheral Memory",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q5": {
                "details": {
                    "Which of the following are normally part of the stack frame?": [
                        [
                            "Saved Register Values",
                            "Arguments",
                            "Return Address",
                            "Local Variables",
                        ],
                        [
                            "Calling Procedure",
                            "Starting Address"
                        ]
                    ]
                },
                "format": SELECT_THAT_APPLY,
            },
            "Q6": {
                "details": {
                    "A stack frame is _": "the area of the stack set aside for passed arguments, return address, local variables, and saved registers",
                    "rpt1": "the area of the text segment set aside for passed arguments, subroutine return address, local variables, and saved registers",
                    "rpt2": "a register window pointing to local variables",
                    "rpt3": "an area in the heap that is used to store global variables",
                    "rpt4": "the area of the stack set aside for storing global strings",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q7": {
                "details": {
                    "A subprocedure's stack frame contains the return address and its local variables.": "True",
                },
                "format": TRUE_OR_FALSE,
            },
        },
        "Saving Registers": {
            "Q1": {
                "details": {
                    "What advantages do stack parameters have over register parameters?": [
                        [
                            "Stack parameters reduce code clutter because registers do not have to be saved and restored",
                            "Stack parameters are compatible with high-level languages",
                        ],
                        [
                            "Programs using stack parameters execute more quickly",
                            "Register parameters are optimized for speed",
                        ]
                    ]
                },
                "format": SELECT_THAT_APPLY,
            },
            "Q2": {
                "details": {
                    "on the stack": "True",
                    "in registers": "False",
                },
                "variant": "Passing arguments to a procedure _ can offer a more flexible approach.",
                "format":TRUE_OR_FALSE,
            },
        },
        "Passing Parameters to Procedures": {
            "Q1": {
                "details": {
                    "Match the definition to its parameter classification.": [
                        ["Input Parameter", "Passes a copy of the original data (or a memory address) to the procedure, to which changes to the data in the procedure are not reflected to the original data"],
                        ["Output Parameter", "Passes the memory address to the procedure, to which changes to the data in the procedure are reflected at the memory address"],
                        ["Input/output Parameter", "Passes the memory address (containing the data) to the procedure, to which changes to the data in the procedure are reflected at the memory address"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
            "Q2": {
                "details": {
                    "Match the definition to its procedure composition.": [
                        ["Argument", "A value or reference passed to a procedure"],
                        ["Parameter", "A value or reference received by a procedure"],
                        ["Return", "A value determined by the procedure, and communicated back to the calling procedure"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
            "Q3": {
                "details": {
                    "An argument passed by reference consists of a memory address offset.": "False",
                },
                "format":TRUE_OR_FALSE,
            },
            "Q4": {
                "details": {
                    "Arrays are passed by reference to avoid copying each element into the stack/registers.": "True",
                },
                "format":TRUE_OR_FALSE,
            },
            "Q5": {
                "details": {
                    "Passing by reference requires accessing a parameter's offset from inside the called procedure.": "True",
                },
                "format":TRUE_OR_FALSE,
            },
            "Q6": {
                "details": {
                    "What general types of parameters are passed on the stack?": [
                        [
                            "Reference parameters",
                            "Value parameters",
                        ],
                        [
                            "Activation records",
                            "Stack frames",
                            "Local variables",
                        ]
                    ]
                },
                "format": SELECT_THAT_APPLY,
            },
            "Q7": {
                "details": {
                    "High-level languages always pass arrays to subroutines by value.": "False",
                },
                "format":TRUE_OR_FALSE,
            },
        },
    },
    "Module 6": {
        "Bit Errors": {
            "Q1": {
                "details": {
                    "If they did not have error detection/correction, WiFi systems would almost never send/receive signals containing bit errors.": "False",
                },
                "format": TRUE_OR_FALSE,
            },
            "Q2": {
                "details": {
                    "One cause of bit errors is signal noise.": "True",
                },
                "format": TRUE_OR_FALSE,
            },
        },
        "Parity Bits": {
            "Q1": {
                "details": None,
                "variant": Question.mod6_parity_bits_q1,
                "format": TRUE_OR_FALSE,
            },
            "Q2": {
                "details": None,
                "variant": Question.mod6_parity_bits_q2,
                "format": TRUE_OR_FALSE,
            },
            "Q3": {
                "details": {
                    "Simple parity checks can detect any odd number of errors in a bit stream.": "True",
                    "Simple parity checks can detect any even number of errors in a bit stream.": "False",
                },
                "format": TRUE_OR_FALSE,
            },
            "Q4": {
                "details": {
                    "Simple parity checks can correct any single-bit errors.": "False",
                    "Simple parity checks can detect any single-bit errors.": "True",
                },
                "format": TRUE_OR_FALSE,
            },
        },
    },
    "Module 7": {
        "Referencing Stack Parameters": {
            "Q1": {
                "details": None,
                "variant": Question.mod7_referencing_stack_passed_parameters_q1,
                "format": FREE_RESPONSE,
            },
            "Q2": {
                "details": {
                    "Match the definition to its addressing mode.": [
                        ["Register Indirect", "Register itself is incremented or decremented to change the pointer to another element of the array"],
                        ["Register Direct", "Refers to data in memory using variable names (data labels)"],
                        ["Indexed Operands", "Surrounds any of the 4-byte multi-purpose registers with brackets to access values at their memory location"],
                        ["Base + Offset", "Utilizes a base pointer to establish a known location in memory, and a constant offset from that memory location to access some information"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
            "Q3": {
                "details": {
                    "When passing procedure parameters on the stack, why are the following lines of code often necessary in a procedure?\n\nPUSH EBP\nMOV EBP, ESP": "To keep additional usage of the stack within the procedure from invalidating the stack offsets",
                    "rpt1": "They are never necessary",
                    "rpt2": "To preserve the original EBP register value for register indirect addressing",
                    "rpt3": "Because the procedure might change the EBP register value",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q4": {
                "details": {
                    "Match the following components of the stack frame in the order in which they should be pushed on the stack.": [
                        ["1.", "Passed Parameters"],
                        ["2.", "Procedure Return Address"],
                        ["3.", "Old EBP Value"],
                        ["4.", "Local Variables"],
                        ["5.", "Saved Registers"],
                    ]
                },
                "format": MATCH_TO_ANSWER,
            },
            "Q5": {
                "details": {
                    "Register Indirect": "MOV EAX, [ESI]",
                    "Indexed Operands": "MOV EAX, list[EBX]",
                    "Base+Offset": "MOV EAX, [EDX+EBX]",
                    "Register Direct": "MOV EAX, list[ESI]",
                },
                "variant": "Given the following register states, and using _ addressing, which of the following lines of code will move the 11th element of the list array (of DWORDs) to the EAX register?\nEDX register contains the address (OFFSET) of the first element of list.\nESI register contains the address (OFFSET) of the eleventh element of list.\nEBX register contains the value 40.",
                "format": MULTIPLE_CHOICE,
            },
            "Q6": {
                "details": {
                    "If you reference a point beyond the end of an array in MASM (for example, the address of the what would be the 105th element of a 100-element array), what happens?": "You attempt to access whatever data bytes are stored there",
                    "rpt1": "Compile-time error",
                    "rpt2": "Run-time error",
                    "rpt3": "The disassembler prevents your program from compiling",
                },
                "format": MULTIPLE_CHOICE,
            },
            "Q7": {
                "details": {
                    "list[8]": "5th element",
                    "list[6]": "4th element",
                    "list[14]": "8th element",
                    "list[16]": "9th element",
                },
                "variant": "Given list, an array of WORDs, what element is addressed by _?",
                "format": MULTIPLE_CHOICE,
            },
            "Q8": {
                "details": {
                    "Arrays elements are stored in _ memory.": "contiguous",
                    "rpt1": "random",
                    "rpt2": "disjoint",
                    "rpt3": "distant",
                },
                "format": MULTIPLE_CHOICE,
            },
        },
        "Operators": {
            "Q1": {
                "details": {
                    "Match the definition to its operatives.": [
                        ["TYPE", "Returns the number of bytes in the data type used in the declaration of a given data label"],
                        ["SIZEOF", "Returns the size of memory assigned in the declaration of a given data label"],
                        ["LENGTHOF", "Returns the length used in the declaration of a given data label"],
                        ["OFFSET", "Returns the address offset from the start of the data segment of a given data label"],
                        ["PTR", "Explicitly specifies the number of bytes to write to memory"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
            "Q2": {
                "details": None,
                "variant": Question.mod7_operators_q2,
                "format": FREE_RESPONSE,
            },
            "Q3": {
                "details": None,
                "variant": Question.mod7_operators_q3,
                "format": FREE_RESPONSE,
            },
            "Q4": {
                "details": None,
                "variant": Question.mod7_operators_q4,
                "format": FREE_RESPONSE,
            },
        },
        "Stack Frames": {
            "Q1": {
                "details": None,
                "variant": Question.mod7_stack_frames_q1,
                "format": FREE_RESPONSE,
            },
            "Q2": {
                "details": None,
                "variant": Question.mod7_stack_frames_q2,
                "format": FREE_RESPONSE,
            },
        },
    },
    # "Module 8": {
    #     "Jumps": {
    #         "Q1": {
    #             "details": None,
    #             "variant": ...,
    #             "format": TRUE_OR_FALSE,
    #         },
    #     },
    # },
    # "Module 9": {
    #     "Jumps": {
    #         "Q1": {
    #             "details": None,
    #             "variant": ...,
    #             "format": TRUE_OR_FALSE,
    #         },
    #     },
    # },
    # "Module 10": {
    #     "Jumps": {
    #         "Q1": {
    #             "details": None,
    #             "variant": ...,
    #             "format": TRUE_OR_FALSE,
    #         },
    #     },
    # },
}
