import pytest
import app

def test_matching_instructions():
    assert app.what_floor('(())') == 0
    assert app.what_floor('()()') == 0

def test_upper_floors():
    assert app.what_floor('(((') == 3
    assert app.what_floor('(()(()(') == 3
    assert app.what_floor('))(((((') == 3

def test_basement_floors():
    assert app.what_floor('())') == -1
    assert app.what_floor('))(') == -1

def test_deeper_basement_floors():
    assert app.what_floor(')))') == -3
    assert app.what_floor(')())())') == -3

def test_invalid_instructions():
    with pytest.raises(Exception):
        app.what_floor('((foobar))')
