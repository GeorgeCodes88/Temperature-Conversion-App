
temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

conversion_factor = 9/5

if unit.upper() == "C":
    converted_temp = (temp * conversion_factor) + 32
    unit = "F"
    print(f"Your Converted Temperature in {unit} is: {converted_temp:.2f}")
elif unit.upper() == "F":
    converted_temp = (temp - 32) / conversion_factor
    unit = "C"
    print(f"Your Converted Temperature in {unit} is: {converted_temp:.2f}")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")