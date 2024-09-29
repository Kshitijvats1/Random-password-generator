import random
import string
import pyperclip

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    character_pool = ''
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        print("Error: No character types selected.")
        return None
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to Secure Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (e.g., !@#$%^&*): (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
    
    if password:
        print(f"Generated Password: {password}")
        copy_to_clipboard = input("Copy to clipboard? (y/n): ").lower() == 'y'
        if copy_to_clipboard:
            pyperclip.copy(password)
            print("Password copied to clipboard!")

if __name__ == "__main__":
    main()
