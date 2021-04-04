while True:
    num = input('Enter number: ')
    try:
        num = int(num)
        reverse = 0
        while num > 0:
            remainder = num % 10
            reverse = reverse * 10 + remainder
            num = num // 10
        print('Reversal is: ', reverse)
    except:
        print('Invalid Input')
        quit()
