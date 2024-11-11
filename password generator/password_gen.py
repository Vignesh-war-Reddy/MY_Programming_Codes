import random
import string

def generate_password(length):
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation
    
    
    all_chars = uppercase + lowercase + digits + special_chars
    
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
   
    length = int(input("Enter the desired length for the password: "))
    
    
    password = generate_password(length)
    
    
    print(f"Generated Password: {password}")

main()
