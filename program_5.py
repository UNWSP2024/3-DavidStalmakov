# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally, a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.
#David Stalmakov 9/18/2025 Hot Dog Calculator
Hot_Dog = 3.50
Chili_Dog = 4.50

# Add on prices
Cheese = 0.50
Peppers = 0.75
Onions = 1.00

tax_rate = 0.07

# Ask user for what kind of hot dog they want.
print("1. Hot Dog ($3.50)")
print("2. Chili Dog ($4.50)")
choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
    cost = Hot_Dog
elif choice == 2:
    cost = Chili_Dog

# Ask about add-ons
cheese = input("Do you want to add Cheese ($0.50)?: ").lower()=="yes"
peppers = input("Do you want to add Peppers ($0.75)?: ").lower()=="yes"
onions = input("Do you want to add Onions ($1.01)?: ").lower()=="yes"

if cheese:
    cost += Cheese
if peppers:
    cost += Peppers
if onions:
    cost += Onions

# Calculate tax and total
tax = cost * tax_rate
total = cost + tax

print( "Order Summery")
print(f"Hot Dog: ${cost:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
