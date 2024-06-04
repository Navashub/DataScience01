"""
Python Syntax Challenge

You have been hired to develop a simple temperature conversion tool. This tool will convert a given temperature from Celsius to Fahrenheit and vice versa.

Instructions:
1. Open a new file in your Python development environment or IDE.
2. Begin by typing the line 'Welcome to Temperature Converter' which will display a welcome message when the code is run.
3. Add a line that prompts the user to choose a conversion type using the input() function and store the user's input in a variable named 'conversion_type'. The user should enter 'C to F' for Celsius to Fahrenheit or 'F to C' for Fahrenheit to Celsius.
4. Add a line that prompts the user to enter the temperature value they want to convert using the input() function and store the user's input in a variable named 'temperature'.
5. Convert the temperature to a float type.
6. Based on the user's choice of conversion type, perform the appropriate temperature conversion:
    - If the user chooses 'C to F', use the formula \(F = \frac{9}{5} \times C + 32\).
    - If the user chooses 'F to C', use the formula \(C = \frac{5}{9} \times (F - 32)\).
7. Print the converted temperature to the console.
8. Check your code for any syntax errors or mistakes.
9. Run the code and test it by providing inputs for conversion_type and temperature"""

print("Welcome to Temperature Converter")

conversion_type = input("choose your conversion type: 'F to C' or 'C to F' ")


if conversion_type == 'F to C' or conversion_type == 'f to c':
    temperature = float(input("Enter the Fahrenheit temperature you want to convert: "))
    temperature_in_celcius = (temperature - 32) * (5/9)
    # print(str(temperature_in_celcius) + "°C")
    print(f"{temperature_in_celcius} °C")

elif conversion_type == 'C to F' or conversion_type == 'c to f':
    temperature = float(input("Enter the Celcius temperature you want to convert: "))
    temperature_in_Fahrenheit = (temperature * 9/5) + 32   
    print(str(temperature_in_Fahrenheit) + "Fahrenheit")
    # print(f"{temperature_in_Fahrenheit} F")
else:
    print("Invalid choice")


