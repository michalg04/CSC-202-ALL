# -----------------------------------------------------------------------------
# Name:        tax
# Purpose:     tax calculator
#
# Author:      Michal Golovanevsky
# Date:        07/05/2017
# -----------------------------------------------------------------------------
"""
Tax calculator assuming a sales tax rate of 8.75% (Los Altos Hills, CA 2017)

Prompts the user for the cost of the product.
Prints the tax amount the the total cost.
"""

TAX_RATE = 8.75 / 100                    # The tax rate constant: 8.75%

user_input = input('Please enter the price in $: ')
cost = float(user_input)               # Converts the input string to a number

tax = TAX_RATE * cost                  # Calculates the tax amount
tax = round(tax, 2)                    # Rounds tax amount to two decimals

print('Sales Tax: $', tax, sep='')    # Suppresses the space separator

total = cost + tax                     # The total cost of product
total = round(total, 2)                # Rounds total to two decimals

print('Total cost: $', total, sep='')  # Suppresses the space separator
