def is_odd(num: int) -> int:
    if num % 2 == 0:
        return 1
    return 2

def check_parity(a: int, b: int, c: int) -> bool:
    return is_odd(a) == is_odd(b) == is_odd(c)

def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")

a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
