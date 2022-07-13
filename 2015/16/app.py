import re

class Sue:
    def __init__(self, number):
        self.number = number
        self.things = {}

    def has(self, things):
        for thing in things:
            if thing in self.things and things[thing] != self.things[thing]:
                return False
        return True

    def load(input):
        m = re.match(r'Sue (?P<number>\d*): (?P<rest>.*)', input)
        number = m.group('number')
        sue = Sue(number)

        rest = m.group('rest')
        for thing in rest.split(','):
            m = re.match(r'(?P<key>\w*): (?P<value>\d*)', thing.strip())
            key = m.group('key')
            value = int(m.group('value'))
            sue.things[key] = value

        return sue


def process(file, things):

    for line in open(file):
        s = Sue.load(line)

        if s.has(things):
            print(f"Found Sue! It's #{s.number}")
            return

if __name__ == '__main__':
    things = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    process('input.txt', things)
