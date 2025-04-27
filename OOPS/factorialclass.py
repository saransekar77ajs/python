from math import factorial


class FactCalc:
    def __init__(self, number):
        self.number = number

    def fact(self):
        if self.number <= 1:
            return 1
        return factorial(self.number)


# Example usage
number = int(input("Enter a number to check its factorial: "))
fact_check = FactCalc(number).fact()

print(f"The factorial for the given number {number} is {fact_check}")
