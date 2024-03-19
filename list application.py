import random
import string
def generate_password(min_length, number=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letters
    if number:
        characters += digits
    if special_characters:
        characters += spcial
        pwd = ""
        meets_criteria = False
        has_number = False
        has_special = False
        while not meets_criteria or len(pwd) < min_length:
            new_char = random.choice(characters)
            pwd += new_char
            if new_char in digits:
                has_number = True
            elif new_char in special:
                has_special = True
            meets_criteria = True
            if number:
                meets_criteria = has_number
            if special_charcters:
                    meets_criteria = meets_critera and has_special
        return pwd
min_length = int(input("Enter the mininum length: "))
has_number = input("Do you want to have number (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("the generated password is:" , pwd)
