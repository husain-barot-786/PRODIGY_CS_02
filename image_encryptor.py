# Pixel-Based Image Encryption and Decryption using XOR

from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    """
    Encrypts an image by applying XOR to each pixel with a given key.
    
    Parameters:
    - input_path (str): Path to the original image.
    - output_path (str): Path to save the encrypted image.
    - key (int): Integer key used for XOR encryption (0-255).
    """
    img = Image.open(input_path)
    img = img.convert("RGB")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # XOR each color channel with the key
            pixels[x, y] = (
                r ^ key,
                g ^ key,
                b ^ key
            )

    img.save(output_path)
    print(f"[+] Encrypted image saved to: {output_path}")

def decrypt_image(input_path, output_path, key):
    """
    Decrypts an XOR-encrypted image using the same key.
    
    Parameters:
    - input_path (str): Path to the encrypted image.
    - output_path (str): Path to save the decrypted image.
    - key (int): Integer key used for XOR decryption (same as encryption).
    """
    # XORing again with the same key reverses the encryption
    encrypt_image(input_path, output_path, key)
    print(f"[+] Decrypted image saved to: {output_path}")

def main():
    print("==== Image Encryption and Decryption Tool ====")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Choose an option (1/2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        return

    input_path = input("Enter path of the image file: ").strip()
    if not os.path.exists(input_path):
        print("Error: File not found.")
        return

    key = input("Enter encryption/decryption key (0-255): ").strip()
    if not key.isdigit() or not (0 <= int(key) <= 255):
        print("Error: Key must be an integer between 0 and 255.")
        return

    key = int(key)

    if choice == '1':
        output_path = input("Enter output path for encrypted image: ").strip()
        encrypt_image(input_path, output_path, key)
    else:
        output_path = input("Enter output path for decrypted image: ").strip()
        decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
  
