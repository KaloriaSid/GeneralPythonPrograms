while True:
    num = input('Enter the number: ')
    try:
        num = int(num)
        if num is None:
            break
        if num % 2 == 0:
            print('Even')
        else:
            print('Odd')
    except:
        print('Invalid Input')
        quit()
