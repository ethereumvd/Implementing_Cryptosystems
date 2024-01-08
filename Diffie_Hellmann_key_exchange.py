import random
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.backends import default_backend


def generate_key(prime, primitive_root, private_key):
    public_key = pow(primitive_root, private_key, prime)
    return public_key

def calculate_shared_secret(public_key, private_key, prime):
    shared_secret = pow(public_key, private_key, prime)
    return shared_secret

def generate_prime_and_primitive_root(bits):

    parameters = dh.generate_parameters(generator=5, key_size=bits, backend=default_backend())
    prime = parameters.parameter_numbers().p

    primitive_root = find_primitive_root(prime)

    return prime, primitive_root

def find_primitive_root(prime):
    for candidate in range(2, prime - 1):
        if pow(candidate, (prime - 1) // 2, prime) != 1 and pow(candidate, prime - 1, prime) == 1:
            return candidate

    raise ValueError("Primitive root not found")

bit_length = 1024

prime, primitive_root = generate_prime_and_primitive_root(bit_length)

print(f"Generated",bit_length,f"bit prime: {prime}")
print(f"Primitive root: {primitive_root}")

private_key_alice = random.randint(2, prime)

private_key_bob = random.randint(2, prime)

public_key_alice = generate_key(prime, primitive_root, private_key_alice)

public_key_bob = generate_key(prime, primitive_root, private_key_bob)

shared_secret_alice = calculate_shared_secret(public_key_bob, private_key_alice, prime)

shared_secret_bob = calculate_shared_secret(public_key_alice, private_key_bob, prime)
