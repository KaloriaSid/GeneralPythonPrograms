while True:
    row = input('Upto which row: ')
    try:
        row = int(row)
        spacing = row - 1
        for i in range(1, row + 1):
            print(' ' * spacing, end='')
            for j in range(i):
                print(i, end=' ')
            print()
            spacing -= 1
    except:
        print('Invalid input')
        quit()
