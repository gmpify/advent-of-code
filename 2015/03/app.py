class Santa:
    NORTH_MOVE = '^'
    SOUTH_MOVE = 'v'
    EAST_MOVE = '>'
    WEST_MOVE = '<'

    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.presents_delivered_per_house = {}
        self.deliver_present()

    def houses_visited(self):
        return len(self.presents_delivered_per_house)

    def move(self, instructions):
        for instruction in instructions:
            self.step(instruction)

    def step(self, instruction):
        if instruction == self.NORTH_MOVE:
            self.y += 1
            self.deliver_present()
        elif instruction == self.SOUTH_MOVE:
            self.y -= 1
            self.deliver_present()
        elif instruction == self.EAST_MOVE:
            self.x += 1
            self.deliver_present()
        elif instruction == self.WEST_MOVE:
            self.x -= 1
            self.deliver_present()
        else:
            raise Exception('Wrong instructions')

    def deliver_present(self):
        self.presents_delivered_per_house[self.position()] = self.presents_delivered_per_house.get(self.position(), 0) + 1
    
    def position(self):
        return (self.x, self.y)

if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = f.read()

    santa = Santa()
    santa.move(input)

    print('Houses visited: ', santa.houses_visited())
