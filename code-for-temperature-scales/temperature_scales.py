# Import temperature module
import temperature

# Convert 32 degrees Celsius to Fahrenheit
celsius = 32
fahrenheit = temperature.celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius = {fahrenheit} degrees Fahrenheit")

# Convert 80 degrees Fahrenheit to Celsius
fahrenheit = 80
celsius = temperature.fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} degrees Fahrenheit = {celsius} degrees Celsius")

# Convert 298 Kelvin to Celsius
kelvin = 298
celsius = temperature.kelvin_to_celsius(kelvin)
print(f"{kelvin} Kelvin = {celsius} degrees Celsius")
