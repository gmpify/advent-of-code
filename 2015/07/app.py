from os import curdir
import re

class Wire:
    def __init__(self, input):
        self.signal_input = input
        self.signal = None
        self.dependencies = set()
        self.resolved_dependencies = {}
        self.parse_dependencies()

    def parse_dependencies(self):
        for input_wire in re.findall(r'[a-z]{1,2}', self.signal_input):
            self.dependencies.add(input_wire)

    def has_unresolved_dependencies(self):
        return len(self.dependencies) != len(self.resolved_dependencies)
    
    def resolve_dependency(self, element, signal):
        if element in self.dependencies:
            self.resolved_dependencies[element] = signal

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
        self.signal = int(value)
        return self.signal

class WirePassThrough(Wire):
    def resolve(self):
        m = re.match(r'(?P<wire>\w{1,2})', self.signal_input)
        wire = m.group('wire')
        self.signal = self.resolved_dependencies[wire]
        return self.signal

class WireAnd(Wire):
    def resolve(self):
        m = re.match(r'(?P<wire_1>[a-z1-9]{1,2}) AND (?P<wire_2>[a-z]{1,2})', self.signal_input)
        wire_1, wire_2 = m.group('wire_1'), m.group('wire_2')
        result = None
        if wire_1.isnumeric():
            result = int(wire_1) & self.resolved_dependencies[wire_2]
        else:
            result = self.resolved_dependencies[wire_1] & self.resolved_dependencies[wire_2]
        self.signal = result
        return self.signal

class WireOr(Wire):
    def resolve(self):
        m = re.match(r'(?P<wire_1>[a-z]{1,2}) OR (?P<wire_2>[a-z]{1,2})', self.signal_input)
        wire_1, wire_2 = m.group('wire_1'), m.group('wire_2')
        self.signal = self.resolved_dependencies[wire_1] | self.resolved_dependencies[wire_2]
        return self.signal

class WireNot(Wire):
    def resolve(self):
        m = re.match(r'NOT (?P<wire>[a-z]{1,2})', self.signal_input)
        wire = m.group('wire')
        self.signal = ~ self.resolved_dependencies[wire]
        return self.signal

class WireLShift(Wire):
    def resolve(self):
        m = re.match(r'(?P<wire>[a-z]{1,2}) LSHIFT (?P<bit_position>\d+)', self.signal_input)
        wire, bit_position = m.group('wire'), m.group('bit_position')
        self.signal = self.resolved_dependencies[wire] << int(bit_position)
        return self.signal

class WireRShift(Wire):
    def resolve(self):
        m = re.match(r'(?P<wire>[a-z]{1,2}) RSHIFT (?P<bit_position>\d+)', self.signal_input)
        wire, bit_position = m.group('wire'), m.group('bit_position')
        self.signal = self.resolved_dependencies[wire] >> int(bit_position)
        return self.signal

class Circuit:
    def __init__(self):
        self.wires = {}

    def resolve(self):
        while True:
            element = self.find_unresolved_element_without_dependencies()
            if element is None:
                break
            value = self.wires[element].resolve()
            print(f'{element}: {value}')
            self.resolve_dependencies_from_element(element, value)

    def find_unresolved_element_without_dependencies(self):
        for identifier, wire in self.wires.items():
            if wire.signal is None and not wire.has_unresolved_dependencies():
                return identifier
        return None

    def resolve_dependencies_from_element(self, element, value):
        for _, wire in self.wires.items():
            wire.resolve_dependency(element, value)

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
