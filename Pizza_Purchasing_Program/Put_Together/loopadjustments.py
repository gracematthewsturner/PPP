# functions go here
loop = 0


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


def collect_check(question, valid_ans_list=('pickup', 'delivery'),
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


while loop < 5:

    all_pizza = []
    all_price = []
    all_toppings = []
    all_diet = []

    mini_movie_dict = {
        'Pizza': all_pizza,
        'Toppings': all_toppings,
        'Diet': all_diet,
        'Price': all_price
    }

    pizza = int_check("What is the code of the pizza you would like to order? ", 1, 10)
    if 1 < pizza <= 5:
        price = 5
    else:
        price = 10

    toppings_ask = string_check("Would you like to add toppings to this pizza? ")
    if toppings_ask == "yes":
        print("Code | Name | Price"
              "1 | Mayonnaise | $2"
              "2 |"
              "3 |"
              "4 |"
              "5 |")

        toppings = int_check("What is the code of the toppings would you like to add to this pizza? ", 1, 5)
        if toppings <= 3:
            price += 2
        else:
            price += 3

    diet_ask = string_check("Would you like to specify any dietary requirements for this pizza?")
    if diet_ask == "yes":
        diet = int_check("What dietary requirement would you like to add to this pizza?", 1, 5)

    all_pizza.append(pizza)
    all_price.append(price)
    all_toppings.append(toppings)
    all_diet.append(diet)

    do_loop = string_check("Would you like to order another pizza?")

    if do_loop == "no":
        break

    print(mini_movie_dict)

    loop += 1

collect = collect_check("Would you like to pick up your order or have it delivered to you? Delivery orders cost an "
                        "extra 10% surcharge ")
if collect == "delivery":
    address = input("Where do you want us to deliver your order? ")


print("end")
