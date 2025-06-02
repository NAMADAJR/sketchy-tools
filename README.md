# 📦 Sketchy Tools by Nam

A collection of fun, experimental, and offline-friendly Python tools built for personal security research, data experiments, and curiosity projects. All tools are local-only — no network dependencies, no cloud, just you and your machine.


## 📖 Overview

This toolkit is a growing playground of unconventional utilities — some useful, some mischievous, all fun to build. Everything runs locally in your terminal, with no external API calls.  

Built with:
- Python 🐍
- Cryptography 🔒
- Steganography 🖼️
- Encoding & Encryption experiments
- File system manipulation
- CLI interfaces

---

## 🧰 Included Tools

| #  | Tool                          | Description                                                        |
|:----|:-----------------------------|:--------------------------------------------------------------------|
| 1  | **Morse Code Encoder/Decoder** | Convert text to Morse and back.                                     |
| 2  | **Binary Text Converter**      | Convert text to binary and vice versa.                              |
| 3  | **Blowfish Encryptor**         | Encrypt and decrypt text with Blowfish cipher.                      |
| 4  | **Steganography (Images)**     | Hide/reveal messages inside images.                                 |
| 5  | **File Bomb Creator**          | Create nested folder/file bombs that expand massively on extraction.|
| 6  | **Self-Destructing Notes**     | Encrypted note that self-deletes after viewing.                     |                |
| 7  | **Invisible Text Injector**    | Hide zero-width characters inside text for secret messages.         |
| ...| *(space for more coming soon)* |                                                                     |

---

## ⚙️ Installation

1. Clone the repo  
```bash
git clone git@github.com:NAMADAJR/sketchy-tools.git
cd sketchy-tools
```

## ⚙️ Setup Instructions
- Make sure you have Python 3.7+ installed.
- Clone or download this repository.
- Navigate to the project folder in your terminal.

Create and activate a virtual environment (Optional but recommended):
```bash
python -m venv env
source env/bin/activate   # On Windows: venv\Scripts\activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

## 🚀 Usage  
Run the main tool menu:

```bash
python lib/cli.py
```

## 🖥️ Project Structure
```css
lib/
├── tools/
│   ├── assets/
│   │   └── [temporary files, notes, bombs etc.]
│   └── [individual tool scripts]
└─cli.py
  helpers.py
```

## 🙌 Credits
Built by Nam — just a curious tinkerer stacking up weird but useful tools for offline experiments.

## ⚠️ Disclaimer
This toolkit is for personal, ethical, and educational use only.
Do not use these tools for illegal, unethical, or unauthorized activities. You are solely responsible for how you use this project. Have fun.

