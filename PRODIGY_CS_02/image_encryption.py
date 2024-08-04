from PIL import Image

def encrypt_image(image_path, key):
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Get image dimensions
        width, height = img.size
        
        # Create a new image with the same dimensions
        encrypted_img = Image.new(img.mode, (width, height))
        
        # Encrypt each pixel
        for y in range(height):
            for x in range(width):
                # Get the pixel value
                pixel = img.getpixel((x, y))
                
                # Encrypt the pixel value
                encrypted_pixel = tuple((p + key) % 256 for p in pixel)
                
                # Set the encrypted pixel value in the new image
                encrypted_img.putpixel((x, y), encrypted_pixel)
        
        # Save the encrypted image
        encrypted_path = image_path.split('.')[0] + '_encrypted.png'
        encrypted_img.save(encrypted_path)
        
        return encrypted_path
    
    except Exception as e:
        print("Error:", e)
        return None

def decrypt_image(image_path, key):
    try:
        # Open the encrypted image
        encrypted_img = Image.open(image_path)
        
        # Get image dimensions
        width, height = encrypted_img.size
        
        # Create a new image with the same dimensions
        decrypted_img = Image.new(encrypted_img.mode, (width, height))
        
        # Decrypt each pixel
        for y in range(height):
            for x in range(width):
                # Get the encrypted pixel value
                encrypted_pixel = encrypted_img.getpixel((x, y))
                
                # Decrypt the pixel value
                decrypted_pixel = tuple((p - key) % 256 for p in encrypted_pixel)
                
                # Set the decrypted pixel value in the new image
                decrypted_img.putpixel((x, y), decrypted_pixel)
        
        # Save the decrypted image
        decrypted_path = image_path.split('.')[0] + '_decrypted.png'
        decrypted_img.save(decrypted_path)
        
        return decrypted_path
    
    except Exception as e:
        print("Error:", e)
        return None

def main():
    print("Image Encryption and Decryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        image_path = input("Enter the path of the image to encrypt: ")
        key = int(input("Enter the encryption key (0-255): "))
        encrypted_path = encrypt_image(image_path, key)
        if encrypted_path:
            print("Image encrypted successfully. Encrypted image saved at:", encrypted_path)
        else:
            print("Failed to encrypt image.")
    
    elif choice == '2':
        image_path = input("Enter the path of the encrypted image to decrypt: ")
        key = int(input("Enter the decryption key (0-255): "))
        decrypted_path = decrypt_image(image_path, key)
        if decrypted_path:
            print("Image decrypted successfully. Decrypted image saved at:", decrypted_path)
        else:
            print("Failed to decrypt image.")
    
    elif choice == '3':
        print("Exiting...")
    
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
