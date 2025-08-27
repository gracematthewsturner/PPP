# functions go here
def string_check(question, valid_ans_list):
    """"checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check  if response is full word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# main routine goes here
levels = ['easy', 'medium', 'hard']

like_coffee = string_check("Do you like coffee? ", ['yes', 'no'])
choose_level = string_check("Choose a level: ", levels)
