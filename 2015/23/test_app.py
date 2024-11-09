from app import *
import pytest

def test_parser():
    f = open('test_instructions.txt', 'r')
    instructions = f.read().split('\n')
    parser = Parser(instructions)
    parser.run()
    assert(parser.registers['a'].current == 2)
    