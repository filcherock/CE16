import os

from ce16 import decode, encode, nonDecodeEncoding
from colorama import Fore, Style

def main():
    while True:
        os.system('cls')
        variant = int(input("Codex Encode 16\n- 1. Encode text\n- 2. Decode text\n- 3. Encode non-decodint text\n- 4. Exit\nEnter [1/2/3/4]: "))
        if variant == 1:
            text = input("Enter text: ")
            print(encode(text))
            input("Enter any key for continue . . .")
        elif variant == 2:
            text = input("Enter encoding code: ")
            print(decode(text))
            input("Enter any key for continue . . .")
        elif variant == 3:
            text = input("Enter text: ")
            print(nonDecodeEncoding(text))
            input("Enter any key for continue . . .")
        elif variant == 4:
            break

if __name__ == '__main__':
    main()