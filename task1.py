def convert_length():
    print("\n--- Length Converter ---")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    choice = input("Choose option (1 or 2): ")
    
    try:
        val = float(input("Enter value: "))                        
        if choice == '1':
            result = val * 3.28084
            print(f"--> {val} meters = {result:.2f} feet\n")
        elif choice == '2':
            result = val / 3.28084
            print(f"--> {val} feet = {result:.2f} meters\n")
        else:
            print("Invalid conversion choice.\n")
    except ValueError:
        print("Error: Please enter a valid numerical value.\n")


def convert_weight():
    print("\n--- Weight Converter ---")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose option (1 or 2): ")
    
    try:
        val = float(input("Enter value: "))
        if choice == '1':
            result = val * 2.20462
            print(f"--> {val} kg = {result:.2f} lbs\n")
        elif choice == '2':
            result = val / 2.20462
            print(f"--> {val} lbs = {result:.2f} kg\n")
        else:
            print("Invalid conversion choice.\n")
    except ValueError:
        print("Error: Please enter a valid numerical value.\n")


def convert_temperature():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose option (1 or 2): ")
    
    try:
        val = float(input("Enter value: "))
        if choice == '1':
            result = (val * 9/5) + 32
            print(f"--> {val}°C = {result:.2f}°F\n")
        elif choice == '2':
            result = (val - 32) * 5/9
            print(f"--> {val}°F = {result:.2f}°C\n")
        else:
            print("Invalid conversion choice.\n")
    except ValueError:
        print("Error: Please enter a valid numerical value.\n")


def main():
    while True:
        print("==============================")
        print("      UNIT CONVERTER CLI      ")
        print("==============================")
        print("1. Length (Meters / Feet)")
        print("2. Weight (Kg / Lbs)")
        print("3. Temperature (Celsius / Fahrenheit)")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            convert_length()
        elif choice == '2':
            convert_weight()
        elif choice == '3':
            convert_temperature()
        elif choice == '4':
            print("Thank you for using Unit Converter CLI. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 4.\n")


if __name__ == "__main__":
    main()