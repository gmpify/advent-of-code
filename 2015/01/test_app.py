import pytest
import app

def test_matching_instructions():
    s = app.Santa('(())')
    s.follow_instructions()
    assert s.floor == 0

    s = app.Santa('()()')
    s.follow_instructions()
    assert s.floor == 0


def test_upper_floors():
    s = app.Santa('(((')
    s.follow_instructions()
    assert s.floor == 3

    s = app.Santa('(()(()(')
    s.follow_instructions()
    assert s.floor == 3

    s = app.Santa('))(((((')
    s.follow_instructions()
    assert s.floor == 3


def test_basement_floors():
    s = app.Santa('())')
    s.follow_instructions()
    assert s.floor == -1

    s = app.Santa('))(')
    s.follow_instructions()
    assert s.floor == -1


def test_deeper_basement_floors():
    s = app.Santa(')))')
    s.follow_instructions()
    assert s.floor == -3

    s = app.Santa(')())())')
    s.follow_instructions()
    assert s.floor == -3


def test_invalid_instructions():
    with pytest.raises(Exception):
        app.Santa('((foobar))').follow_instructions()


def test_enter_basement_on_first_step():
    s = app.Santa(')')
    s.enter_basement()
    assert s.step == 1


def test_enter_basement_on_last_step():
    s = app.Santa('()())')
    s.enter_basement()
    assert s.step == 5
