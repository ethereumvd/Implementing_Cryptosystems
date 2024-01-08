print('''Please choose your desired cryptographic system
Enter 1 for Caesar encryption
Enter 2 for Vigenere encryption 
Enter 3 for Caesar decryption
Enter 4 for Vigenere decryption
Enter 5 for Atbash cipher 
Enter 6 for Diffie Hellman key exchange''')

def main():
    choice = int(input("Enter your choice: "))

    if choice == 1:
        
        from Caesar_Encrypt import caesar_cipher
        message = input("Enter your message: ")
        shift = int(input("Number of positions to shift: "))
        encrypted_message = caesar_cipher(message, shift)
        print(f"Encrypted message: {encrypted_message}")

    elif choice == 2:
        
        from Vigenere_Encrypt import generate_vigenere_key, cipherText 
        message = input("Enter your message: ").upper()
        key = input("Enter the key: ").upper()
        vigenere_key = generate_vigenere_key(message, key)
        cipher_text = cipherText(message, key)
        print(f"Cipher text: {cipher_text}")
    
    elif choice == 3:
        
        from Caesar_Decrypt import caesar_cipher 
        encrypted_message = input("Enter the encrypted message: ")
        shift_used = int(input("Enter the number of positions the letters were shifted: "))
        decrypted_message = caesar_cipher(encrypted_message, -shift_used)
        print(f"Decrypted message : {decrypted_message}")
    
    elif choice == 4:
        
        from Vigenere_Decrypt import generate_vigenere_key , originalText
        message = input("Enter the message : ").upper()
        key = input("Enter the key : ").upper()
        vigenere_key = generate_vigenere_key(message, key)
        original_text = originalText(message, key)
        print(f"Original message is : {original_text}")

    elif choice == 5:
        
        from Atbash_Cipher import atbash
        message = input("Enter the message to encrypt: ").upper()
        encrypted_message = atbash(message)
        print(f"Atbash encrypted message: {encrypted_message}")

        message_to_decrypt = input("Enter the message to decrypt: ").upper()
        decrypted_message = atbash(message_to_decrypt)
        print(f"Atbash decrypted message: {decrypted_message}")

    elif choice == 6:
        
        from Diffie_Hellmann_key_exchange import generate_key , generate_prime_and_primitive_root, calculate_shared_secret ,find_primitive_root ,random
        
        bit_length = 1024
        prime, primitive_root = generate_prime_and_primitive_root(bit_length)
        print("Generated",bit_length,f"bit prime: {prime}")
        print(f"Primitive root: {primitive_root}")
        private_key_alice = random.randint(2, prime)
        private_key_bob = random.randint(2, prime)
        public_key_alice = generate_key(prime, primitive_root, private_key_alice)
        public_key_bob = generate_key(prime, primitive_root, private_key_bob)
        shared_secret_alice = calculate_shared_secret(public_key_bob, private_key_alice, prime)
        shared_secret_bob = calculate_shared_secret(public_key_alice, private_key_bob, prime)
        print("Public key of Alice:", public_key_alice)
        print("Public key of Bob:", public_key_bob)
        print("Shared secret for Alice:", shared_secret_alice)
        print("Shared secret for Bob:", shared_secret_bob)
    

    
if __name__ == "__main__":
    main()
