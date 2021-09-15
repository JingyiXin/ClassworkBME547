import pytest


@pytest.mark.parametrize("point1, point2, x, expected", [
    ((1,1), (2,2), 3, 3),
    ((0,0), (1,2), 2, 4),
    ((0,3), (1,6), 2, 9)])
def test_y_coordinate(point1, point2, x, expected):
    from two_point_line import y_coordinate
    answer = y_coordinate(point1, point2, x)
    assert answer == expected