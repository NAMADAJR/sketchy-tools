from PIL import Image
from stegano import lsb
import os

ASSET_IMAGE_PATH = "lib/tools/assets/picmsg/stitch.png"
ENCODED_IMAGE_PATH = "lib/tools/assets/picmsg/lilo.png"

def encode_message():
    message = input("Enter the message to hide: ")

    try:
        image = Image.open(ASSET_IMAGE_PATH)
        if image.mode != 'RGB':
            print(f"The image mode is {image.mode}, converting to RGB...")
            image = image.convert('RGB')
            image.save(ASSET_IMAGE_PATH)

        stego_image = lsb.hide(ASSET_IMAGE_PATH, message)
        stego_image.save(ENCODED_IMAGE_PATH)
        print(f"✅ Message encoded and saved as {ENCODED_IMAGE_PATH}")

    except Exception as e:
        print(f"❌ Error: {e}")

    input("Press Enter to continue...")

def decode_message():
    image_path = input("Enter the local image file path to decode: ")
    if not os.path.exists(image_path):
        print("❌ File does not exist.")
        input("Press Enter to continue...")
        return

    try:
        message = lsb.reveal(image_path)
        if message:
            print(f"📨 Hidden message: {message}")
        else:
            print("❌ No hidden message found.")
    except Exception as e:
        print(f"❌ Error: {e}")

    input("Press Enter to continue...")

def run():
    while True:
        os.system("clear")
        print("🎨 Steganography(Images)")
        print("1. Hide a message (encode)")
        print("2. Extract a message (decode)")
        print("0. Back")
        choice = input("Select an option: ")

        if choice == '1':
            encode_message()
        elif choice == '2':
            decode_message()
        elif choice == '0':
            break
        else:
            print("Invalid option. Try again.")
            input("Press Enter to continue...")
