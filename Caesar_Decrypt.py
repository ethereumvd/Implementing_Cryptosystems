def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            result += char
    return result

def main():
    encrypted_message = input("Enter the encrypted message: ")
    shift_used = int(input("Enter the number of positions the letters were shifted: "))
    
    decrypted_message = caesar_cipher(encrypted_message, -shift_used)
    
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
