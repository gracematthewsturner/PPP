# functions go here
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


# main routine goes here
# payment_ans = ['cash', 'credit']
while True:
    want_instructions = string_check("Do you want to see the instructions?")
    print(f"You chose {want_instructions}")
    print()
# pay_method = string_check("Payment method", payment_ans, 2)
# print(f"You chose {pay_method}")
