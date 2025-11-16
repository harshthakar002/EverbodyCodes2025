f = open('./1/inp2.txt', 'r')
nameStr = f.readline()
f.readline()
instructionStr = f.readline()
names = nameStr.split(',')
instructions = instructionStr.split(',')
index = 0
def goToInstruction(index: int, instruction: str, limit: int):
    if instruction[0] == 'R':
        jump = int(instruction[1:])
        return index + jump
    else:
        jump = int(instruction[1:])
        return index - jump

for instruction in instructions:
    index = goToInstruction(index, instruction, len(names))

print(names[index])