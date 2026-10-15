import random

def get_positive_int(prompt):
    """Utility function to ensure user inputs a positive integer >= 1."""
    while True:
        try:
            val = int(input(prompt))
            if val >= 1:
                return val
            print("Please enter a number greater than or equal to 1.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")


def roll_dice(num_dice, sides):
    """Simulates rolling 'num_dice' dice, each with 'sides' sides."""
    results = [random.randint(1, sides) for _ in range(num_dice)]
    total = sum(results)
    return results, total


def display_history(history):
    """Displays all rolls recorded during the active session."""
    if not history:
        print("\n📜 No rolls recorded in this session yet.")
        return

    print("\n" + "=" * 50)
    print("📜 SESSION ROLL HISTORY")
    print("=" * 50)
    for entry in history:
        dice_str = ", ".join(map(str, entry['results']))
        print(f"Roll #{entry['roll_num']}: {entry['num_dice']}d{entry['sides']} "
              f"-> [{dice_str}] | Total: {entry['total']}")
    print("=" * 50)


def main():
    session_history = []
    roll_counter = 0

    print("=== 🎲 Welcome to the Dice Rolling Simulator 🎲 ===")

    while True:
        print("\nMain Menu:")
        print("1. Roll Dice")
        print("2. View Session History")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            # Gather configuration
            num_dice = get_positive_int("\nHow many dice would you like to roll? ")
            sides = get_positive_int("How many sides does each die have? (e.g., 6, 20): ")

            # Roll logic
            results, total = roll_dice(num_dice, sides)
            roll_counter += 1

            # Store in session history
            session_history.append({
                "roll_num": roll_counter,
                "num_dice": num_dice,
                "sides": sides,
                "results": results,
                "total": total
            })

            # Display results
            print("\n" + "-" * 35)
            print(f"🎲 Rolled {num_dice} x {sides}-sided die/dice!")
            print(f"Individual Results : {results}")
            print(f"Total              : {total}")
            print("-" * 35)

        elif choice == "2":
            display_history(session_history)

        elif choice == "3":
            print("\nThanks for playing! Goodbye 👋")
            break

        else:
            print("Invalid selection. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()