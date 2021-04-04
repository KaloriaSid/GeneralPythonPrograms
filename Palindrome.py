def checkPalindrome(checkString):
    length = len(checkString)
    flag = True
    for i in range(length // 2):
        if checkString[i] != checkString[length - 1]:
            flag = False
    if flag is True:
        print('Entered string is a palindrome.')
    else:
        print('Entered string is not palindrome.')


while True:
    string = input('Enter your input: ')

    if len(string) < 3:
        print('Not a palindrome')
    else:
        checkPalindrome(string)

    while True:
        check = input('Want to enter more(y/n): ')
        if check != 'y' and check != 'Y' and check != 'n' and check != 'N':
            print('Invalid Input')
        elif check == 'N' or check == 'n':
            quit()
        else:
            break
