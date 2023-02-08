# 11 спринт, задача: Ловкость рук
# id: 82012855
from collections import Counter
from typing import Tuple


def points_counting(taps: int, conc_str: str, gamers: int = 2) -> int:
    keys = Counter(conc_str.replace('.', ''))
    win_condition = taps * gamers
    win_points = sum(
        [value <= win_condition for key, value in keys.items()]
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
