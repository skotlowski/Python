def show_progress(how_many: int, character: str = '*') -> None:
    print(how_many * character)


show_progress(10)
show_progress(20, '-')
show_progress(character='^', how_many=15)
