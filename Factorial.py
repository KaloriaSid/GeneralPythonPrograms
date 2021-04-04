def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


while True:
    num = input('Enter your number: ')
    try:
        num = int(num)
        print(fact(num))
    except:
        print('Invalid input')

    while True:
        check = input('Want to enter more(y/n): ')
        if check != 'y' and check != 'Y' and check != 'n' and check != 'N':
            print('Invalid Input')
        elif check == 'N' or check == 'n':
            quit()
        else:
            break
