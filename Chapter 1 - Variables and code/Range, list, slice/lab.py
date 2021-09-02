def generate_colors(colors: list, n: int) -> list:
    return colors[:n]


list_of_colors = ["red", "orange", "green", "violet", "blue", "yellow"]

print(generate_colors(colors=list_of_colors, n=4))

for i in range(len(list_of_colors)):
    print(generate_colors(list_of_colors, i+1))

random_string = "Hello World"
print(random_string[0:-5])

