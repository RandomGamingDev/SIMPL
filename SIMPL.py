# INCLUDE <NAME>
# LOGIC <OUTPUT> <INPUT1> <INPUT2?> <LENGTH> <STEP>
# AND, ORR, XOR, NOT
# DEF <TO> <FROM>
# GOTO <NAME>
# LBL <NAME>

def convert(line):
    output = "  "
    elements = line.split(' ')

    match elements[0]:
        # GATES
        case "AND":
            if len(elements) == 5:
                output += f"for (size_t i = 0; i < { elements[4] }; i++) "
                output += f"mem[{ int(elements[1]) } + i] = mem[{ int(elements[2]) } + i] & mem[{ int(elements[3]) } + i];"
            else:
                output += f"mem[{ int(elements[1]) }] = mem[{ int(elements[2]) }] & mem[{ int(elements[3]) }];"
        case "OR":
            if len(elements) == 5:
                output += f"for (size_t i = 0; i < { elements[4] }; i++) "
                output += f"mem[{ int(elements[1]) } + i] = mem[{ int(elements[2]) } + i] | mem[{ int(elements[3]) } + i];"
            else:
                output += f"mem[{ int(elements[1]) }] = mem[{ int(elements[2]) }] | mem[{ int(elements[3]) }];"
        case "XOR":
            if len(elements) == 5:
                output += f"for (size_t i = 0; i < { elements[4] }; i++) "
                output += f"mem[{ int(elements[1]) } + i] = mem[{ int(elements[2]) } + i] ^ mem[{ int(elements[3]) } + i];"
            else:
                output += f"mem[{ int(elements[1]) }] = mem[{ int(elements[2]) }] ^ mem[{ int(elements[3]) }];"
        case "NOT":
            if len(elements) == 4:
                output += f"for (size_t i = 0; i < { elements[3] }; i++) "
                output += f"mem[{ int(elements[1]) } + i] = !mem[{ int(elements[2]) } + i];"
            else:
                output += f"mem[{ int(elements[1]) }] = !mem[{ int(elements[2]) }];"

        # DEFINE
        case "DEF":
            output += f"#define { elements[1] } { elements[2] }"

        # GOTO & LABEL
        case "GOTO":
            output += f"goto { elements[1] };"
        case "LABEL":
            output += f"{ elements[1] }:"

        # INCLUDE
        case "INCLUDE":
            includeFile = open(elements[1], "r", encoding="utf-8")
            include = includeFile.readlines()
            includeFile.close()
            for line in include:
                convert(line)

    print(output)

codeFile = open(input("Enter the SIMPL file location: "), "r", encoding="utf-8")
code = codeFile.readlines()
codeFile.close()

print("#include <bitset>")
memLen = int(code[0][0 : len(code)])
print(f"std::bitset<{memLen}> mem = std::bitset<{memLen}>();")
print("int main() {")
for i in range(1, len(code)):
    convert(code[i])
print('}')