import random as rd
import string

pass_length = int(input("\nHow long would you like your password to be? "))

# check the length
while pass_length < 12 or pass_length > 112:
    if pass_length < 12:
        print("\nA strong password has more than 12 characters.")
        pass_length = int(input("\nPlease pick a number greater than or equal to 12: "))
    if pass_length > 112:
        print("\nWoah! That password is crazy long!")
        pass_length = int(input("\nPlease pick a number below 112: "))

# assign all character options to categorized variables
pass_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
pass_chars_upper = string.ascii_uppercase
pass_chars_lower = string.ascii_lowercase
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

pass_options = []

# create an array with every character option
for char in pass_chars_upper:
    pass_options.append(char)
for char in pass_chars_lower:
    pass_options.append(char)
for spec_char in special_chars:
    pass_options.append(spec_char)
for num in pass_nums:
    pass_options.append(num)

# logic to create the password
def generate_pass():
    new_pass_chars = []
    num_of_chars = 0
    generated_pass = ""

    while num_of_chars < pass_length:
        new_pass_chars.append(rd.choice(pass_options))
        num_of_chars += 1

    for char in new_pass_chars:
        generated_pass += char

    return generated_pass

print("\nHere's your password: " + generate_pass())
