import random

print(" 🎼 MUSIC RECOMMENDER 🎼 ")

genre = ["rock", "pop", "hip-hop", "melody"]

music = {
    "rock": [
        "Bohemian Rhapsody - Queen",
        "Stairway to Heaven - Led Zeppelin",
        "Hotel California - Eagles",
        "Smells Like Teen Spirit - Nirvana",
        "Sweet Child O' Mine - Guns N' Roses",
    ],
    "pop": [
        "Blinding Lights - The Weeknd",
        "Shape of You - Ed Sheeran",
        "Bad Romance - Lady Gaga",
        "Uptown Funk - Mark Ronson ft. Bruno Mars",
        "Shake It Off - Taylor Swift",
    ],
    "hip-hop": [
        "Lose Yourself - Eminem",
        "Sicko Mode - Travis Scott",
        "Juicy - The Notorious B.I.G.",
        "God's Plan - Drake",
        "HUMBLE. - Kendrick Lamar",
    ],
    "melody": [
        "Someone Like You - Adele",
        "Fix You - Coldplay",
        "The Scientist - Coldplay",
        "Thinking Out Loud - Ed Sheeran",
        "Let Her Go - Passenger",
    ],
}

while True:
    print("\n Choose your choice of muisc: ")
    print(" 1.Rock")
    print(" 2.Pop")
    print(" 3.Hip-Hop")
    print(" 4.Melody")
    users_choice = input("What genre do you like to hear? ")
    # print(users_choice)
    index = int(users_choice) - 1

    try:
        if 0 <= index < len(genre):
            selected_genre = genre[index]
            songs = music[selected_genre]
            random.shuffle(songs)
            print(f"Here are some songs from the {selected_genre.capitalize()} genre:")
            print("\n".join(songs[:3]))
        else:
            print(" 😭 Sorry, I don't know that genre.")
            break
    except ValueError as v:
        print(f"Value Error occured: {v}")
    except Exception as e:
        print(f"Error occured: {e}")
