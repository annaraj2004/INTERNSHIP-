import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    """Generate a random password with the given parameters."""
    # Define character sets
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    # Combine all character sets
    all_chars = lower_chars + upper_chars + digits + special_chars
    
    if not all_chars:
        raise ValueError("No character sets selected. At least one type of character must be included.")
    
    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input for length: {e}")
        return
    
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    
    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
