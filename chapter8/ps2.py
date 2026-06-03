# temperature covterion using functions Fahrenheit (°F) to Celsius (°C)

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter a temperature in Fahrenheit (°F) : "))

print(f"{f} Fahrenheit to Celsius is {round(f_to_c(f), 2)} °C" )

# print(f_to_c(f))