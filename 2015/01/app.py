def what_floor(instructions):
    floor = 0
    for instruction in instructions:
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1
        else:
            raise Exception('Instruction not either "(" or ")"')
    return floor

if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = f.read()
    print(what_floor(input))
