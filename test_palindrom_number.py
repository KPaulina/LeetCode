from palindrom_number import isPalindrome


def test_isPalindrom_1():
    actual = isPalindrome(121)
    expected = True
    return actual == expected


def test_isPalindrom_2():
    actual =isPalindrome(-121)
    expected = False
    return actual == expected
