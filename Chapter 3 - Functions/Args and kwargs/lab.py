def calculate_paint(efficency_ltr_per_m2: int, *rooms_space: int) -> int:
    return sum(rooms_space)*efficency_ltr_per_m2


print(calculate_paint(2, 10, 20, 10))

list_of_rooms = [10, 20, 10]
print(calculate_paint(2, *list_of_rooms))


def log_it(path: str, *args: str) -> None:
    with open(path, 'a') as f:
        for arg in args:
            f.write(f'{arg} ')
        f.write('\n')

log_dir = r'C:\repositories\Python\Chapter 3 - Functions\Args and kwargs\log.txt'
log_it(log_dir, 'Starting processing forecasting')
log_it(log_dir, 'ERROR', 'Not enough data', 'invoices', '2020')
