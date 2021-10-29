from app import *


def test_process():
    look_and_say = LookAndSay()
    assert look_and_say.process('1') == '11'
    assert look_and_say.process('11') == '21'
    assert look_and_say.process('21') == '1211'
    assert look_and_say.process('1211') == '111221'
    assert look_and_say.process('111221') == '312211'
