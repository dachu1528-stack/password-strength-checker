import string
import random

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 2
    if any(c.isupper() for c in password):
        score += 2
    if any(c.islower() for c in password):
        score += 2
    if any(c.isdigit() for c in password):
        score += 2
    if any(c in string.punctuation for c in password):
        score += 2

    if score == 10:
        return "Strong 💪"
    elif score >= 6:
        return "Medium ⚠️"
    else:
        return "Weak ❌"

# Menu system
while True:
    print("\n--- Password Tool ---")
    print("1. Check Password Strength")
    print("2. Generate Password")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pwd = input("Enter password: ")
        print("Strength:", check_password(pwd))

    elif choice == "2":
        length = int(input("Enter length: "))
        print("Generated Password:", generate_password(length))

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
