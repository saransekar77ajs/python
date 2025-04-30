import time, random, math

word_pairs = {
    "sky": ["blue", "cloud", "bird", "fly", "sun"],
    "water": ["drink", "ocean", "river", "swim", "boat"],
    "food": ["cook", "eat", "tasty", "meal", "restaurant"],
    "music": ["song", "dance", "listen", "band", "rhythm"],
    "book": ["read", "story", "library", "page", "author"],
    "tree": ["leaf", "green", "forest", "wood", "shade"],
    "car": ["drive", "road", "wheel", "travel", "speed"],
    "dog": ["pet", "bark", "walk", "loyal", "puppy"],
}

print("🔡 WORD ASSOCIATION GAME 🔡")
print("✨ Respond with the related word quickly ✨")

total_score = 0
rounds = 0

while True:
    prompt = random.choice(list(word_pairs.keys()))
    realted_words = word_pairs[prompt]

    print(f"Prompted Word: {prompt.upper()}")
    print(f"Quick! type a word related to this prompt.")

    start_time = time.time()
    user_response = input("Enter your related word: ").lower().strip()
    response_time = time.time() - start_time

    print("Response time", response_time)

    if user_response not in word_pairs[prompt]:
        print(
            f"Not a common association. Related words included: {', '.join(realted_words)}"
        )

    else:
        round_score = max(5 - int(response_time), 1)
        total_score += round_score
        rounds += 1

        print(
            f"✅ Good association! +{round_score} points this round. (answered in ⏱️ {response_time:.1f}s)"
        )
        print(f"📊 Total Score: {total_score}/{rounds * 5}")

    play_again = input("Do you want to play again? (y/n) ").lower().strip()

    if play_again != "y":
        print("👋 Goodbye!")
        break


"""
words = ["Dog", "Tree", "Sky", "Human", "Ocean", "Fire"]
question = 1
points_per_question = 5
total_score = 0

while True:
    prompt_word = random.choice(words)
    print(f"Prompt word: {prompt_word}")
    print(f"Quick! type a word related to this prompt.")

    start_time = time.time()
    user_response = input("Enter your word: ")
    end_time = time.time()

    response_time = round(end_time - start_time, 2)
    round_score = max(points_per_question - math.ceil(response_time), 1)
    total_score += round_score

    print(f"⏱️ Response Time: {response_time}s")
    print(f"✅ You earned {round_score} points this round.")
    print(f"📊 Total Score: {total_score}/{question * points_per_question}")

    play_again = input("Do you want to play again? (y/n) ").lower().strip()

    if play_again != "y":
        print("👋 Goodbye!")
        break
    question += 1
"""
