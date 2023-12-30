Reference = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
                'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
                'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
                'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
                'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}
def atbash(message):
    cipher = ''
    for letter in message:
    
        if letter != ' ':
        
            cipher += Reference[letter]
        else:
          
         cipher += ' '

    return cipher

def main():

    message = input("Enter the message to encrypt: ").upper()
    encrypted_message = atbash(message)
    print(f"Atbash encrypted message: {encrypted_message}")

    message_to_decrypt = input("Enter the message to decrypt: ").upper()
    decrypted_message = atbash(message_to_decrypt)
    print(f"Atbash decrypted message: {decrypted_message}")

if __name__ == '__main__':
    main()