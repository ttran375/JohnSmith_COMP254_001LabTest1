import pytest
from .singly_linked_list import SinglyLinkedList


@pytest.mark.parametrize(
    "elements, expected_list1, expected_list2",
    [
        ([], [], []),
        ([1], [1], []),
        ([1, 2], [1], [2]),
        ([1, 2, 3], [1, 2], [3]),
        ([1, 2, 3, 4], [1, 2], [3, 4]),
        ([1, 2, 3, 4, 5], [1, 2, 3], [4, 5]),
        ([1, 2, 3, 4, 5, 6], [1, 2, 3], [4, 5, 6]),
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4], [5, 6, 7]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4], [5, 6, 7, 8]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5], [6, 7, 8, 9]),
        (
            [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            [10, 20, 30, 40, 50],
            [60, 70, 80, 90, 100],
        ),
        ([1, 1, 1, 1, 1, 1], [1, 1, 1], [1, 1, 1]),
        ([5, 6, 7, 8, 9, 10, 11, 12, 13], [5, 6, 7, 8, 9], [10, 11, 12, 13]),
        ([4, 3, 2, 1, 0], [4, 3, 2], [1, 0]),
        ([1], [1], []),
        ([1, 1, 1, 1, 1], [1, 1, 1], [1, 1]),
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4], [5, 6, 7]),
        ([10, 20, 30, 40, 50, 60, 70], [10, 20, 30, 40], [50, 60, 70]),
        (
            [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
            [100, 200, 300, 400, 500],
            [600, 700, 800, 900, 1000],
        ),
        ([3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3]),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [9, 10, 11, 12, 13, 14, 15],
        ),
        ([2, 4, 6, 8, 10, 12], [2, 4, 6], [8, 10, 12]),
        ([11, 22, 33, 44, 55, 66, 77, 88], [11, 22, 33, 44], [55, 66, 77, 88]),
        ([100, 200], [100], [200]),
        ([1, 3, 5, 7, 9], [1, 3, 5], [7, 9]),
        ([2, 4, 6, 8, 10, 12, 14, 16], [2, 4, 6, 8], [10, 12, 14, 16]),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [1, 3, 5, 7, 9], [11, 13, 15, 17, 19]),
        ([2, 3, 5, 7, 11, 13, 17, 19], [2, 3, 5, 7], [11, 13, 17, 19]),
        ([3, 1, 4, 1, 5, 9, 2, 6], [3, 1, 4, 1], [5, 9, 2, 6]),
        ([8, 6, 7, 5, 3, 0, 9], [8, 6, 7, 5], [3, 0, 9]),
        ([2, 7, 1, 8, 2, 8, 1, 8, 2, 8], [2, 7, 1, 8, 2], [8, 1, 8, 2, 8]),
        ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], [3, 1, 4, 1, 5], [9, 2, 6, 5, 3]),
        (
            [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],
            [10, 20, 30, 40, 50, 60],
            [70, 80, 90, 100, 110, 120],
        ),
        ([5, 10, 15, 20, 25, 30], [5, 10, 15], [20, 25, 30]),
        ([12, 34, 56, 78, 90], [12, 34, 56], [78, 90]),
        ([21, 43, 65, 87, 109], [21, 43, 65], [87, 109]),
        ([7, 14, 21, 28, 35, 42, 49], [7, 14, 21, 28], [35, 42, 49]),
        ([1, 2, 4, 8, 16, 32], [1, 2, 4], [8, 16, 32]),
        ([9, 18, 27, 36, 45, 54, 63, 72], [9, 18, 27, 36], [45, 54, 63, 72]),
        ([3, 6, 9, 12, 15, 18], [3, 6, 9], [12, 15, 18]),
        ([1000, 2000, 3000, 4000], [1000, 2000], [3000, 4000]),
        ([100, 200, 300, 400, 500], [100, 200, 300], [400, 500]),
        ([2, 4, 6, 8, 10, 12, 14], [2, 4, 6, 8], [10, 12, 14]),
        ([11, 22, 33, 44], [11, 22], [33, 44]),
        ([1, 2, 3, 4, 5, 6], [1, 2, 3], [4, 5, 6]),
        ([10, 20, 30, 40, 50, 60], [10, 20, 30], [40, 50, 60]),
        ([5, 10, 15, 20], [5, 10], [15, 20]),
        ([1, 1, 2, 3, 5, 8, 13, 21, 34], [1, 1, 2, 3, 5], [8, 13, 21, 34]),
        ([7, 11, 13, 17, 19, 23, 29, 31], [7, 11, 13, 17], [19, 23, 29, 31]),
    ],
)
def test_split(elements, expected_list1, expected_list2):
    linked_list = SinglyLinkedList()
    for element in elements:
        linked_list.add_last(element)

    list1, list2 = linked_list.split()

    expected_linked_list1 = SinglyLinkedList()
    for element in expected_list1:
        expected_linked_list1.add_last(element)

    expected_linked_list2 = SinglyLinkedList()
    for element in expected_list2:
        expected_linked_list2.add_last(element)

    assert list1 == expected_linked_list1
    assert list2 == expected_linked_list2