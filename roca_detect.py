# sage -python detect_roca.py

# Necessary imports / headers
from math import ceil, log, floor
from Crypto.Util.number import getRandomNBitInteger, isPrime as is_prime, getPrime
from sympy import nextprime as next_prime
from sage.all import Zmod   # requires running under sage -python

# ----- Primorial / weak-key helpers-----

def compute_primorial(count):
    product = 1
    prime_cursor = 1
    for _ in range(count):
        prime_cursor = next_prime(prime_cursor)
        product *= prime_cursor
    return int(product)

def derive_parameters(key_bits):
    if 512 <= key_bits <= 960:
        n = 39
    elif 992 <= key_bits <= 1952:
        n = 71
    elif 1984 <= key_bits <= 3936:
        n = 126
    elif 3968 <= key_bits <= 4096:
        n = 225
    else:
        return None
    M = compute_primorial(n)
    k_bits = key_bits // 2 - round(log(M, 2))
    g_order = Zmod(M)(65537).multiplicative_order()
    a_bits = ceil(log(g_order, 2))
    return M, k_bits, a_bits

def generate_weak_prime(M, k_bits, a_bits):
    p = 0
    while not is_prime(p):
        k_val = getRandomNBitInteger(k_bits)
        a_val = getRandomNBitInteger(a_bits)
        p = k_val * M + pow(65537, a_val, M)
    return p

def generate_weak_modulus(size_bits):
    params = derive_parameters(size_bits)
    if params is None:
        raise ValueError("Unsupported key size.")
    M, k_bits, a_bits = params
    modulus = 0
    while modulus.bit_length() != size_bits:
        p1 = generate_weak_prime(M, k_bits, a_bits)
        p2 = generate_weak_prime(M, k_bits, a_bits)
        modulus = p1 * p2
    return modulus

# ----- ROCA detection function (uses Pohlig-Hellman via SageZmod.log) -----

def detect_roca_vulnerability(n):
    params = derive_parameters(n.bit_length())
    if params is None:
        return False
    M = params[0]
    try:
        exponent_val = Zmod(M)(n).log(65537)
        print(f"Vulnerable key detected! Exponent a = {exponent_val}")
        return True
    except ValueError:
        print("Key is not vulnerable to ROCA.")
        return False

# ----- Demo / tests -----
if __name__ == "__main__":
    # Test a known weak key (generated with the same procedure)
    print()
    vulnerable_modulus = generate_weak_modulus(512)
    print("Testing vulnerable (generated) modulus:")
    detect_roca_vulnerability(vulnerable_modulus)
    print()

    # Test a secure key (random primes)
    secure_modulus = int(getPrime(300) * getPrime(300))
    print("Testing a random secure modulus:")
    detect_roca_vulnerability(secure_modulus)
    print()