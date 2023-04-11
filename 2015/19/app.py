import re

class Machine:
    def __init__(self, replacement_rules, calibration_input) -> None:
        self.replacement_rules = replacement_rules
        self.calibration_input = calibration_input
        self.distinct_molecules = set()

        self.process()

    def process(self):
        for replacement_rule in self.replacement_rules:
            m = re.match(r'(?P<old>.*) => (?P<new>.*)', replacement_rule)
            old = m.group('old')
            new = m.group('new')

            start_position = 0
            position = self.calibration_input.find(old, start_position)
            while position != -1:
                head = self.calibration_input[0:start_position]
                tail = self.calibration_input[start_position:-1].replace(old, new, 1)

                self.distinct_molecules.add(head + tail)

                start_position = position + len(old)
                position = self.calibration_input.find(old, start_position)
    
    def distinct_molecules_count(self):
        return len(self.distinct_molecules)

if __name__ == '__main__':
    rules = []
    calibration_input = ''

    for line in open('input.txt').read().split('\n'):
        if "=>" in line:
            rules.append(line)
        elif line == "":
            pass
        else:
            calibration_input = line

    print("Part 1")
    machine = Machine(rules, calibration_input)
    count = machine.distinct_molecules_count()

    print(f"There are {count} different possible molecules")
