# functions
def int_check(question):
    """"checks that users enter an integer that is more than 0 (or xxx exit code)"""

    error = f"Oops - please enter an integer."

    while True:

        try:
            # return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")


def string_check(question, valid_ans_list=('yes', 'no'),
                 num_letters=1):
    """"checks that users enter the full word
    or the n letters of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check  if response is full word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# main routine

# initialise variables / non default options for string checker
payment_ans = ['cash', 'credit']

# loop for test
while True:
    print()

    # ask user for name and check it's not blank
    name = not_blank("Name: ")

    # ask for age and check it's between 12 and 120
    age = int_check("Age: ")

    # output error or success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

    # ask for payment method
    pay_method = string_check("Payment method", payment_ans, 2)
    print(f"You chose {pay_method}")
