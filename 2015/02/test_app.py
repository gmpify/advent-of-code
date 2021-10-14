import pytest
from app import Box, parse_boxes, calculate_total_paper_needed


@pytest.fixture
def box1():
    return Box(2, 3, 4)


@pytest.fixture
def box2():
    return Box(1, 1, 10)


def test_surface_area_box1(box1):
    assert box1.surface_area() == 52


def test_surface_area_box2(box2):
    assert box2.surface_area() == 42


def test_smallest_side_area_box1(box1):
    assert box1.smallest_side_area() == 6


def test_smallest_side_area_box2(box2):
    assert box2.smallest_side_area() == 1


def test_needed_wrapping_paper_box1(box1):
    assert box1.needed_wrapping_paper() == 58


def test_needed_wrapping_paper_box2(box2):
    assert box2.needed_wrapping_paper() == 43


def test_parse_boxes(box1, box2):
    measures = [
        '2x3x4',
        '1x1x10'
    ]

    assert parse_boxes(measures) == [box1, box2]


def test_calculate_total_paper_needed(box1, box2):
    assert calculate_total_paper_needed([box1, box2]) == 101
