import random

protiens = ["Chicken", "Beef", "Pork", "Fish", "Tofu", "Legumes", "Eggs"]
veggies = [
    "Spinach",
    "Brocolli",
    "Cauliflower",
    "Carrots",
    "Squash",
    "Green beans",
    "Cabbage",
]
carbs = ["Rice", "Pasta", "Potatoes", "Quinoa", "Bread"]
methods = ["Baked", "Grilled", "Poached", "Saut`eed", "Roasted", "Steamed"]
flavors = ["Garlic", "Lemon", "Herb", "Spicy", "Schezwan", "Sweet & Sour"]

while True:
    protien = random.choice(protiens)
    veggie = random.choice(veggies)
    carb = random.choice(carbs)
    method = random.choice(methods)
    flavor = random.choice(flavors)

    print(
        f"\nYour random recipe: {flavor} {method} {protien} with {veggie} and {carb}."
    )

    if not input("Do you want another recipe (y/n)? ").lower().startswith("y"):
        print("👋 Goodbye!")
        break
    else:
        continue
