"""
Author: Johnathan Price
Date: 9/1/2024
File Name: Price_lemonadeStand.py
Description: This program simulates a lemonade stand by calculating the cost of making lemonade and the profit from selling it.
"""

# Function to calculate the cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
    """
    This function calculates the total cost of making lemonade.
    Parameters:
    lemons_cost (float): The cost of lemons.
    sugar_cost (float): The cost of sugar.

    Returns:
    float: The total cost of making the lemonade.
    """
    total_cost = lemons_cost + sugar_cost  # Calculating the total cost
    return total_cost  # Returning the total cost

# Function to calculate the profit from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    """
    This function calculates the profit from selling lemonade.
    Parameters:
    lemons_cost (float): The cost of lemons.
    sugar_cost (float): The cost of sugar.
    selling_price (float): The selling price of the lemonade.

    Returns:
    float: The profit from selling the lemonade.
    """
    total_cost = calculate_cost(lemons_cost, sugar_cost)  # Reusing the calculate_cost function
    profit = selling_price - total_cost  # Calculating the profit
    return profit  # Returning the profit

# Variables for testing the functions
lemons_cost = 5.0  # Cost of lemons
sugar_cost = 3.0   # Cost of sugar
selling_price = 12.0  # Selling price of lemonade

# Building a string for the cost result
cost_result = f"({lemons_cost}) + ({sugar_cost}) = {calculate_cost(lemons_cost, sugar_cost)}"

# Building a string for the profit result
profit_result = f"Profit: {calculate_profit(lemons_cost, sugar_cost, selling_price)}"

# Printing the results to the console
print("Cost Calculation:")
print(cost_result)
print("\nProfit Calculation:")
print(profit_result)
