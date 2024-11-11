class Machine:
    def __init__(self, code):
        self.code = code
        self.row = 1
        self.column = 1
    
    def next(self):
        if self.row == 1:
            self.row = self.column + 1
            self.column = 1
        else:
            self.column += 1
            self.row -= 1
        
        self.code *= 252533
        self.code %= 33554393

    def resolve(self, row, column):
        while row != self.row or column != self.column:
            self.next()
        return self.code

if __name__ == "__main__":
    m = Machine(20151125)
    
    print("Part 1:", m.resolve(2947, 3029))
