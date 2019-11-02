#declare variables
largest = None
smallest = None

#get input from user
while True:
    user_input = input('Enter a number: ')

    #check is user input done
    if user_input == 'done':
        break

    try:
        user_input = int(user_input)
    except Exception as e:
        print('Invalid input')
        continue

    #check for largest number
    if largest is None:
        largest = user_input
    elif largest < user_input:
        largest = user_input

    #check for smallest number
    if smallest is None:
        smallest = user_input
    elif smallest > user_input:
        smallest = user_input

print('Maximum is',largest)
print('Minimum is',smallest)
