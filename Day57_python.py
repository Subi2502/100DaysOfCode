#Implementation of Simple DES SBOX
print ("\nSubi - Day 57 of #100DaysOfCode\n") 
print("\nImplementation of Simple DES SBOX\n")

IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
S1 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]

S2 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]

P = [2, 4, 3, 1]

def permute(data, permutation):
    return [data[i - 1] for i in permutation]

def expand(data, expansion):
    return [data[i - 1] for i in expansion]

def sbox_substitution(data, sbox):
    row = int(str(data[0]) + str(data[3]), 2)
    col = int(str(data[1]) + str(data[2]), 2)
    return [int(bit) for bit in bin(sbox[row][col])[2:].zfill(2)]

def xor(data1, data2):
    return [bit1 ^ bit2 for bit1, bit2 in zip(data1, data2)]

def generate_subkeys(key):
    subkeys = []
    key = permute(key, [3, 5, 2, 7, 4, 10, 1, 9, 8, 6])
    left = key[:5]
    right = key[5:]

    for i in range(2):
        left = left[1:] + [left[0]]
        right = right[1:] + [right[0]]
        combined = left + right
        subkey = permute(combined, [6, 3, 7, 4, 8, 5, 10, 9])
        subkeys.append(subkey)
    return subkeys

def encrypt(plaintext, key):
    subkeys = generate_subkeys(key)
    plaintext = permute(plaintext, IP)
    left = plaintext[:4]
    right = plaintext[4:]

    for i in range(2):
        new_left = right
        expanded = expand(right, EP)
        xor_result = xor(expanded, subkeys[i])
        sbox_result = sbox_substitution(xor_result[:4], S1) + sbox_substitution(xor_result[4:], S2)
        permuted_result = permute(sbox_result, P)
        new_right = xor(left, permuted_result)
        left = new_left
        right = new_right
    ciphertext = right + left
    ciphertext = permute(ciphertext, IP_inv)
    return ciphertext

key = [0, 1, 0, 0, 0, 1, 1, 1, 1, 0]
plaintext = [1, 0, 1, 0, 0, 1, 0, 1]
ciphertext = encrypt(plaintext, key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)