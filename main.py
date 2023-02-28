print("WELCOME TO DAILY THOUGHTS APP\n")
date = input("Enter Today's Date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("What are your thoughts for the day:\n")

with open(f"thoughts/{date}.txt", "w") as file:
    file.write(mood + 2 * '\n')
    file.write(thoughts)
