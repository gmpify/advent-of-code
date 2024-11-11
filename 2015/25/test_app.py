import pytest
from app import *

def test_2_2():
    m = Machine(20151125)
    assert(m.resolve(2, 2) == 21629792)

def test_6_6():
    m = Machine(20151125)
    assert(m.resolve(6, 6) == 27995004)

