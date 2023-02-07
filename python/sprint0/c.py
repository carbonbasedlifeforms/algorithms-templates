from typing import List, Tuple

def moving_average(arr: List[int], window_size: int) -> List[float]:
    result = []
    curr_sum = sum(arr[0:window_size])
    result.append(curr_sum / window_size)
    for i in range(0,len(arr) - window_size):
        curr_sum -= arr[i]
        curr_sum += arr[i+window_size]
        curr_avg = curr_sum/window_size
        result.append(curr_avg)
    return result

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size

arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))
