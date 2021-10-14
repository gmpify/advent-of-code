class Santa:
    NORTH_MOVE = '^'
    SOUTH_MOVE = 'v'
    EAST_MOVE = '>'
    WEST_MOVE = '<'

    def __init__(self, instructions) -> None:
        self.instructions = instructions
        self.x = 0
        self.y = 0
        self.presents_delivered_per_house = {}
        self.deliver_present()

    def move(self):
        for instruction in self.instructions:
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

    def houses_visited(self):
        return len(self.presents_delivered_per_house)

    def position(self):
        return (self.x, self.y)

    def deliver_present(self):
        self.presents_delivered_per_house[self.position()] = self.presents_delivered_per_house.get(self.position(), 0) + 1

if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = f.read()

    santa = Santa(input)
    santa.move()

    print('Houses visited: ', santa.houses_visited())
