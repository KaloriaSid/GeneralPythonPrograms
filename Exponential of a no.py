while True:
    num = input('Enter number: ')
    try:
        num = int(num)
        print(num ** num)
    except:
        print('Invalid Input')
        quit()
