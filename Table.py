while True:
    num = input('Enter number: ')
    try:
        num = int(num)
        for i in range(1,11):
            print(num, 'x', i, '=', num * i)
    except:
        print('Invalid Input')
        quit()
