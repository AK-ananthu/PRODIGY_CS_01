def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift letters
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep spaces and symbols unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Main program
print("=== Caesar Cipher Encryption/Decryption ===")
choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))

if choice == 'E':
    encrypted_text = encrypt(message, shift)
    print("Encrypted message:", encrypted_text)
elif choice == 'D':
    decrypted_text = decrypt(message, shift)
    print("Decrypted message:", decrypted_text)
else:
    print("Invalid choice! Please choose 'E
