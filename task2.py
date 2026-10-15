import secrets
import string

def get_user_preferences():
    """Gathers password requirements from the user."""
    print("=== 🔑 CLI Password Generator 🔑 ===")
    
    # 1. Password Length
    while True:
        try:
            length = int(input("Enter desired password length (min 4): "))
            if length >= 4:
                break
            print("Length should be at least 4 for basic security.")
        except ValueError:
            print("Please enter a valid number.")

    # 2. Character Types
    print("\nSelect character types to include:")
    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include special symbols? (y/n): ").strip().lower() == 'y'

    # Ensure at least one set is chosen
    if not any([use_upper, use_lower, use_digits, use_symbols]):
        print("\n⚠️ You must select at least one character type! Defaulting to lowercase.")
        use_lower = True

    # 3. Number of Passwords
    while True:
        try:
            count = int(input("\nHow many passwords would you like to generate? "))
            if count > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    return length, use_upper, use_lower, use_digits, use_symbols, count


def build_character_pool(use_upper, use_lower, use_digits, use_symbols):
    """Combines selected character sets into a single string pool."""
    pool = ""
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation
    return pool


def generate_passwords(length, pool, count):
    """Generates random passwords using cryptographically secure secrets module."""
    passwords = []
    for _ in range(count):
        # Pick 'length' random characters from the pool
        pwd = ''.join(secrets.choice(pool) for _ in range(length))
        passwords.append(pwd)
    return passwords


def main():
    # Gather settings
    length, use_upper, use_lower, use_digits, use_symbols, count = get_user_preferences()
    
    # Build pool
    pool = build_character_pool(use_upper, use_lower, use_digits, use_symbols)
    
    # Generate
    passwords = generate_passwords(length, pool, count)
    
    # Output
    print("\n" + "="*35)
    print(f" Generated Password{'s' if count > 1 else ''}:")
    print("="*35)
    for idx, pwd in enumerate(passwords, start=1):
        print(f"[{idx}] {pwd}")
    print("="*35)


if __name__ == "__main__":
    main()