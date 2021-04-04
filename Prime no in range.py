while True:
    try:
        upp = input('Enter upper value: ')
        upp = int(upp)
        low = input('Enter lower value: ')
        low = int(low)
        for num in range(low, upp+1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                    else:
                        print(num, end='  ')
                        break
        print()
    except:
        print('Invalid Input')
        quit()
