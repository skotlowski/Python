from os.path import basename

files_to_process = [
    r"C:\repositories\Python\Chapter 2 - code\Exec\math_sin_square.py",
    r"C:\repositories\Python\Chapter 2 - code\Exec\math_square_root.py"]

for script in files_to_process:
    print(basename(script))

    with open(script, 'r') as f:
        source = f.read()

    exec(source)
