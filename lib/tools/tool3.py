import os
from Crypto.Cipher import Blowfish
import base64

def blowfish_encrypt(text, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    plen = 8 - (len(text) % 8)
    text += chr(plen) * plen
    encrypted_bytes = cipher.encrypt(text.encode('utf-8'))
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def blowfish_decrypt(encoded_text, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted_bytes = cipher.decrypt(base64.b64decode(encoded_text))
    plen = decrypted_bytes[-1]
    return decrypted_bytes[:-plen].decode('utf-8')

def run():
    while True:
        os.system("clear")
        print("🔐 Blowfish Encryptor/Decryptor")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "0":
            break
        elif choice not in ["1", "2"]:
            print("Invalid choice.")
            input("\nPress Enter to continue...")
            continue

        text = input("\nEnter text: ")
        key_input = input("Enter encryption key (8-56 chars): ").encode('utf-8')

        if len(key_input) < 8:
            print("Key too short. Must be at least 8 characters.")
            input("\nPress Enter to continue...")
            continue

        try:
            if choice == "1":
                result = blowfish_encrypt(text, key_input)
            else:
                result = blowfish_decrypt(text, key_input)
        except Exception as e:
            result = f"❌ Error: {str(e)}"

        print("\n🔸 Result:\n")
        print(result)
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
