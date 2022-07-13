from app import *


def test_distance_at():
    reindeer = Reindeer.load('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.')
    reindeer.calculate_until(1000)
    assert reindeer.distance_at(1) == 14
    assert reindeer.distance_at(10) == 140
    assert reindeer.distance_at(11) == 140
    assert reindeer.distance_at(1000) == 1120

    reindeer = Reindeer.load('Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.')
    reindeer.calculate_until(1000)
    assert reindeer.distance_at(1) == 16
    assert reindeer.distance_at(10) == 160
    assert reindeer.distance_at(11) == 176
    assert reindeer.distance_at(1000) == 1056
