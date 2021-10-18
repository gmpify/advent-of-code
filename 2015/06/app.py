import re

class Light:
    OFF = 0
    ON = 1
    def __init__(self):
        self.status = self.OFF

    def command(self, action):
        str_to_func = {
            'turn on': self.turn_on,
            'turn off': self.turn_off,
            'toggle': self.toggle
        }
        func = str_to_func.get(action, lambda: None)
        return func()

    def turn_on(self):
        self.status = self.ON

    def turn_off(self):
        self.status = self.OFF

    def toggle(self):
        if self.status == self.ON:
            self.turn_off()
        else:
            self.turn_on()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if (isinstance(other, Point)):
            return self.x == other.x and self.y == other.y
        return False

    @classmethod
    def parse(self, coordinates):
        x, y = [int(n) for n in coordinates.split(',')]
        return Point(x, y)


class Grid:
    def __init__(self, size=1000):
        self.size = 1000
        self.lights = [[Light() for _ in range(size)] for _ in range(size)]

    def count_lights(self, status=Light.ON):
        result = 0
        for x in range(self.size):
            for y in range(self.size):
                light = self.lights[x][y]
                if light.status == status:
                    result += 1
        return result

    def run_command(self, command):
        action, begin, end = self.parse_command(command)
        for x in range(begin.x, end.x + 1):
            for y in range(begin.y, end.y + 1):
                light = self.lights[x][y]
                light.command(action)

    def parse_command(self, command):
        m = re.match(r'(?P<action>.*)\s(?P<begin>\d{1,3},\d{1,3}) through (?P<end>\d{1,3},\d{1,3})', command)
        action = m.group('action')
        begin = Point.parse(m.group('begin'))
        end = Point.parse(m.group('end'))
        return action, begin, end


if __name__ == '__main__':
    f = open('input.txt')
    input = f.read().split('\n')

    grid = Grid()
    for command in input:
        grid.run_command(command)
    
    print('Number of lights lit are: ', grid.count_lights())
