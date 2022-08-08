from TwoSum import twoSum


def test_1_twoSum():
    actual = twoSum([2, 7, 11, 15], 9)
    expected = [0, 1]
    assert actual == expected


def test_2_twoSum():
    actual = twoSum([3, 2, 4], 6)
    expected = [1, 2]
    assert actual == expected


def test_3_twoSum():
    actual = twoSum([3, 3], 6)
    expected = [0, 1]
    assert actual == expected


def test_4_twoSum():
    actual = twoSum([3, 2, 3], 6)
    expected = [0, 2]
    assert actual == expected
