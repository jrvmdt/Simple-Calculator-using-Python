def operation():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Pili ka kung ano want mo: ")

    if choice == '1':
        print("You chose Addition.")
        num1 = int(input("Input the first no. "))
        num2 = int(input("Input the second no. "))
        sum = num1 + num2
        print("The sum of the two numbers is", sum)
        repeat()

    elif choice == '2':
        print("You chose Subtraction.")
        num3 = int(input("Input the first no. "))
        num4 = int(input("Input the second no. "))
        diff = num3 - num4
        print("The difference of the two numbers is", diff)
        repeat()

    elif choice == '3':
        print("You chose Multiplication.")
        num5 = int(input("Input the first no. "))
        num6 = int(input("Input the second no. "))
        prod = num5 * num6
        print("The product of the two numbers is", prod)
        repeat()

    elif choice == '4':
        print("You chose Division.")
        num7 = int(input("Input the first no. "))
        num8 = int(input("Input the second no. "))
        quo = num7 / num8
        print("The difference of the two numbers is", quo)
        repeat()
    else:
        print("Wala don tanga.")
        repeat()


def repeat():
    while True:
        answer = input("Do you want to continue? (y/n): ")
        if answer.lower() == "y":
            print("Okay, let's continue!")
            operation()
        elif answer.lower() == "n":
            print("Okay, exiting now.")
            break
        else:
            print("Sorry, I didn't understand that. Please enter 'y' or 'n'.")

operation()