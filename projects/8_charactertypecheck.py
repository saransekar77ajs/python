print("🔣 CHECK CHAR TYPE 🔣")
character = input("Enter a single character: ")

if len(character) != 1:
    print("Please enter single character.")
else:
    if character.isalpha():
        print(f"Entered {character} is an alphabet!")
    elif character.isdigit():
        print(f"Entered {character} is a number.")
    else:
        print(f"Entered {character} is a special character.")
