import string
import random

def generate_length():
    while True:
        try:
            password_length = input("Enter your desired password length or 'exit' to quit: ")
            if password_length.lower() == 'exit':
                return None
            length = int(password_length)
            if length < 6:
                print("Your password should at least be 6 characters")
            else:
                return length
        except ValueError:
            print("Please enter a number")

def password_complexity():
    password_strength = {
        "weak": {"lowercase": True, "uppercase": False, "digits": False, "punctuation": False},
        "medium": {"lowercase": True, "uppercase": True, "digits": False, "punctuation": False},
        "strong": {"lowercase": True, "uppercase": True, "digits": True, "punctuation": False},
        "very strong": {"lowercase": True, "uppercase": False, "digits": True, "punctuation": True}
    }
    while True:
        strength = input("Enter your desired complexity level (weak/medium/strong/very strong): ").strip().lower()
        if strength in password_strength:
            return password_strength[strength]
        else:
            print("Invalid choice.")

def generate_password(length, complexity):
    characters = ""

    if complexity["lowercase"]:
        characters += string.ascii_lowercase
    if complexity["uppercase"]:
        characters += string.ascii_uppercase
    if complexity["digits"]:
        characters += string.digits
    if complexity["punctuation"]:
        characters += string.punctuation

    password = random.choices(characters, k=length)

    random.shuffle(password)

    return ''.join(password)

def main():
    while True:
        length = generate_length()
        if length is None:
            print("Exiting...")
            break

        complexity = password_complexity()
        password = generate_password(length, complexity)
        if password:
            print(f"Generated password: {password}")

if __name__ == "__main__":
    main()