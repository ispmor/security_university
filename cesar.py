import fileinput
import sys
result = []
key = sys.argv[1] if len(sys.argv) > 1 else 5
file = sys.argv[2] if len(sys.argv) > 2 else "text.txt"
table = str.maketrans(str.join('', [chr(value) for value in range(0, 256)]), str.join('', [chr((value + key) % 256) for value in range(0, 256)]))
for line in fileinput.input(file):
    line = line.strip()
    result += [str.translate(line, table)]

