pwdtoCheck = input("Enter a password to check: ")
uppercaseCount = 0
lowercaseCount = 0
numCount = 0
specialCount = 0
if len(pwdtoCheck) < 8:
    print("Password is too short. It must be at least 8 characters long.")
for i in pwdtoCheck:
    if i.isupper():
        uppercaseCount += 1
    elif i.islower():
        lowercaseCount += 1
    elif i.isdigit():
        numCount += 1
    else:
        specialCount += 1
if uppercaseCount < 2:
    print("Password must contain at least 2 uppercase letters.")
if lowercaseCount < 2:
    print("Password must contain at least 2 lowercase letters.")
if numCount < 2:
    print("Password must contain at least 2 numeric digits.")
if specialCount < 2:
    print("Password must contain at least 2 special characters.")
if uppercaseCount >= 2 and lowercaseCount >= 2 and numCount >= 2 and specialCount >= 2 and len(pwdtoCheck) >= 8:
    print("Password is valid, you can use this password for an account.")