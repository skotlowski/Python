def run():
    options = ['load data', 'export data', 'analyze & predict']
    choice = input()
    try:
        choice = int(choice)
    except:
        print("Your choice is not an int")
    else:
        if 1 <= choice <= 3:
            print(f'Your choice: {options[choice-1]}')
        else:
            print("Wrong number")


if __name__ == '__main__':
    print('''Choose:
1.load data
2.export data
3.analyze & predict''')
    run()






