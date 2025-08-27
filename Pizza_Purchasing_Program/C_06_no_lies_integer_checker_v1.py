# functions go here
def int_check(question):
    """"checks that users enter an integer"""

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
    name = input("Name: ")  # replace with call to not blank

    # ask for age between 12 and 120
    age = int_check("Age: ")

    # error or success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")
