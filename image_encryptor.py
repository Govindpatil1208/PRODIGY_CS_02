from PIL import Image

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    for i in range(image.size[0]):      # width
        for j in range(image.size[1]):  # height
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

# === Main Program ===
print("=== Image Encryptor ===")
choice = input("Choose (E)ncrypt or (D)ecrypt: ").strip().upper()
input_image = input("Enter path to input image (e.g., image.jpg): ")
output_image = input("Enter path for output image (e.g., output.jpg): ")
key = int(input("Enter numeric key (e.g., 10): "))

if choice == 'E':
    encrypt_image(input_image, output_image, key)
elif choice == 'D':
    decrypt_image(input_image, output_image, key)
else:
    print("Invalid choice!")
