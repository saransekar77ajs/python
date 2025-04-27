class PalindromeChecker:
    def __init__(self, number):
        self.number = str(number)  # Convert the input to a string

    def is_palindrome(self):
        return self.number == self.number[::-1]  # Compare the original with its reverse


# Example usage
number = input("Enter a number to check if it's a palindrome: ")  # Keep it as a string
checker = PalindromeChecker(number)

if checker.is_palindrome():
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
