password = input("Enter Password: ")

has_upper = False
has_lower = False
has_digit = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Strong Password")
else:
    print("Weak Password")
    print("Reasons:")
    if len(password) < 8:
        print("- Password must be at least 8 characters.")
    if not has_upper:
        print("- Add at least one uppercase letter.")
    if not has_lower:
        print("- Add at least one lowercase letter.")
    if not has_digit:
        print("- Add at least one digit.")  

