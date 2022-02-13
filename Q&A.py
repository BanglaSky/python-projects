# -------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# -------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")


# -------------------------
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


# -------------------------


questions = {
    "What is 1 + 1?: ": "B",
    "What is the definition of the word 'flabbergasted'?: ": "A",
    "Who created Facebook?: ": "C",
    "Is the Earth round?: ": "A",
    "What is the best game in 2021?: ": "C"
}

options = [["A. 1", "B. 2", "C. 3", "D. 4"],
           ["A. greatly surprised", "B. sad", "C. angry", "D. a sentence worded so as to elicit information."],
           ["A. Elon Musk", "B. Jeff Bezos", "C. Mark Zuckerburg", "D. Bill Gates"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"],
           ["A. Fortnite", "B. COD Warzone", "C. There isn't a best game", "D. Minecraft"]]
new_game()

while play_again():
    new_game()

print("Byeeeeee!")
