def generate_vigenere_key(message, key):
    key_length = len(key)
    repeated_key = (key * (len(message) // key_length)) + key[:len(message) % key_length]
    return repeated_key

message = input("Enter the message : ").upper()

key = input("Enter the key : ").upper()

vigenere_key = generate_vigenere_key(message, key)

def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(vigenere_key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))

original_text = originalText(message, key)
