# functions go here
def int_check(question, low, high):
    """"checks that users enter an integer that is more than 0 (or xxx exit code)"""

    error = f"Oops - please enter an integer."

    while True:

        try:
            # return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# main routine

# loop for testing purposes...
while True:
    print()

    # ask user for name
    name = input("Name: ")

    #  ask for age between 12 and 120
    age = int_check(f"Age:", 12, 120)

    # output error /success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")
