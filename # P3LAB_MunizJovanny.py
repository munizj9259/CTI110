# P3LAB_MunizJovanny
# This program calculates the number of dollars, quarters, dimes, nickels, and pennies
# needed for a given amount of money.

# Get user input
amount = float(input("Enter the amount of money: "))

# Convert dollars to cents to avoid floating point issues
cents = int(round(amount * 100))

# Calculate each coin
dollars = cents // 100
cents = cents % 100

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5

pennies = cents

# Output results
if dollars > 0:
    print(f"{dollars} dollar" if dollars == 1 else f"{dollars} dollars")

if quarters > 0:
    print(f"{quarters} quarter" if quarters == 1 else f"{quarters} quarters")

if dimes > 0:
    print(f"{dimes} dime" if dimes == 1 else f"{dimes} dimes")

if nickels > 0:
    print(f"{nickels} nickel" if nickels == 1 else f"{nickels} nickels")

if pennies > 0:
    print(f"{pennies} penny" if pennies == 1 else f"{pennies} pennies")