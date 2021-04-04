nums = []
largest = None
while True:
    for i in range(3):
        print("Enter", i+1, "value: ", end='')
        k = input()
        try:
            k = int(k)
            nums.append(k)
        except:
            print('Invalid Input')
            quit()
    for num in nums:
        if largest is None or num > largest:
            largest = num
    print('Largest number is: ', largest)
