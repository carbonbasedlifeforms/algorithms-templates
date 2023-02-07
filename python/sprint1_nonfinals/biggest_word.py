line = 'my name is null'
# line_len = dict()
split_lines = line.split()
biggest_word = max(split_lines, key=len)
# for item in list(split_lines):
#     line_len[] = item, len(item)
print(f'{biggest_word}\n{len(biggest_word)}')