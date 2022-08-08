from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for index, number in enumerate(nums):
        if target - number in num_dict:
            return [num_dict[target - number], index]
        elif number not in num_dict:
            num_dict[number] = index



