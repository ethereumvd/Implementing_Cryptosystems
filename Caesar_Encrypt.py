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
    message = input("Enter your message: ")
    
    shift = int(input("Number of positions to shift: "))

    encrypted_message = caesar_cipher(message, shift)
    print(f"Encrypted message: {encrypted_message}")

if __name__ == "__main__":
    main()