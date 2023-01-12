import functions


while True:
    user_action = input("Would you like to add, multiply, subtract or divide? ")

    if user_action in('add', 'multiply','subtract','divide'):
        num_1 = float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: "))


    if user_action == 'add':
       added = functions.add(num_1, num_2)
       print(added)
       

    elif user_action == 'multiply':
        multiply = functions.multiply(num_1,num_2)
        print(multiply)
    
    elif user_action == 'divide':
        divided = functions.divide(num_1,num_2)
        print(divided)
    
    elif user_action == 'subtract':
        subtracted = functions.subtract(num_1,num_2)
        print(subtracted)

    else:
        print("Please enter a number")
