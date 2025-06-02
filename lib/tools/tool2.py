import os

def binary_encrypt(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_decrypt(binary_text):
    chars = binary_text.split()
    return ''.join(chr(int(b, 2)) for b in chars)

def run():
    while True:
        os.system("clear")
        print("🔐 Binary Text Converter ")
        print("1. Encrypt Text to Binary")
        print("2. Decrypt Binary to Text")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "0":
            break
        elif choice == "1":
            text = input("\nEnter text: ")
            result = binary_encrypt(text)
        elif choice == "2":
            binary_text = input("\nEnter binary (space-separated 8-bit groups): ")
            try:
                result = binary_decrypt(binary_text)
            except Exception:
                result = "❌ Invalid binary input."
        else:
            print("Invalid choice.")
            input("\nPress Enter to continue...")
            continue

        print("\n🔸 Result:\n")
        print(result)
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
