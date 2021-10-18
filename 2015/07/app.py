from os import curdir
import re

class Wire:
    def __init__(self, input):
        self.signal_input = input
        self.signal = None
        self.depends_on = set()
        self.parse_dependencies()

    def parse_dependencies(self):
        for input_wire in re.findall(r'[a-z]{1,2}', self.signal_input):
            self.depends_on.add(input_wire)

    def has_dependencies(self):
        return len(self.depends_on) > 0
    
    def remove_dependency(self, element):
        self.depends_on.discard(element)

    @classmethod
    def build_wire_type(self, input):
        if 'AND' in input:
            wire = WireAnd(input)
        elif 'OR' in input:
            wire = WireOr(input)
        elif 'NOT' in input:
            wire = WireNot(input)
        elif 'LSHIFT' in input:
            wire = WireLShift(input)
        elif 'RSHIFT' in input:
            wire = WireRShift(input)
        elif input.isnumeric():
            wire = WireValue(input)
        else:
            wire = WirePassThrough(input)
        return wire
    
class WireValue(Wire):
    def resolve(self):
        m = re.match(r'(?P<value>\d+)', self.signal_input)
        value = m.group('value')
        return lambda _: int(value)

class WirePassThrough(Wire):
    def resolve(self):
        m = re.match(r'(?P<wire>\w{1,2})', self.signal_input)
        wire = m.group('wire')
        return lambda wires: wires[wire].signal

class WireAnd(Wire):
    def resolve(self):
        m = re.match(r'(?P<wire_1>[a-z1-9]{1,2}) AND (?P<wire_2>[a-z]{1,2})', self.signal_input)
        wire_1, wire_2 = m.group('wire_1'), m.group('wire_2')
        result = lambda _: None
        if wire_1.isnumeric():
            result = lambda wires: int(wire_1) & wires[wire_2].signal
        else:
            result = lambda wires: wires[wire_1].signal & wires[wire_2].signal
        return result

class WireOr(Wire):
    def resolve(self):
        m = re.match(r'(?P<wire_1>[a-z]{1,2}) OR (?P<wire_2>[a-z]{1,2})', self.signal_input)
        wire_1, wire_2 = m.group('wire_1'), m.group('wire_2')
        return lambda wires: wires[wire_1].signal | wires[wire_2].signal

class WireNot(Wire):
    def resolve(self):
        m = re.match(r'NOT (?P<wire>[a-z]{1,2})', self.signal_input)
        wire = m.group('wire')
        return lambda wires: ~ wires[wire].signal

class WireLShift(Wire):
    def resolve(self):
        m = re.match(r'(?P<wire>[a-z]{1,2}) LSHIFT (?P<bit_position>\d+)', self.signal_input)
        wire, bit_position = m.group('wire'), m.group('bit_position')
        return lambda wires: wires[wire].signal << int(bit_position)

class WireRShift(Wire):
    def resolve(self):
        m = re.match(r'(?P<wire>[a-z]{1,2}) RSHIFT (?P<bit_position>\d+)', self.signal_input)
        wire, bit_position = m.group('wire'), m.group('bit_position')
        return lambda wires: wires[wire].signal >> int(bit_position)

class Circuit:
    def __init__(self):
        self.wires = {}

    def resolve(self):
        while True:
            element = self.find_unresolved_element_without_dependencies()
            if element is None:
                break
            func = self.wires[element].resolve()
            value = func(self.wires)
            self.wires[element].signal = value
            print(f'{element}: {value}')
            self.delete_element_in_dependencies(element)

    def find_unresolved_element_without_dependencies(self):
        for identifier, wire in self.wires.items():
            if wire.signal is None and not wire.has_dependencies():
                return identifier
        return None

    def delete_element_in_dependencies(self, element):
        for _, wire in self.wires.items():
            wire.remove_dependency(element)

    def add_instruction(self, instruction):
        input, identifier = [term.strip() for term in instruction.split('->')]
        wire = Wire.build_wire_type(input)
        self.wires[identifier] = wire

if __name__ == '__main__':
    f = open('input.txt')
    input = f.read().split('\n')

    circuit = Circuit()
    for line in input:
        circuit.add_instruction(line)
    
    circuit.resolve()
