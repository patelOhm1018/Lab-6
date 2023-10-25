if __name__ == "__main__":
    print("Menu")
    print("-" * 13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    option = True
    while option:
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = int(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        if user_input == 2:
            encoded_password = password + 33333333
            print(f"The encoded password is {encoded_password}, and the original password is {password}")
        if user_input == 3:
            option = False



