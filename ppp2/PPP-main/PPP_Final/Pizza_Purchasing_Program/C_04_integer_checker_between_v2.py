# functions go here
def int_check(question, low, high):
    """"checks that users enter an integer that is more than 0 (or xxx exit code)"""

    error = f"Oops - please enter an integer between {low} and {high}."

    while True:

        try:
            # change response to an integer to check it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine

# loop for testing purposes...
while True:
    print()

    # ask user for integer
    my_num = int_check("Choose a number: ", 1, 10)
    print(f"You chose {my_num}")
