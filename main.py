import vigenere

KEY = ""


def main():
    print("")
    print("----------------------------------------")
    print("Welcome to my Vignère Cipher Application")
    print("----------------------------------------")
    print("")

    cycle = True

    while cycle:
        response = input("Would you like to encrypt or decrypt? (e/d): ").lower()
        while response not in ["e", "d"]:
            response = input("Please enter a valid response, 'e' or 'd': ").lower()

        prompt_cycle(response)
        proceede = input("Would you like to exit? (y/n): ").lower()
        while proceede not in ["y", "n"]:
            proceede = input("Please enter a valid response, 'y' or 'n': ").lower()

        if proceede == "y":
            cycle = False

    print("Shutting down...")


def prompt_cycle(response):
    if response == "e":
        message = input("Please enter an alphanumeric message to encrypt: ")
        key = input("Please enter a key: ")
        print("Your encrypted messages is: " + vigenere.encrypt(message, key))
        print("")
    else:
        message = input("Please enter an alphanumeric message to decrypt: ")
        key = input("Please enter a key: ")
        print("Your decrypted message is: " + vigenere.decrypt(message, key))
        print("")


if __name__ == "__main__":
    main()
