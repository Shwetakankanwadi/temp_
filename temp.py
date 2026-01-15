def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def main():
    try:
        temp_c = float(input("Enter temperature in Celsius: "))
        temp_f = celsius_to_fahrenheit(temp_c)
        print("Temperature in Fahrenheit:", temp_f)
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
