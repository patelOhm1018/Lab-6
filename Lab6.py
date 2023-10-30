#This is Om Patel's code

def encode(password):
    encoded_password =""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def menu_display():
    print("Menu")
    print("-" * 13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

if __name__ == "__main__":
    menu_display()
    option = True
    while option:
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = str(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        if user_input == 2:
            encoded_password = encode(password)
            print(f"The encoded password is {encoded_password}, and the original password is {password}")
        if user_input == 3:
            break
