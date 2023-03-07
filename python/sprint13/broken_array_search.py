# sprint 13 A.Поиск в сломанном массиве
# ID: 83522076
from typing import List


def broken_search(nums: List[int], target: int) -> int:
    low_idx: int = 0
    high_idx: int = len(nums) - 1
    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx) // 2
        curr_item = nums[mid_idx]
        low_item = nums[low_idx]
        high_item = nums[high_idx]
        if curr_item == target:
            return mid_idx
        if curr_item >= low_item:
            if curr_item > target >= low_item:
                high_idx = mid_idx - 1
            else:
                low_idx = mid_idx + 1
        else:
            if curr_item < target <= high_item:
                low_idx = mid_idx + 1
            else:
                high_idx = mid_idx - 1
    return -1


if __name__ == '__main__':
    length_arr = int(input())
    target = int(input())
    nums = [int(num) for num in input().split()]
    print(broken_search(nums, target))
