print("🚶‍♀️‍➡️ STEP COUNTER 🚶‍♀️")
print()
print(" 🤷‍♂️ What is your daily step goal? ")

try:
    daily_goal = int(input("Enter your daily step goal: "))
    print()
    todays_step = int(input("How many steps you have completed today? "))

    if daily_goal > todays_step:
        print(f"You need {daily_goal-todays_step} more steps to reach your goal!")
    elif daily_goal < todays_step:
        print(
            f"🎉 Congradulations! you have exceeded your goal by {todays_step-daily_goal} steps!"
        )
    else:
        print(f"You have exactly reached your goal!")

except ValueError:
    print("Invalid input steps should be numeric.")
except Exception as e:
    print(f"Error occured: {e}")
