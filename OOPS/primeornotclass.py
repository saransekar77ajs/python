class PrimeChecker:
    def __init__(self, number):
        self.number = number

    def is_prime(self):
        if self.number <= 1:
            return False
        for i in range(2, int(self.number**0.5) + 1):
            if self.number % i == 0:
                return False
        return True


# Example usage
number = int(input("Enter a number to check if it's prime: "))
checker = PrimeChecker(number)

if checker.is_prime():
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
