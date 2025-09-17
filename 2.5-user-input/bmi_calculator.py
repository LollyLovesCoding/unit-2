input("Height (feet only): ")
height = float(input("Height (inches): "))
weight = float(input("Weight in pounds: "))

height_in_m = round((height / 39.37), 2)
weight_in_kg = int(weight / 2.205)

print(f"Height in m: {height_in_m}")
print(f"Weight in kg: {weight_in_kg}")

bmi = round(weight_in_kg / height_in_m / height_in_m, 6)
print(f"The BMI is {bmi}")
