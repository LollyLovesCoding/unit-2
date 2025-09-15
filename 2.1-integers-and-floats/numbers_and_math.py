print("I have a class of 33 students.")
print("There are 11 girls, so that means..")
# Takes the number of the total students and subtracts the number by the number of girls to get the number of boys
print(f"there are {str(33 - 11)} boys.")
print()

# Divides the number of girls by the total to get the percentage of girls
print(f"That means {round(11 / 33, 2)} % are girls...")
# Divides the number of boys by the total to get the percentage of boys
print(f"and {round(((33 - 11) / 33), 2)} % are boys.")
print("If we made groups of six...")
# Floors the division of the total divided by 6 to get an integer amount of groups
print(f"There would be {33 // 6} groups of six.")
# Takes the remainder of the total divided by 6 to see the amount of people left over
print(f"And then a smaller group of {33 % 6} people.")
# Prints the symbol "-" 30 times
print("-" * 30)

print("If we had 17 apples and 3 people...")
# Floors the division of total apples divided by the number of people
print(f"Each person would get {17 // 3} whole apples.")
# Takes the remainder of total apples divided by the number of people to see the apples remaining
print(f"There would be {str(17 % 3)} apples remaining.")
print()

print("If we charged each person $2 each for their 5 apples..")
# Calculates the amount of money each person has to pay by multiplying price with amount
print(f"they would each pay ${2 * 5}.")
