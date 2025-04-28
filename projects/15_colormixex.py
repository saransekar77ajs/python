color_mixes = {
    ("red", "blue"): "purple",
    ("red", "yellow"): "orange",
    ("blue", "yellow"): "green",
    ("blue", "green"): "teal",
    ("red", "white"): "pink",
    ("black", "white"): "gray",
    ("yellow", "green"): "lime",
    ("blue", "purple"): "indigo",
    ("red", "brown"): "maroon",
    ("orange", "black"): "burnt orange",
    ("purple", "white"): "lavender",
    ("green", "brown"): "olive",
    ("pink", "purple"): "magenta",
    ("blue", "gray"): "slate",
}

while True:
    color1 = input("\nEnter first color: ").lower().strip()
    color2 = input("\nEnter second color: ").lower().strip()

    mix = None
    if (color1, color2) in color_mixes:
        mix = color_mixes[(color1, color2)]
    elif (color2, color1) in color_mixes:
        mix = color_mixes[(color2, color1)]

    if mix:
        print(f"When you mix {color1} and {color2}, you get {mix}")
    else:
        print(
            f"Sorry i dont know what color your will get if you mix {color1} and {color2}"
        )
    if not input("\nMix more colors? (y/n) ").lower().startswith("y"):
        print("👋 Goodbye!")
        break
    else:
        continue
