while True:
    num = input('Enter number: ')
    try:
        num = int(num)
        print(float(1/num))
    except:
        print('Invalid Input')
        quit()
