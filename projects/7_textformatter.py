print(" 📢 TEXT FORMATTER 📢")
print()
text = input("Enter the text you would like to format: ")
print("\nChoose a format option:")
print("1. Upper Case")
print("2. Lower Case")
print("3. Capitalize")
print("4. Title Case")
formatter = input("Enter your choice (1-4): ")

match formatter:
    case "1":
        print(f"{text.upper()}.")
    case "2":
        print(f"{text.lower()}.")
    case "3":
        print(f"{text.capitalize()}.")
    case "4":
        print(f"{text.title()}.")
    case _:
        print(f"Invalid Choice.")
