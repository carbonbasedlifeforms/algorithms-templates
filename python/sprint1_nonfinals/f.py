import re

def is_palindrome(line: str) -> bool:
    prep_line = re.sub("[^a-z0-9]", "", line.lower())
    if prep_line == "":
        return False
    return prep_line == prep_line[::-1]
    # if prep_line == prep_line[::-1]:
    #     return True
    # return False

print(is_palindrome(input().strip()))
