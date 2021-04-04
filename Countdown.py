while True:
    num = input('Enter number: ')
    try:
        num = int(num)
        while num >= 0:
            print(num)
            num -= 1
    except:
        print('Invalid Input')
        quit()
