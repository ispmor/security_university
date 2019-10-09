import fileinput
from sys import argv

key = ''.join(set(argv[1])) if len(argv) > 1 else ''.join([chr(i) for i in range(70, 80)])
file = argv[2] if len(argv) > 2 else "text.txt"
rows = len(key)
table = [[chr((ord(starting) + i) % 256) for i in range(0, 255)] for starting in key]
letter_count = 0
for line in fileinput.input(file):
    translated = ''
    for letter in line.strip():
        translated = translated + table[letter_count % rows][ord(letter)]
        letter_count = letter_count + 1
    print(translated)