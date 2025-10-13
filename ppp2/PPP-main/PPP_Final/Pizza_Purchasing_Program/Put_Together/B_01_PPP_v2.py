# Functions go here
import random

MIN = 0
MAX = 0


def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_ans_list=('yes', 'y', 'no', 'n'),
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

        print(f"Please enter one of the following: {valid_ans_list}")


def instructions():
    make_statement("Instructions", "🧾")

    print('''
    
The menu will display all the pizzas we sell, a code for them, and their availability 
and price. To order a pizza, enter the code for the pizza that you want to order and then 
how many you would like to buy. Should you desire, you can add extra toppings or modifications to your 
pizza. 

You can pick up your order or have it delivered to your home. You can then pay with cash or credit at 
the place you receive your order.

To cancel an order, enter "xxx".

''')


def menu():
    make_statement("Menu", "🍕")

    print(f'''
Code Pizza Price Availability

1 | Pepperoni | $5 | {random.randint(1, 5)}
2 | Cheese | $5 | {random.randint(1, 5)}
3 | Hawaiian | $5 | {random.randint(1, 5)}
4 | Margarita | $5 | {random.randint(1, 5)}
5 | Vegetarian | $5 | {random.randint(1, 5)}
6 | Chicken | $10 | {random.randint(1, 5)}
7 | Chicken Again | $10 | {random.randint(1, 5)}
8 | Artichoke | $10 | {random.randint(1, 5)}
9 | Truffle | $15 | {random.randint(1, 5)}
10 | Seafood | $15 | {random.randint(1, 5)}
''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")


def int_check(question):
    """"checks that users enter an integer that is more than 0 (or xxx exit code)"""

    error = f"Please enter an integer between {MIN} and {MAX}."

    while True:

        try:
            # return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# main routine

# Initialise ticket numbers
MAX_PIZZAS = 5
pizzas_sold = 0

# initialise variables / non default options for string checker
payment_ans = ['cash', 'credit']

make_statement("Pizza Purchasing Program", "🍕")

print()
want_instructions = string_check("Would you like to view your instructions? ")

if want_instructions == "yes":
    instructions()

print()

menu()

print()

while pizzas_sold < MAX_PIZZAS:

    MIN = 1
    MAX = 10

    # ask user for name and check it's not blank
    print()
    code = int_check("What is the code of the pizza you would like to order? ")

    # output error or success message
    if MIN < code < MAX:
        continue
    elif MAX < code or code < MIN:
        print(f"Please enter an available pizza code between {MIN} and {MAX}.")
        continue
    else:
        pass

    # if name is exit code, break out of loop
    if pizzas_sold == "xxx":
        break

    # ask for payment method
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"{name} bought a ticket ({pay_method})")

    pizzas_sold += 1

if pizzas_sold == MAX_PIZZAS:
    print(f"You have placed a maximum capacity order of {MAX_PIZZAS} pizzas.")
else:
    print(f"You have sold {pizzas_sold} / {MAX_PIZZAS} tickets.")
