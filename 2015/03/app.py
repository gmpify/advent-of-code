class DistributionPlan:
    def __init__(self, instructions, santa_numbers = 1):
        self.instructions = instructions
        self.santas = [Santa() for _ in range(santa_numbers)]
        self.houses = set()
        for santa in self.santas:
            self.houses.add(santa.position())
        self.santa_to_move = 0

    def houses_visited(self):
        return len(self.houses)

    def execute(self):
        for instruction in self.instructions:
            santa = self.santas[self.santa_to_move]
            santa.move(instruction)
            self.houses.add(santa.position())

            self.set_santa_to_move()

    def set_santa_to_move(self):
        self.santa_to_move = (self.santa_to_move + 1) % len(self.santas)

class Santa:
    NORTH_MOVE = '^'
    SOUTH_MOVE = 'v'
    EAST_MOVE = '>'
    WEST_MOVE = '<'

    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, instruction):
        if instruction == self.NORTH_MOVE:
            self.y += 1
        elif instruction == self.SOUTH_MOVE:
            self.y -= 1
        elif instruction == self.EAST_MOVE:
            self.x += 1
        elif instruction == self.WEST_MOVE:
            self.x -= 1
        else:
            raise Exception('Wrong instructions')
    
    def position(self):
        return (self.x, self.y)

if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = f.read()

    plan = DistributionPlan(input)
    plan.execute()

    print('Houses visited: ', plan.houses_visited())
