
def isPalindrome(x: int) -> bool:
    if str(x)[::-1] == str(x):
        return True
    return False


print(isPalindrome(121))
print(isPalindrome(-121))
