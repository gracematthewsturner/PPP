# functions go here

loop = 0


def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")


def int_check(question, low, high):
    """checks that users enter an integer that is more than 0"""

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


def string_check(question, valid_ans_list=('yes', 'no'),
                 num_letters=1):
    """checks that users enter the full word
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


def instructions():
    make_statement("Instructions", "🧾")

    print('''

The menu will display all the pizzas we sell, a code for them, and their availability 
and price. To order a pizza, enter the code for the pizza that you want to order and then 
how many you would like to buy. Should you desire, you can add extra toppings or modifications to your 
pizza. You can order up to 5 pizzas.

You can pick up your order or have it delivered to your home. You can then pay with cash or credit at 
the place you receive your order.

''')


def menu():
    make_statement("Menu", "🍕")

    print(f'''
Code | Pizza | Type
1 | Pepperoni | Traditional($5) |
2 | Cheese |   
3 | Hawaiian |  
4 | Margarita |  
5 | Vege |  
6 | Chicken | Gourmet($10) |
7 | Chicken Again |  
8 | Artichoke |  
9 | Truffle |  
10 | Seafood |  
''')


def toppings_menu():
    print("")
    make_statement("Toppings", "🧂")

    print('''
Code | Name | Price
1 | Mayonnaise | $2 |
2 | Barbeque Sauce |
3 | Extra Cheese |
4 | Herbs | $3 |
5 | Sausage |
''')


print("")


def diet_menu():
    print("")
    make_statement("Dietary Requirements", "🌾")

    print('''
Code | Name | Price
1 | Gluten Free | $2 |
2 | Dairy Free |
3 | Vegetarian | $3 |
4 | Vegan | 
''')


print("")

price = 0
payment_ans = ['cash', 'credit']
collect_ans = ['delivery', 'pickup']

make_statement("Pizza Purchasing Program", "🍕")

print()
want_instructions = string_check("Would you like to view your instructions? ")

if want_instructions == "yes":
    instructions()

while loop < 5:
    print()

    menu()

    print()

    pizza = int_check("What is the code of the pizza you would like to order? ", 1, 10)
    if 1 < pizza <= 5:
        price += 5
    else:
        price += 10

    toppings_ask = string_check("Would you like to add toppings to this pizza? ")
    if toppings_ask == "yes":

        toppings_menu()

        toppings = int_check("What is the code of the toppings would you like to add to this pizza? ", 1, 5)
        if toppings <= 3:
            price += 2
        else:
            price += 3
    else:
        toppings = 0

    diet_ask = string_check("Would you like to specify any dietary requirements for this pizza?")
    if diet_ask == "yes":

        diet_menu()

        diet = int_check("What dietary requirement would you like to add to this pizza?", 1, 5)
        if diet <= 2:
            price += 2
        else:
            price += 3
    else:
        diet = 0

    loop += 1

    if loop < 5:
        do_loop = string_check("Would you like to add another pizza to your order? ")
        if do_loop == "no":
            break
    else:
        break

if loop == 5:
    print("You have added the maximum amount of pizzas (5) to your cart.")
else:
    if loop == 1:
        print(f"You have {loop} pizza in your cart.")
    else:
        print(f"You have {loop} pizzas in your cart.")

collect = string_check("Would you like to pick up your order or have it delivered to you? Delivery orders cost an "
                       "extra 10% surcharge ", collect_ans, 1)

if collect == "delivery":
    address = input("Where do you want us to deliver your order? ")
    surcharge = 1.1
    price = price * surcharge

name = not_blank("What is your name? ")

contact = not_blank("Please enter your email or phone number so we can contact you when your order is ready ")

pay_method = string_check(f"Your order costs ${price}. Will you be paying with cash or credit? ", payment_ans, 2)

print()
print("Thank you for ordering from the Pizza Purchasing Program. We will contact you when your order is ready ")
print()
