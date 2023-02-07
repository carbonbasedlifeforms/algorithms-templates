def get_longest_word(line: str) -> str:
    split_lines = line.split()
    biggest_word = max(split_lines, key=len)
    return biggest_word    

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))
