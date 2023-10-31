if __name__ == '__main__':
    #My name is Thomas Hahn and I wrote this encode function
    def encode():
        password = int(input("Please enter your password to encode:"))
        password += 33333333
        print("Your password has been encoded and stored!")

    #This is the change made by Om Patel
    def decode():
        decoded_password =""
        for digit in password:
            decoded_digit = str((int(digit) - 3) % 10)
            decoded_password += decoded_digit
        return decoded_password
        print("Your password has been decoded and stored!")

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    user_input = input("Please enter an option:")
    if user_input == "1":
        encode()
    if user_input == "2":
        decode()
