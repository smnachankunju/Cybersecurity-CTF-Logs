import hashlib

# Ciphertext from bytecode
val = [101, 105, 100, 96, 118, 125, 116, 101, 123, 37, 
       121, 120, 120, 104, 106, 20, 108, 103, 107, 114, 
       106, 62, 122, 112, 112, 123, 121, 105, 106, 102, 
       116, 79, 106, 122]

# Reconstruct keystream (aharray)
aharray, x = [], 0
for _ in range(16):
    aharray.append(x + 2)
    x += 2

# Decryption: Functional inverse identified as (val ^ key) - 1
flag = "".join(chr((val[i] ^ aharray[i % 16]) - 1) for i in range(len(val)))

print(f"Flag: {flag}")

# Hash Verification
assert hashlib.sha256(flag.encode()).hexdigest() == \
    "abd6177c760bed2e078e2ff804f5da70664f0df4d293e238d623231a6d7f6f49"
