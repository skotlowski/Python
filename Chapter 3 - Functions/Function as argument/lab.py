def double(x):
    return 2 * x


def square(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


def generate_values(function_name, numbers: list) -> list:
    result = list()
    for x in numbers:
        result.append(f'The result of {function_name.__name__} for {x} is: {function_name(x)}')
    return result


x_table = list(range(11))

print(generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))
