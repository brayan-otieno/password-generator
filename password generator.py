import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    # Combine all character sets
    all_characters = lowercase + uppercase + numbers + special_chars
    
    # Ensure the password contains at least one character from each selected set
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_special_chars:
        password.append(random.choice(special_chars))
    
    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - len(password))
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")
