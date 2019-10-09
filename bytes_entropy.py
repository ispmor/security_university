from Crypto.Cipher import ARC4
import math

key = "passwordtotale"
chain = "a traditional Chinese story, are both relativelcomplex and demonstrate not only the evolution of the White Snake figure to become amore believable human, but also what aspects may have given her enduring appeal. While both these stories are ostensibly morality tales about the dangerous beauty ofthis femme fatale, the true source of pleasure from these narratives is the femmefatale’s transgressive behavior, not her eventual punishment for it. Early tales of Madame White Snake appeared in China as early as the Song Dynasty, andinitially her portrayal was fairly direct, as a villainous demon who drains the lifeforce out of her human husband.Lai, Whalen. ".replace(" ", "")
cipher = ARC4.new(key)
print(chain)
encrypted = cipher.encrypt(chain)
encrypted = ''.join([format(x, "02x") for x in bytearray(encrypted)])
total_sign_count = 0
stat = {}
possibilities_natural = {}
for sign in chain:
    if sign in stat:
        stat[sign] += 1
    else:
        stat[sign] = 1
    total_sign_count += 1
for key, value in stat.items():
    possibilities_natural[key] = value / total_sign_count
entropy_natural = -sum([possibilities_natural[x] * math.log(possibilities_natural[x], 2) for x in chain])

stat_crypted = {}
possibilities_crypted = {}
total_sign_count = 0
for sign in encrypted:
    if sign in stat_crypted:
        stat_crypted[sign] += 1
    else:
        stat_crypted[sign] = 1
    total_sign_count += 1
for key, value in stat_crypted.items():
    possibilities_crypted[key] = value / total_sign_count
entropy_crypted = -sum([possibilities_crypted[x] * math.log(possibilities_crypted[x], 2) for x in encrypted])

print(possibilities_natural)
print(possibilities_crypted)
print("Entropy of the natural language: {}, \nEntropy of the encrypted text: {}".format(entropy_natural, entropy_crypted))
