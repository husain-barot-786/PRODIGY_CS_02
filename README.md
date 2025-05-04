# PRODIGY_CS_02
A simple image encryption and decryption tool using XOR-based pixel manipulation.

# Image Encryption and Decryption using Pixel Manipulation

## Description

This project is a lightweight Python tool that performs encryption and decryption on images using pixel-level XOR manipulation. The program reads each pixel’s RGB values and applies a user-defined key (0–255) using the XOR operation. Using the same key again restores the original image. This tool is ideal for demonstrating how basic cryptographic operations can be applied to multimedia files like images.

---

## Objective

- To implement simple yet effective image encryption using XOR.
- To understand how pixel data in images can be manipulated securely.
- To demonstrate reversible multimedia encryption logic.

---

## Requirements

- Python 3.x
- Pillow Library

### Install Pillow:

```bash
pip install pillow
```

---

## How to Use

1. Clone or download this repository.
2. Run the script:

```bash
python image_encryptor.py
```

3. Follow the prompts:
   - Choose Encrypt or Decrypt
   - Provide the image path
   - Enter a key (0–255)
   - Provide the output image path

---

## Example

```bash
==== Image Encryption and Decryption Tool ====
1. Encrypt Image
2. Decrypt Image
Choose an option (1/2): 1
Enter path of the image file: sample.jpg
Enter encryption/decryption key (0-255): 100
Enter output path for encrypted image: encrypted.png
[+] Encrypted image saved to: encrypted.png
```

---

## Files

- `image_encryptor.py` – Main Python script
- `README.md` – Project documentation

---

## Note

This encryption method is not suitable for production. XOR is reversible but weak for high-security applications. Use AES or other modern encryption for real-world scenarios.

---
