import os

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': '/'
}
REVERSE_MORSE = {v: k for k, v in MORSE_CODE_DICT.items()}

def morse_encrypt(text):
    return ' '.join(MORSE_CODE_DICT.get(c.upper(), '') for c in text)

def morse_decrypt(code):
    return ''.join(REVERSE_MORSE.get(c, '') for c in code.split())

def run():
    while True:
        os.system("clear")
        print("🔐 Morse Code: Encrypt & Decrypt Text ")
        print("1. Encrypt Text to Morse")
        print("2. Decrypt Morse to Text")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "0":
            break
        elif choice == "1":
            text = input("\nEnter text(A-Z): ")
            result = morse_encrypt(text)
        elif choice == "2":
            code = input("\nEnter Morse code (space-separated): ")
            result = morse_decrypt(code)
        else:
            print("Invalid choice.")
            input("\nPress Enter to continue...")
            continue

        print("\n🔸 Result:\n")
        print(result)
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
