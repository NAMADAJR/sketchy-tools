import os

ZERO_WIDTH_SPACE = '\u200B'  # 0
ZERO_WIDTH_NON_JOINER = '\u200C'  # 1

ASSETS_PATH = "lib/tools/assets/invisible_text/"
os.makedirs(ASSETS_PATH, exist_ok=True)

def encode_message(message, cover_text, output_file):
    binary = ''.join(format(ord(c), '08b') for c in message)
    zwc_message = ''.join(ZERO_WIDTH_SPACE if bit == '0' else ZERO_WIDTH_NON_JOINER for bit in binary)

    stego_text = cover_text + zwc_message

    with open(os.path.join(ASSETS_PATH, output_file), 'w', encoding='utf-8') as f:
        f.write(stego_text)

    print(f"\n✅ Stego text saved as: {output_file}")

def decode_message(file_path):
    full_path = os.path.join(ASSETS_PATH, file_path)
    if not os.path.exists(full_path):
        print("❌ File not found.")
        return

    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    zwc_sequence = ''.join(c for c in content if c in (ZERO_WIDTH_SPACE, ZERO_WIDTH_NON_JOINER))

    binary = ''.join('0' if c == ZERO_WIDTH_SPACE else '1' for c in zwc_sequence)

    message = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

    print(f"\n📨 Hidden message:\n{message}")

def run():
    while True:
        os.system("clear")
        print("🕵️ Invisible Text Injector")
        print("1. Encode a message")
        print("2. Decode a message")
        print("0. Back")
        choice = input("Choose an option: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            cover_text = input("Enter the cover text (visible text): ")
            secret_message = input("Enter the secret message to hide: ")
            file_name = input("Enter output file name (without extension): ").strip() + ".txt"
            encode_message(secret_message, cover_text, file_name)
            input("\nPress Enter to continue...")
        elif choice == "2":
            file_name = input("Enter the file name to decode (with .txt extension): ").strip()
            decode_message(file_name)
            input("\nPress Enter to continue...")
        else:
            print("Invalid choice.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    run()
