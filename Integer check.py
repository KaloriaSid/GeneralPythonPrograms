while True:
    check = input('Enter: ')
    try:
        check = int(check)
        print('Integer value')
    except:
        print('Not a integer value')
        quit()
