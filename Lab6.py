#This is Om Patel's code

def encode(password):
    encoded_password =""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

#This Decode Function was written by Thomas Hahn
def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_num = str((int(digit) - 3) % 10)
        decoded_password += decoded_num
    return decoded_password
#This prints the menu
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
            #This code is used to encode the password
            password = str(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
            encoded_password = encode(password)
            print(f"The encoded password is {encoded_password}, and the original password is {password}")
        if user_input == 2:
            #This code is used to decode the password
            password = str(input("Please enter your password to decode: "))
            print("Your password has been encoded and stored!")
            decoded_password = decode(password)
            print(f"The decoded password is {decoded_password}, and the original password is {password}")
        if user_input == 3:
            break
