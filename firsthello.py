# -----------------------------------------------------------------------------
# Name:        tip
# Purpose:     tip calculator
#
# Author:      Rula Khayrallah
# Date:        12/14/2016
# -----------------------------------------------------------------------------
"""
Tip calculator assuming a 20% tip rate

Prompt the user for the cost of their meal.
Print the tip amount and the total cost.
"""

TIP_RATE = 20 / 100                    # The tip rate constant: 20%

user_input = input('Please enter the cost of your meal in $: ')
cost = float(user_input)               # Convert the input string to a number

tip = TIP_RATE * cost                  # Calculate the tip amount
tip = round(tip, 2)                    # Round tip to two decimals

print('Tip Amount: $', tip, sep='')    # Suppress the space separator

total = cost + tip                     # The total cost of the meal
total = round(total, 2)                # Round total to two decimals

print('Total cost: $', total, sep='')  # Suppress the space separator


