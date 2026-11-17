lines = open("src/main.S", "r").readlines()

format_map = {
    1: 2,
    2: 2,
    3: 2,
    4: 4,
    5: 4,
    6: 4,
    7: 4,
}


instruction_map = {
    "bv": 3,
    "bc": 3,
    "blt": 3,
    "ble": 3,
    "bl": 3,
    "be": 3,
    "bz": 3,
    "bnh": 3,
    "br": 3,
    "bnv": 3,
    "bnc": 3,
    "bnl": 3,
    "bnz": 3,
    "bne": 3,
    "bn": 3,
    "bh": 3,
    "bp": 3,
    "bge": 3,
    "bgt": 3,

    "movea": 5,
    "addi": 5,
    "jr": 4,
    "jal": 4,
    "ori": 5,
    "andi": 5,
    "xori": 5,
    "movhi": 5,
    "ld.b": 6,
    "ld.h": 6,
    "ld.w": 6,
    "st.b": 6,
    "st.h": 6,
    "st.w": 6,
    "in.b": 6,
    "in.h": 6,
    "caxi": 6,
    "in.w": 6,
    "out.b": 6,
    "out.h": 6,
    "out.w": 6,

    "cmpf.s": 7,
    "cvt.ws": 7,
    "cvt.sw": 7,
    "addf.s": 7,
    "subf.s": 7,
    "mulf.s": 7,
    "divf.s": 7,
    "xb": 7,
    "xh": 7,
    "rev": 7,
    "trnc.sw": 7,
    "mpyhw": 7,

    "cli": 2,
    "sei": 2,


    "mov": 1,
    "add": 1,
    "sub": 1,
    "cmp": 1,
    "shl": 1,
    "shr": 1,

    "jmp": 1,
    "sar": 1,

    "mulu": 1,

    "divu": 1,
    "or": 1,
    "and": 1,
    "xor": 1,
    "not": 1,

    "setf": 2,
    "trap": 2,
    "reti": 2,
    "halt": 2,
    "ldsr": 2,
    "stsr": 2,
    "sei": 2,

    "mul": 1,

    "div": 1,
    "ei": 1,
    "di": 1,
}

local_instructions = [
"jal",
"jr",
"be",
"bne",
"blt",
"ble",
"bl",
"bgt",
"bge",
"bnh",
"bnl",
"bh"
]

gotos = []

out_lines = []
pc = 0
i = 0
while i < len(lines):
    line = lines[i].strip()

    found = False
    for keyword in list(instruction_map.keys()):
        if line.startswith(keyword):
            line = f"B{pc:04X}: {line}"
            length = format_map[instruction_map[keyword]]
            if keyword in local_instructions:
                label, opcode, goto = line.split(" ", 2)
                if goto.find(".+") != -1:
                    goto = goto[2:]
                    if goto.isdigit() or (goto.startswith("-") and goto[1:].isdigit()):
                        goto = f"B{pc+int(goto):04X}"
                        gotos.append(goto)
                        line = f"{label} {opcode} {goto}"
            pc += length
            found = True
            break

    out_lines.append(line+"\n")
    i += 1

i = 0
while i < len(out_lines):
    line = out_lines[i].strip()
    if line.find(":") != -1 and not line.endswith(":"):
        label, contents = line.split(":", 1)
        if label.startswith("B"):
            if label in gotos:
                out_lines.insert(i, label+":\n")
                i += 1
            out_lines[i] = contents.strip()+"\n"

    i += 1

open("test.S", "w").writelines(out_lines)