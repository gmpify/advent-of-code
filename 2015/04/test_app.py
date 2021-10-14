import pytest
from app import *

def test_mine_key_1():
    m = Md5Miner('abcdef')
    assert m.mine() == 609043

def test_mine_key_2():
    m = Md5Miner('pqrstuv')
    assert m.mine() == 1048970
