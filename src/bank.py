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
                    "An assembly language is defined by an instruction set architecture (ISA)": "True",
                },
                "format": TRUE_OR_FALSE,
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
                "variant": "The ASCII code values for alphabetic letters are _ than for decimal digits",
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
                    "The CPU clock cycle length is the only contributing factor to the speed of operations on a computer.": "True",
                },
                "format": TRUE_OR_FALSE,
            },
        },
        "Main Memory": {
            "Q1": {
                "details": {
                    "In a specific architecture, created by _, programs are stored in memory and executed according to an instruction execution cycle": "John von Neumann",
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
                        ["WriteInt", "Writes a signed integer to the console window"],
                        ["WriteDec", "Writes an unsigned integer to the console window"],
                        ["WriteString", "Writes a string to the console window"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
        },
    },
    "Module 3": {
        "Directives": {
            "Q1": {
                "details": {
                    "Match the definition to its directive.": [
                        [".data", "Marks beginning of the data segment"],
                    ]
                },
                "format": MATCH_TO_ANSWER_RANDOMIZED,
            },
        },
    },
}
