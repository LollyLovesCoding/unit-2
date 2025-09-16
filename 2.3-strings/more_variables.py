store = "Tim Hortons"
item = "Coffee"
price = 3
quantity = 5
subtotal = price * quantity
tax = subtotal * 0.05
total = tax + subtotal

# f-string
print(f"At {store} I bought some {item}.")
# concatenation
print("They sold for $" + str(price) + " each.")
# "dot format"
print("I wanted to purchase {} of them.".format(quantity))
# Subtotal is the price times the quantity which is 0.5 * 7 = $3.5
# Tax 5% of the subtotal which is 3.5 * 0.05 = $0.175
# f-string
print(f"The total price, with tax included, was ${total}.")
