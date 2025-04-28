import random


first_parts = [
    "Elowen",
    "Seraphina",
    "Lilith",
    "Aria",
    "Talyndra",
    "Kael",
    "Thalric",
    "Eryndor",
    "Zephyr",
    "Draven",
    "Orin",
    "Lyric",
    "Solas",
    "Ashen",
    "Aeryn",
]

second_parts = [
    "Shadowveil",
    "Moonwhisper",
    "Frostshade",
    "Starblade",
    "Darkbrook",
    "Firestride",
    "Emberstone",
    "Stormheart",
    "Duskfall",
    "Nightshade",
    "Spellbound",
    "Everglen",
    "Windwalker",
    "Thornspire",
    "Mistshade",
]

print(" ✨ FANTASY NAME GENERATOR ✨ ")

generated_names = []

try:
    count = int(input("How many fantasy names do you want: "))

    for _ in range(count):
        first_name = random.choice(first_parts)
        last_name = random.choice(second_parts)
        generated_names.append(first_name + " " + last_name)
    print("Generated Fantasy Names: ", generated_names)


except ValueError:
    print("Please enter the number in numeric value.")
except Exception as e:
    print("Error Occured:", e)
