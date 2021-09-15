import pytest


@pytest.mark.parametrize("point1, point2, x, expected" [
    ([1,1], [2,2], 3, 3)])
def test_y_coordinate(point1, point2, x, expected):
    from two_point_line import y_coordinate
    answer = y_coordinate(point1, point2, x)
    assert answer == expected