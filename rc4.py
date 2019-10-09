import fileinput
from Crypto.Cipher import ARC4

key = "password"
secret = "total secret"
cipher = ARC4.new(key)
encrypted = cipher.encrypt(secret)
print([format(x, "02x") for x in bytearray(encrypted)])

# manual approach
def generateCypheringRegister(key):
    key_length = len(key)
    S = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def provideCypheringStreamGenerator(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key):
    S = generateCypheringRegister(key)
    return provideCypheringStreamGenerator(S)


if __name__ == '__main__':
    def convert_key(s):
        return [ord(c) for c in s]
    key = convert_key(key)
    keystream = RC4(key)

    result = []
    for c in secret:
        result += ["%02X" % (ord(c) ^ next(keystream))]
    print(result)
