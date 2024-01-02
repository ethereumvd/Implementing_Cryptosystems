## Implementing Cryptosystems

**Name - Vedant Das**

This repository contains python scripts that implement :-

1. **Caesar Cipher** :
It is a  substitution cipher in which the letters of the original message are all shifted by a fixed number of positions , to make it unreadable for any other person . To get the original message , we just reverse the shifting by the number of places the letters were originally shifted . This makes it very hard to read the original message as one will have to guess the shift amount to get to the original message . 

1. **Atbash Cipher** :
It is yet another substitution cipher where we replace the letters of the original message by the corresponding letters which are generated by reversing the alphabet system . For example A is replaced by Z , B is substituted by X and so on . This basically maps the letters of the aphabet , suppose the position of the alphabet is n in the alphabet system , then it replaces the letter by 26 - n + 1 th alphabet in the alphabet system . However , this type of cipher is unreliable as it can be easily decrypted .  

1. **Diffie-Hellmann Key Exchange**:
It is a efficient method to share cryptographic keys on a public (untrusted) channel . Both parties agree with two prime numbers say *g* and *n* (n is very large for security) .Now , each party generates a public key by raising *g* to the power of their selectedd private keys (say *a* and *b*) and taking modulus of *n* of that number . Then they exhange the public keys which are *g<sup>a</sup>mod n* and *g<sup>b</sup>mod n* which are available for everyone to see . Now both raise the public key to the power of their own private key to generate a common key that is *g<sup>ab</sup>mod n* which can be used for secure communication . It is efficient becaues for an attacker , it is impossible to figure out *a* and *b* with the help of *g<sup>a</sup>mod n* and *g<sup>b</sup>mod n* , *g* and *n*.

1. **RSA Encryption System** :
It is a public-key cryptosystem used for secure communication . Two keys are generated , where two large prime numbers are selected to create a public key where exponent and modulus functions are used , and a private key. We use recipient's public key to transform plaintext into ciphertext.It is secure as it is a very complex task to factor the product of these prime numbers . We decrypt it by using the private key . This asymmetric encryption scheme ensures secure communication, where the public key can be freely shared for encryption, but the private key remains confidential for decryption. 
