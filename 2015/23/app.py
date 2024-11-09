import re

class Register:
    def __init__(self, current = 0):
        self.current = current

    def hlf(self):
        self.current /= 2
    
    def tpl(self):
        self.current *= 3
    
    def inc(self):
        self.current += 1

    def is_even(self):
        return self.current % 2 == 0
    
    def is_one(self):
        return self.current == 1

class Parser:
    def __init__(self, registers, lines):
        self.registers = registers
        self.lines = lines
        self.current_line = 0
    
    def run(self):
        while self.current_line < len(self.lines):
            self.parse_line(self.lines[self.current_line])

    def parse_line(self, line):
        if line.startswith('hlf') or line.startswith('tpl') or line.startswith('inc'):
            instruction, register = line.split()
            if register not in self.registers:
                raise Exception("Register not known")
            
            f = getattr(Register, instruction)
            f(self.registers[register])
            self.current_line += 1
        elif line.startswith('jmp'):
            _, offset = line.split()
            self.current_line += int(offset)
        elif line.startswith('jie'):
            instruction_raw, offset = line.split(',')
            _, register = instruction_raw.split()
            if register not in self.registers:
                raise Exception("Register not known")
            
            if self.registers[register].is_even():
                self.current_line += int(offset)
            else:
                self.current_line += 1
        elif line.startswith('jio'):
            instruction_raw, offset = line.split(',')
            _, register = instruction_raw.split()
            if register not in self.registers:
                raise Exception("Register not known")
            
            if self.registers[register].is_one():
                self.current_line += int(offset)
            else:
                self.current_line += 1
        else:
            raise Exception("Instruction not known")

if __name__ == '__main__':
    f = open('instructions.txt', 'r')
    instructions = f.read().split('\n')
    
    registers = {
        'a': Register(),
        'b': Register()
    }

    parser = Parser(registers, instructions)
    parser.run()

    print('Register b is:', parser.registers['b'].current)

    registers = {
        'a': Register(1),
        'b': Register()
    }

    parser = Parser(registers, instructions)
    parser.run()
    
    print('Register b is:', parser.registers['b'].current)
