import random

choice = input("Do you want to code or decode? ").lower()
message = input("Enter your message: ")
words = message.split()

if choice == "code":
    for word in words:
        if len(word) >= 3:
            new_word = word[1:] + word[0]

            for _ in range(3):
                new_word = random.choice("abcdefghijklmnopqrstuvwxyz") + new_word

            for _ in range(3):
                new_word = new_word + random.choice("abcdefghijklmnopqrstuvwxyz")

            final_word = new_word
        else:
            final_word = word[::-1]

        print(final_word, end=" ")

elif choice == "decode":
    for word in words:
        if len(word) >= 3:
            trimmed_word = word[3:-3]
            final_word = trimmed_word[-1] + trimmed_word[:-1]
        else:
            final_word = word[::-1]

        print(final_word, end=" ")

else:
    print("Invalid choice! Please enter code or decode.")
