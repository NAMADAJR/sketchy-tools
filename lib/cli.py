from helpers import clear_screen
from tools import tool1, tool2, tool3, tool4, tool5, tool6, tool7

def show_tools_menu():
    while True:
        clear_screen()
        print("Sketchy Messages and tools by Nam\n")
        print("1. Morse Code: Encrypt & Decrypt Text")
        print("2. Binary Text Converter")
        print("3. Blowfish Encryptor/Decryptor")
        print("4. Steganography (Images)")
        print("5. File Bomb Creator")
        print("6. Self-Destructing Notes")
        print("7. Text Injector\n")
        print("0. Exit ")

        choice = input("Select an option: ")

        if choice == "0":
            clear_screen()
            print("You saw nothing")
            break
        elif choice == "1":
            tool1.run()
        elif choice == "2":
            tool2.run()
        elif choice == "3":
            tool3.run()
        elif choice == "4":
            tool4.run()
        elif choice == "5":
            tool5.run()
        elif choice == "6":
            tool6.run()
        elif choice == "7":
            tool7.run()
        else:
            print("\nInvalid choice. Try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    show_tools_menu()
