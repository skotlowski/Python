def print_value_and_id(*args):
    for item in args:
        print(f'value: {item}')
        print(f'id: {id(item)}')


a, b, c = 10, 10, 10

print_value_and_id(a, b, c)

a = 20

print_value_and_id(a, b, c)

lista = [1, 2, 3]
a, b, c = lista, lista, lista

a.append(4)

print_value_and_id(a, b, c)

x = 10
y = 10

y = y + 1 - 1

print_value_and_id(x, y)

y = y + 1234567890 - 1234567890

print_value_and_id(x, y)
