class Santa:
    MOVE_UP = '('
    MOVE_DOWN = ')'

    def __init__(self, instructions) -> None:
        self._instructions = instructions
        self.step = 0
        self.floor = 0

    def move(self):
        while self.can_move_step():
            self.move_step()

    def enter_basement(self):
        while self.can_move_step() and self.floor >= 0:
            self.move_step()

    def can_move_step(self):
        return self.step < len(self._instructions)

    def move_step(self):
        instruction = self._instructions[self.step]
        if instruction == self.MOVE_UP:
            self.floor += 1
        elif instruction == self.MOVE_DOWN:
            self.floor -= 1
        else:
            raise Exception('Wrong instructions')
        self.step += 1

if __name__ == '__main__':
    f = open('input.txt', 'r')
    instructions = f.read()
    santa = Santa(instructions)
    santa.move()
    print('Part 1: ', santa.floor)

    santa = Santa(instructions)
    santa.enter_basement()
    print('Part 2: ', santa.step)
