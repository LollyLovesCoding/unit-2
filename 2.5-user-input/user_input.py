print("Enter the following information about an item you wish to purchase..\n")

# One difference between name and price is how they were formatted in the code, although they displayed the exact same thing.
# The second difference is that the price is converted to a float type number.
name = input("The name of the item: ")

# int() and float() functions are used to convert input into the specified number type so multiplying the number by another float is possible.
# If I remove the function, I will get a TypeError
price = float(input("The price: $"))

quantity = int(input("How many do you want? "))

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print(f"\nYou choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")

# There is an issue with this prompt because the question is asked after the prompt is issued.
# name = input()
# print("Enter the name of the item:")
