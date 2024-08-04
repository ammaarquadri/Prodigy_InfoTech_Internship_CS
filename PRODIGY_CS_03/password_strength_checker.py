import re

def check_password_strength(password):
    # Define criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Calculate score based on criteria
    score = length_criteria + uppercase_criteria + lowercase_criteria + digit_criteria + special_char_criteria

    # Determine password strength based on score
    if score == 5:
        return "Very Strong"
    elif score >= 3:
        return "Strong"
    elif score >= 2:
        return "Moderate"
    elif score >= 1:
        return "Weak"
    else:
        return "Very Weak"

def main():
    print("Password Strength Checker")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            break
        
        strength = check_password_strength(password)
        print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
