import os
import time
import base64
import json
from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes

NOTE_PATH = "lib/tools/assets/notes/"
os.makedirs(NOTE_PATH, exist_ok=True)

def pad(text):
    plen = 8 - (len(text) % 8)
    return text + (chr(plen) * plen)

def unpad(text):
    plen = ord(text[-1])
    return text[:-plen]

def encrypt_note(message, key, read_time, output_file):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded_message = pad(message)
    encrypted_bytes = cipher.encrypt(padded_message.encode('utf-8'))
    encoded = base64.b64encode(encrypted_bytes).decode('utf-8')

    note_data = {
        "note": encoded,
        "read_time": read_time  
    }

    with open(os.path.join(NOTE_PATH, output_file), 'w') as f:
        json.dump(note_data, f)

    print(f"\n✅ Note created: {output_file} (Self-destructs after {read_time} seconds once opened)")

def decrypt_note(file_path, key):
    full_path = os.path.join(NOTE_PATH, file_path)
    if not os.path.exists(full_path):
        print("❌ Note not found.")
        return

    with open(full_path, 'r') as f:
        note_data = json.load(f)

    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    encrypted_bytes = base64.b64decode(note_data["note"])
    decrypted = cipher.decrypt(encrypted_bytes).decode('utf-8')
    message = unpad(decrypted)

    print(f"\n📨 Note content:\n{message}\n")

    read_time = note_data.get("read_time", 10)  
    print(f"⏳ You have {read_time} seconds to read this...")

    for i in range(read_time, 0, -1):
        print(f"🕒 {i} seconds remaining...", end='\r')
        time.sleep(1)

    print("\n💥 Time's up! Deleting note securely...")
    secure_delete(full_path)

def secure_delete(file_path):
    try:
        size = os.path.getsize(file_path)
        with open(file_path, 'wb') as f:
            f.write(os.urandom(size))
        os.remove(file_path)
        print("✅ Note securely deleted.")
    except Exception as e:
        print(f"❌ Error deleting note: {e}")

def run():
    while True:
        os.system("clear")
        print("📝 Self-Destructing Notes")
        print("1. Create a note")
        print("2. Open a note")
        print("0. Back")
        choice = input("Choose an option: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            message = input("Enter your secret message: ")
            key_input = input("Enter encryption key (8-56 chars): ").encode('utf-8')
            if len(key_input) < 8:
                print("Key too short.")
                input("Press Enter to continue...")
                continue
            try:
                read_time = int(input("Enter reading time in seconds (how long recipient can view it): "))
            except ValueError:
                print("Invalid time.")
                input("Press Enter to continue...")
                continue
            file_name = input("Enter file name (without extension): ").strip() + ".secure"

            encrypt_note(message, key_input, read_time, file_name)
            input("\nPress Enter to continue...")

        elif choice == "2":
            file_name = input("Enter the note file name (with .secure extension): ").strip()
            key_input = input("Enter encryption key: ").encode('utf-8')
            decrypt_note(file_name, key_input)
            input("\nPress Enter to continue...")

        else:
            print("Invalid choice.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    run()
