print("WE ARE LIVE FOR TODAY'S KBC QUIZ...!!")

player_name = input("Enter your name: ")
print(f"Welcome {player_name} to the KBC quiz game!")

questions = [
    "What is the capital of INDIA?",
    "What is the largest planet in our solar system?",
    "What is the chemical symbol for water?",
    "Who wrote Indian national anthem?",
    "What is the smallest prime number?",
    "What is the currency of India?",
]

options = [
    ["A) Delhi", "B) Mumbai", "C) Kolkata", "D) Chennai"],
    ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
    ["A) H2O", "B) CO2", "C) O2", "D) N2"],
    ["A) Sarojini Naidu", "B) Bankim Chandra Chatterjee", "C) Rabindranath Tagore", "D) Mahatma Gandhi"],
    ["A) 0", "B) 1", "C) 3", "D) 2"],
    ["A) Dollar", "B) Euro", "C) Rupee", "D) Pound"],
]

correct_answers = ["A", "B", "A", "C", "D", "C"]
prize_money = 0

def ask_question(index):
    print(f"\nQuestion {index + 1}: {questions[index]}")
    for option in options[index]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").upper()
    return answer == correct_answers[index]

for i in range(len(questions)):
    if ask_question(i):
        prize_money += 1000
        print(f"Correct! Prize money: ₹{prize_money}")
    else:
        print("Wrong answer! Game over.")
        break

print(f"\nYou are taking home: ₹{prize_money}")
