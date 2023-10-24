  # Vishakh Surendran
def encoder(password):  # method to encode a password by adding three to each digit
    encoded_password = ""
    for i in password:
        encoded_digit = int(i) + 3
        encoded_password += str(encoded_digit)
    return encoded_password


def decoder(code):
    pass


def main():
    continue_codec = True
    while continue_codec:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = str(input("Please enter your password to encode: "))
            encoded = encoder(password)
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            decoded = decoder(encoded)
            print("The encoded password is " + encoded + " and the original password is " + decoded + ".\n")
        elif choice == 3:
            continue_codec = False


if __name__ == "__main__":  # calls main function and executes program
    main()
