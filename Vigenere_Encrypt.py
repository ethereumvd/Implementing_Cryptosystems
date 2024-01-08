def get_user_input():
	message= input("Enter your message : ")
	key=input("Enter the key : ")
	return message,key

def generate_vigenere_key(message, key):
    key_length = len(key)
    repeated_key = (key * (len(message) // key_length)) + key[:len(message) % key_length]
    return repeated_key


def cipherText(message, key):
	vigenere_key = generate_vigenere_key(message, key)

	cipher_text = []
	for i in range(len(message)):
		x = (ord(message[i]) +
			ord(vigenere_key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))
 
