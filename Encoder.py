if __name__ == '__main__':
    def encode():
        password = int(input("Please enter your password to encode:"))
        password += 33333333
        print("Your password has been encoded and stored!")

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    user_input = input("Please enter an option:")
    if user_input == "1":
        encode()
    elif user_input == 2:
        encoded_password = password
        password = encoded_password - 33333333
        print(f"The encoded password is {encoded_password}, and the original password is {password}.")




