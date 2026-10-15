import sys


def get_quiz_questions():
    """Returns a list of 10 general knowledge questions."""
    return [
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B",
        },
        {
            "question": "What is the smallest country in the world by land area?",
            "options": ["A. Monaco", "B. Nauru", "C. Vatican City", "D. San Marino"],
            "answer": "C",
        },
        {
            "question": "Who painted the ceiling of the Sistine Chapel?",
            "options": ["A. Leonardo da Vinci", "B. Michelangelo", "C. Raphael", "D. Donatello"],
            "answer": "B",
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["A. Quartz", "B. Diamond", "C. Topaz", "D. Titanium"],
            "answer": "B",
        },
        {
            "question": "Which river is the longest in the world?",
            "options": ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"],
            "answer": "B",
        },
        {
            "question": "How many players are on the field for one team in a standard soccer match?",
            "options": ["A. 9", "B. 10", "C. 11", "D. 12"],
            "answer": "C",
        },
        {
            "question": "What is the chemical symbol for Gold?",
            "options": ["A. Au", "B. Ag", "C. Fe", "D. Gd"],
            "answer": "A",
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["A. 1905", "B. 1912", "C. 1918", "D. 1923"],
            "answer": "B",
        },
        {
            "question": "What is the currency of Japan?",
            "options": ["A. Won", "B. Yuan", "C. Yen", "D. Ringgit"],
            "answer": "C",
        },
        {
            "question": "Which organ in the human body consumes the most energy?",
            "options": ["A. Heart", "B. Liver", "C. Brain", "D. Lungs"],
            "answer": "C",
        },
    ]


def run_quiz():
    """Runs a single round of the General Knowledge quiz game."""
    questions = get_quiz_questions()
    score = 0
    total = len(questions)

    print("\n" + "=" * 45)
    print("   WELCOME TO THE GENERAL KNOWLEDGE QUIZ!")
    print("=" * 45)

    for idx, q in enumerate(questions, 1):
        print(f"\nQuestion {idx} of {total}:")
        print(q["question"])

        for option in q["options"]:
            print(f"  {option}")

        # Get valid user input
        while True:
            user_ans = (
                input("\nYour answer (A, B, C, or D): ").strip().upper()
            )
            if user_ans in ["A", "B", "C", "D"]:
                break
            print("Invalid input! Please enter A, B, C, or D.")

        # Check answer
        if user_ans == q["answer"]:
            print("✨ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was {q['answer']}.")

    # Display final performance metrics
    percentage = (score / total) * 100
    print("\n" + "=" * 45)
    print("                 QUIZ RESULTS")
    print("=" * 45)
    print(f"Final Score: {score} / {total} ({percentage:.1f}%)")

    if percentage == 100:
        print("🏆 Perfect score! Brilliant mind!")
    elif percentage >= 70:
        print("🎉 Great job! Solid general knowledge.")
    else:
        print("📚 Good attempt! Time for some trivia refresher.")


def main():
    """Main game loop with replay capability."""
    while True:
        run_quiz()

        # Replay loop validation
        while True:
            replay = (
                input("\nWould you like to play again? (yes/no): ")
                .strip()
                .lower()
            )
            if replay in ["yes", "y"]:
                break
            elif replay in ["no", "n"]:
                print("\nThanks for playing! Goodbye!\n")
                sys.exit()
            else:
                print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()