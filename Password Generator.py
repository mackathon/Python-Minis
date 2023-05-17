import secrets
import string

def generate_password(length):
    # All the characters you want to allow
    all_characters = string.ascii_letters + string.digits + string.punctuation

    if length < 4:
        print("Password length should be at least 4.")
        return None

    # Generate a password
    # Make sure the password contains at least one lowercase, one uppercase, one digit, and one special character
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    # Generate the remaining characters
    password += [secrets.choice(all_characters) for _ in range(length-4)]

    # Shuffle the password to ensure it's not in a predictable order
    secrets.SystemRandom().shuffle(password)

    # Convert the list of characters into a string
    password = ''.join(password)

    return password

length = int(input("Enter the length of the password: "))
password = generate_password(length)
if password:
    print("Your new password is:", password)
