# 11 спринт, задача: Ловкость рук
# id: 81925481
from collections import Counter
from typing import Tuple

def points_counting(taps: int, conc_str: str, gamers: int = 2) -> int:
    keys = Counter(conc_str)
    win_condition = taps * gamers
    win_points = sum(
        [1 for key, value in keys.items() if value <= win_condition and key.isdigit()]
    )
    return win_points

if __name__ == '__main__':
   
    def read_input() -> Tuple[int, str]:
        taps = int(input())
        conc_str = ''
        for str_num in range(4):
            conc_str += str(input())
        return taps, conc_str
    
    taps, conc_str = read_input()
    print(points_counting(taps, conc_str))
