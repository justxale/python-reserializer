with open('test.jaon') as f:
    while line := f.readline().rstrip():
        print(line)
        break
