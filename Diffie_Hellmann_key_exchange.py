import random
def generate_key(p, g, private_key):
    public_key = pow(g, private_key, p)
    return public_key

def calculate_shared_secret(public_key, private_key, p):
    shared_secret = pow(public_key, private_key, p)
    return shared_secret

def main():
    p = 23  # Usually a much larger prime number will be used
    g = 5   # The common primitive root of p
    
    private_key_alice = random.randint(2, p - 2)

    private_key_bob = random.randint(2, p - 2)

    public_key_alice = generate_key(p, g, private_key_alice)
    public_key_bob = generate_key(p, g, private_key_bob)

    shared_secret_alice = calculate_shared_secret(public_key_bob, private_key_alice, p)
    shared_secret_bob = calculate_shared_secret(public_key_alice, private_key_bob, p)

    print("Public key of Alice:", public_key_alice)
    print("Public key of Bob:", public_key_bob)
    print("Shared secret for Alice:", shared_secret_alice)
    print("Shared secret for Bob:", shared_secret_bob)

if __name__ == "__main__":
    main()