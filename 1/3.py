f = open('./1/inp3.txt', 'r')
nameStr = f.readline()
f.readline()
instructionStr = f.readline()
names = nameStr.split(',')
instructions = instructionStr.split(',')
index = 0
def goToInstruction(index: int, instruction: str, limit: int):
    if instruction[0] == 'R':
        jump = int(instruction[1:])
        return (index + jump)%limit
    else:
        jump = int(instruction[1:])
        return (index - jump)%limit

for instruction in instructions:
    index = goToInstruction(index, instruction, len(names))
    names[0], names[index] = names[index], names[0]
    index = 0

print(names[index])