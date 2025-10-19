# functions go here


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

        if num_letters == 1:
            print(f"Please reply with one of the following or its first letter: {valid_ans_list}")
        else:
            print(f"Please reply with one of the following or its first {num_letters} letters: {valid_ans_list}")


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
2 | Hawaiian |   
3 | Cheese |  
4 | Margarita |  
5 | Mushroom |  
6 | Chicken | Gourmet($10) |
7 | Many Meats |  
8 | Seafood |  
9 | Truffle |  
10 | Artichoke |  
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


def end_message():
    print()
    print("Thank you for using the Pizza Purchasing Program. Be sure to use it for future pizza orders")


print("")

order_again = "yes"
total_price = 0
price = 0
loop = 0
address = 0
final_cancel = "no"
# lists with valid answers for string check for pay method and way of order collection
payment_ans = ['cash', 'credit']
collect_ans = ['delivered', 'pickup']
order_ans = ['place', 'cancel']
# lists for cart
cart_pizza = []
pizza_price = []
cart_toppings = []
toppings_price = []
cart_diet = []
diet_price = []
delivery_surcharge = []
full_pizza_price_list = []

make_statement("Pizza Purchasing Program", "🍕")

# optional instructions for new users
print()
want_instructions = string_check("Would you like to view your instructions? ")

if want_instructions == "yes":
    instructions()

while order_again == "yes":
    # ask for order details until the user adds up to 5 pizzas
    while loop < 5:
        print()

        menu()

        print()

        # ask user for the flavour of pizza they would like to order
        pizza = int_check("What is the code of the pizza you would like to order? ", 1, 10)
        if 1 < pizza <= 5:
            pizza_price.append(5)
        else:
            pizza_price.append(10)
        cart_pizza.append(pizza)

        toppings_ask = string_check("Would you like to add toppings to this pizza? ")
        # if user wants toppings for this pizza, display the toppings menu and ask which one they want
        if toppings_ask == "yes":

            toppings_menu()

            # add topping price to total price depending on type of topping
            toppings = int_check("What is the code of the toppings would you like to add to this pizza? ", 1, 5)
            if toppings <= 3:
                toppings_price.append(2)
            else:
                toppings_price.append(3)
            cart_toppings.append(toppings)
        else:
            toppings = 0
            cart_toppings.append(0)
            toppings_price.append(0)

        diet_ask = string_check("Would you like to specify any dietary requirements for this pizza?")
        # ask user if they have any diet requirements and show available ones
        if diet_ask == "yes":

            diet_menu()
            # genetic dietary requirements are cheaper than chosen like vegetarian
            diet = int_check("What dietary requirement would you like to add to this pizza?", 1, 4)
            if diet <= 2:
                diet_price.append(2)
            else:
                diet_price.append(3)
            cart_diet.append(diet)
        else:
            diet = 0
            cart_diet.append(0)
            diet_price.append(0)

        loop += 1
        full_pizza_price = [sum(i) for i in zip(pizza_price, toppings_price, diet_price)]

        # ask user if they want to add another pizza to their cart
        if loop < 5:
            do_loop = string_check("Would you like to add another pizza to your order? ")
            # if they don't want another pizza, leave the loop
            if do_loop == "no":
                full_pizza_price_list.append(full_pizza_price)
                break
        else:
            full_pizza_price_list.append(full_pizza_price)
            break

    print()
    # inform the user of the amount of pizzas they have added. If they reach the max, tell them then continue
    if loop == 5:
        print("You have added the maximum amount of pizzas (5) to your cart.")
    else:
        if loop == 1:
            print(f"You have {loop} pizza in your cart.")
        else:
            print(f"You have {loop} pizzas in your cart.")

    price = sum(pizza_price) + sum(toppings_price) + sum(diet_price)
    print(f"Your order currently costs ${price:.2f}.")

    # check with user if they want to place or cancel their order
    cancel = string_check(f"Would you like to place or cancel your order? ", order_ans, 1)

    while final_cancel == "no":
        if cancel == "cancel":

            # double check that the user wants to cancel their order and cancel it
            final_cancel = string_check("Are you sure you want to cancel your order? ")

            if final_cancel == "yes":
                print("This order has been cancelled.")
                # ask user if they want to place another order
                break
            else:
                pass

        else:
            pass

        collect = string_check(
            f"Would you like to pick up your order or have it delivered to you? Delivery orders cost"
            f" an extra 10% surcharge which would change your total cost from ${price:.2f} to "
            f"${price * 1.1:.2f} ",
            collect_ans, 1)

        # apply surcharge to price and ask for address
        if collect == "delivered":
            address = not_blank("Where do you want us to deliver your order? ")
            surcharge = 1.1
            price *= surcharge
            delivery_surcharge.append(surcharge)
        if collect == "pickup":
            delivery_surcharge.append('NA')
        total_price = price

        # ask for users name, contact and payment method
        name = not_blank("What is your name? ")

        contact = not_blank(
            "Please enter your email or phone number so we can contact you when your order is ready ")

        if collect == "delivered":
            pay_method = string_check(f"Including the delivery fee, your order comes to a total cost of "
                                      f"${total_price:.2f}. "
                                      f"Will you be paying with cash or credit? ",
                                      payment_ans, 2)
        else:
            pay_method = string_check(f"In total, your order costs ${total_price:.2f}. Will you be paying with cash or "
                                      f"credit? ",
                                      payment_ans, 2)
        # users will pay with either method when they collect their order

        print()
        make_statement("Receipt", "💰")
        print()
        # order details
        if collect == "delivered":
            print(f"Delivery order for: {name}")
            print(f"Address: {address}")
        else:
            print(f"Pickup order for: {name}")
        print(f"Contact: {contact}")
        print()
        # cart details
        print(f"Pizza:{cart_pizza}")
        print(f"Toppings:{cart_toppings}")
        print(f"Dietary Requirements:{cart_diet}")
        print(f"Full Pizza Price: {full_pizza_price_list}")
        print(f"Delivery Surcharge:{delivery_surcharge}")
        print(f"Total Price: ${total_price:.2f}")

        # end order with friendly message
        print()
        print(
            "Thank you for ordering from the Pizza Purchasing Program. We will contact you when your order is "
            "ready ")
        final_cancel = "yes"

    # reset price and amount of pizzas in cart for another order
    price = 0
    total_price = 0
    loop = 0
    cart_pizza = []
    pizza_price = []
    cart_toppings = []
    toppings_price = []
    cart_diet = []
    diet_price = []
    delivery_surcharge = []
    full_pizza_price_list = []
    final_cancel = "no"
    print()
    order_again = string_check("Would you like to place another order? ")
    

end_message()
