from app import *

def test_sum_all_nums():
    jp = JsonParser('[1,2,3]')
    assert jp.sum_all_nums() == 6

    jp = JsonParser('{"a":2,"b":4}')
    assert jp.sum_all_nums() == 6

    jp = JsonParser('[[[3]]]')
    assert jp.sum_all_nums() == 3

    jp = JsonParser('{"a":{"b":4},"c":-1}')
    assert jp.sum_all_nums() == 3

    jp = JsonParser('{"a":[-1,1]}')
    assert jp.sum_all_nums() == 0

    jp = JsonParser('[-1,{"a":1}]')
    assert jp.sum_all_nums() == 0


def test_sum_all_nums_red():
    jp = JsonParserRed('[1,2,3]')
    assert jp.sum_all_nums() == 6

    jp = JsonParserRed('[1,{"c":"red","b":2},3]')
    assert jp.sum_all_nums() == 4

    jp = JsonParserRed('{"d":"red","e":[1,2,3,4],"f":5}')
    assert jp.sum_all_nums() == 0

    jp = JsonParserRed('[1,"red",5]')
    assert jp.sum_all_nums() == 6
