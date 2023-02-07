def to_binary(number: int) -> str:
    if number == 0:
        return str(number)
    result_bin = ""
    while number > 0:
        if number % 2 == 0:
            result_bin += "0"
            number //= 2
        elif number % 2 == 1:
            result_bin += "1"
            number //= 2
    return str(result_bin[::-1])  

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))
