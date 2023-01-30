print("Welcome to the best calculator ever!")
print("Would you like to: ")
print("1 mathematical expressions")
print("2 Input some numbers and the program will give you the give the biggest and the smallest")
choice = int(input())

if choice == 1:
    print("You chose mathematical expressions")
    print("Enter num1 and num2")
    numA = int(input())
    numB = int(input())
    print(f'What do you want to do with {numA} and {numB}?')
    print(f'1   {numA} + {numB}')
    print(f'2   {numA} - {numB}')
    print(f'3   {numA} * {numB}')
    print(f'4   {numA} / {numB}')
    print(f'5   {numA} ^ {numB}')
    print("6    All")
    choice = int(input())


    def addition():
        result = numA + numB
        print(f'The result of {numA} plus {numB} is {result}')


    def subtraction():
        result = numA - numB
        print(f'The result of {numA} minus {numB} is {result}')


    def multiplication():
        result = numA * numB
        print(f'The result of {numA} multiplied {numB} is {result}')


    def division():
        result = numA / numB
        print(f'The result of {numA} divided by {numB} is {result}')


    def power():
        result = numA ** numB
        print(f'The result of {numA} to the power of {numB} is  {result}')


    if choice == 1:
        addition()
    elif choice == 2:
        subtraction()
    elif choice == 3:
        multiplication()
    elif choice == 4:
        division()
    elif choice == 5:
        power()
    elif choice == 6:
        addition()
        subtraction()
        multiplication()
        division()
        power()

elif choice == 2:
    print("You chose min max")
    print("Please input 2 or more numbers seperated by spaces")
    numbers = input().split()
    numbers.sort()
    print(f'Smallest number is: {numbers[0]}')
    numbers.sort(reverse=True)
    print(f'Biggest number is: {numbers[0]}')
