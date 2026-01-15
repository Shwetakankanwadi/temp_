def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


if _name_ == "_main_":
    temp_c = 32.0  
    temp_f = celsius_to_fahrenheit(temp_c)
    print("Temperature in Fahrenheit:", temp_f)
