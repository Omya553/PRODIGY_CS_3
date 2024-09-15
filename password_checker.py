import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Add at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Add at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Include at least one number.")
    if not special_char_criteria:
        feedback.append("Use at least one special character (e.g., !@#$%).")

    return strength, feedback

password = input("Enter a password to assess: ")
strength, feedback = assess_password_strength(password)

print(f"Password strength: {strength}")
if feedback:
    print("Suggestions to improve your password:")
    for suggestion in feedback:
        print(f"- {suggestion}")