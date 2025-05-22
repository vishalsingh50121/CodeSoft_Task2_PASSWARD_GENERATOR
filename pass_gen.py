import random
import string

def generate_password(length):
    """Generate a random password of specified length"""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    all_chars = lowercase + uppercase + digits + symbols
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Password Generator")
    print("-----------------")
    
    while True:  # Keep asking until valid input
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            
            if length < 8:
                print("Password length should be at least 8. Using 8 instead.")
                length = 8
            
            password = generate_password(length)
            print("\nGenerated Password:", password)
            print("\nNote: Make sure to store this password securely!")
            break  # Exit loop if successful
            
        except ValueError:
            print("⚠️ Invalid input! Please enter a number (e.g., 10).")

if __name__ == "__main__":
    main()
