# Lyrics Quiz Project
# write a quiz
def lyrics_quiz():
    print("** Welcome to the Lyrics Quiz **")

    print("Instructions: Answer each question by typing a, b, c, or d")

if __name__== "__main__":
    lyrics_quiz()
    print()




def play_quiz():
    print("Starting quiz...")

if __name__== "__main__":
    play_quiz()
print()

quiz_data = [
    {
        "question": "I'm ready to go ___",
        "choices": [
            "a) ye",
            "b) ohoh",
            "c) lets go",
            "d) she go",
        ],
        "answer": "b(ohoh)",
    },
    {
        "question": "She is so pretty ___?",
        "choices": [
            "a) there is goes",
            "b) yeahh ohhh",
            "c) she takes my breath away",
            "d) oh lala",
        ],
        "answer": "c(she takes my breath away)",
    },
    {
        "question": "Coconut ___",
        "choices": [
            "a) water",
            "b) tree",
            "c) flavour",
            "d) tea",
        ],
        "answer": "a(water)",
    },
]
score = 0
for question in quiz_data:
    print(question["question"])
    print()
    for choice in question["choices"]:
        print(choice)
        print()
    user_answer = input("Enter Choice: ").strip().lower()
    if user_answer == question["answer"]:
        print("You got it right")
        print()
        score += 1
    else:
        print(f"Incorrect answer (right answer is : {question['answer']})")
        print()

print(f"Quiz Score : {score} / {len(quiz_data)}")
print("Thank you for playing , hope you had fun.")






    



    