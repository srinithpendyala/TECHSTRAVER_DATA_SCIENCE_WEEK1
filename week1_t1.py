import random
import string

def get_user_input():
    length = int(input("Enter the desired length of the password: "))
    
    min_lowercase = int(input("Enter the minimum number of lowercase characters: "))
    min_uppercase = int(input("Enter the minimum number of uppercase characters: "))
    min_digits = int(input("Enter the minimum number of digits: "))
    min_symbols = int(input("Enter the minimum number of symbols: "))
    
    return length, min_lowercase, min_uppercase, min_digits, min_symbols

def generate_password(length, min_lowercase, min_uppercase, min_digits, min_symbols):
    if min_lowercase + min_uppercase + min_digits + min_symbols > length:
        raise ValueError("Minimum counts exceed total length")
    
    password = []
    
    password.extend(random.choices(string.ascii_lowercase, k=min_lowercase))
    password.extend(random.choices(string.ascii_uppercase, k=min_uppercase))
    password.extend(random.choices(string.digits, k=min_digits))
    password.extend(random.choices(string.punctuation, k=min_symbols))
    
    remaining_length = length - len(password)
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password.extend(random.choices(all_characters, k=remaining_length))
    
    random.shuffle(password)
    
    return ''.join(password)

if __name__ == "__main__":
    length, min_lowercase, min_uppercase, min_digits, min_symbols = get_user_input()
    try:
        password = generate_password(length, min_lowercase, min_uppercase, min_digits, min_symbols)
        print(f"Generated Password: {password}")
    except ValueError as ve:
        print(ve)
