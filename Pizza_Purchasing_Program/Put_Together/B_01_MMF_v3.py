import pandas
import random


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


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


def instructions():
    make_statement("Instructions", "🧾")

    print('''
    
For each ticket holder enter ...
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the 
ticket cost (and the profit).

Once you have either sold all of the tickets or entered the 
exit code ('xxx'), the program will display  the ticket
sales information and write the data to a text file.

It will also choose on lucky ticket holder who wins the
draw ( their ticket is free).

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

    error = f"Oops - please enter an integer."

    while True:

        try:
            # return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


def currency(x):
    """formats numbers as currency"""
    return "${:.2f}".format(x)


# main routine

# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

# initialise variables / non default options for string checker
payment_ans = ('cash', 'credit')

# ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# credit surcharge of 5%
CREDIT_SURCHARGE = 0.05

# lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}

# program main heading
make_statement("Mini-Movie Fundraiser Program", "🍿")

# ask user if they want to see instructions
# display them if necessary
print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

# loop to get name age and payment details
while tickets_sold < MAX_TICKETS:
    # ask user for name and check it's not blank
    print()
    name = not_blank("Name: ")

    # if name is exit code, break out of loop
    if name == "xxx":
        break

    # ask for age and check it's between 12 and 120
    age = int_check("Age: ")

    # output error or success message
    if age < 12:
        print(f"{name} is too young")
        continue

    # child ticket price is 7.50
    elif age < 16:
        ticket_price = CHILD_PRICE

    # adult ticket 10.5
    elif age < 65:
        ticket_price = ADULT_PRICE

    # senior price 6.5
    elif age < 121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    # ask for payment method
    pay_method = string_check("Payment method: ", payment_ans, 2)

    if pay_method == "cash":
        surcharge = 0

    # if paying by credit calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # add name, ticket cost and surcharge
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

    tickets_sold += 1

# end of ticket loop

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate the total payable for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# work out total paid and profit
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# choose random winner
winner = random.choice(all_names)

# find index / position of winner
winner_index = all_names.index(winner)
print("winner", winner, "list position", winner_index)

# retrieve winner ticket price and profit ( so we can adjust
# profit numbers so that the winning ticket is excluded)
ticket_won = mini_movie_frame.at[winner_index, 'Total']
profit_won = mini_movie_frame.at[winner_index, 'Profit']

# currency format (use currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# output movie frame without index
print(mini_movie_frame.to_string(index=False))

print()
print(f"Total Paid: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")

# winner announcement
print(f"The lucky winner is {winner}. Their ticket worth {ticket_won} is free!")
print(f"Total Paid is now ${total_paid - ticket_won:.2f}")
print(f"Total Profit is now ${total_profit - profit_won:.2f}")

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all of the tickets (ie: {MAX_TICKETS} tickets)")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets.")
