import itertools, re

class Person:
    def __init__(self, name):
        self.name = name
        self.happiness_change = {}

    def __repr__(self):
        return self.name

    def get_neighbour_change(self, neighbour):
        return self.happiness_change[neighbour]

    def load_all(file_name):
        result = {}
        file = open(file_name)
        for line in file:
            m = re.match(r'(?P<person>\w*) would (?P<change>\w*) (?P<change_value>\d*) happiness units by sitting next to (?P<neighbour>\w*).', line)
            person = m.group('person')
            neighbour = m.group('neighbour')
            change_value = int(m.group('change_value'))
            if m.group('change') == 'lose':
                change_value *= -1

            if person not in result:
                result[person] = Person(person)
            p = result[person]
            if neighbour not in result:
                result[neighbour] = Person(neighbour)
            n = result[neighbour]
            p.happiness_change[n] = change_value

        return set(result.values())

class Arrangement:
    def __init__(self, order):
        self.order = order
        self.happiness = 0

    def __repr__(self):
        return f"Happiness: {self.happiness}\nOrder: {self.order}"

    def calculate_happiness(self):
        for i, person in enumerate(self.order):
            neighbour_1 = self.order[i - 1]
            neighbour_2 = self.order[(i + 1) % len(self.order)]
            self.happiness += person.get_neighbour_change(neighbour_1)
            self.happiness += person.get_neighbour_change(neighbour_2)

    def load_all(participants):
        names = participants
        result = itertools.permutations(names, len(names))
        return list(map(lambda a: Arrangement(a), result))

def process(file_name):
    people = Person.load_all(file_name)
    arrangements = Arrangement.load_all(people)
    best_arrangement = None
    for arrangement in arrangements:
        arrangement.calculate_happiness()
        if not best_arrangement or arrangement.happiness > best_arrangement.happiness:
            best_arrangement = arrangement
    print(f"Best arrangement for {file_name}")
    print(best_arrangement)


if __name__ == '__main__':
    process('test.txt')

    process('input.txt')

    process('input2.txt')
