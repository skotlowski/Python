import os


def read_text_file(file_path: str) -> int:
    with open(file_path, encoding='utf-8') as file:
        output = file.read().split()
        return len(output)

path = r'C:\repositories\Python\Chapter 1 - Variables and code\Boolean operations\txt_file.txt'

if os.path.isfile(path):
    print(f'Words in file: {read_text_file(path)}')

os.path.isfile(path) and print(f'Words in file: {read_text_file(path)}')
