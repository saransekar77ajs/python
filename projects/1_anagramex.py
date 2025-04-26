print("Welcome to find if your input strings are Anagram!")


def find_anagram(string1, string2):

    if len(string1) != len(string2):
        print(f"Your strings '{string1}' and '{string2}' are NOT an Anagram.")
    else:
        string1, string2 = string1.lower(), string2.lower()
        first_list = list(string1)
        second_list = list(string2)
        first_list.sort()
        second_list.sort()
        # print("first_string", first_list)
        # print("second_string", second_list)
        new_string_one = "".join(first_list)
        new_string_two = "".join(second_list)
        # print("New String one", new_string_one)
        # print("New String two", new_string_two)

        if new_string_one == new_string_two:
            print(
                f"Entered String one '{string1}' and String two '{string2}' is Anagram."
            )
        else:
            print(f"Your strings '{string1}' and '{string2}' are NOT an Anagram.")


if __name__ == "__main__":
    string_one = input("Enter first string: ")
    string_two = input("Enter second string: ")
    find_anagram(string_one, string_two)
