import fileinput
from os import walk
from sys import argv
import re

text_container = "written"
coded_file = argv[1] if len(argv) > 1 else "text_english_coded.txt"
stat = {}
total_sign_count = 0
for (dirpath, dirnames, filenames) in walk(text_container):
    for child_dir in dirnames:
        inner = dirpath + "/"+ child_dir
        for (parent_path, child_dirs, child_files) in walk(inner):
            for filename in child_files:
                for line in fileinput.input("{}/{}".format(inner, filename)):
                    line = re.sub(r'\s', '', line)
                    line.strip()
                    for sign in line:
                        if sign in stat:
                            stat[sign] += 1
                        else:
                            stat[sign] = 1
                        total_sign_count += 1

for sign in stat:
    stat[sign] = stat[sign] / total_sign_count

stat_tuple = [(key, value) for key, value in stat.items()]
sorted_stat_tuple = sorted(stat_tuple, key=lambda tuple: tuple[1], reverse= True)
for sign in sorted_stat_tuple:
        print("{} <=> {}".format(sign[0], stat[sign[0]]))

decrypted_stat = {}
total_sign_count = 0
for line in fileinput.input(coded_file):
    line = re.sub(r'\s', '', line)
    line.strip()
    for sign in line:
        total_sign_count += 1
        if sign in decrypted_stat:
            decrypted_stat[sign] += 1
        else:
            decrypted_stat[sign] = 1

for sign in decrypted_stat:
    decrypted_stat[sign] = decrypted_stat[sign] / total_sign_count

decrypted_stat_tuple = [(key, value) for key, value in decrypted_stat.items()]
decrypted_stat_tuple = sorted(decrypted_stat_tuple, key=lambda tup: tup[1], reverse= True)

cesar_key = abs(ord(decrypted_stat_tuple[0][0]) - ord(sorted_stat_tuple[0][0]))

for line in fileinput.input(coded_file):
    line = re.sub(r'\s', '', line)
    line.strip()
    result = []
    for sign in line:
        result += chr((ord(sign) - cesar_key))
    print("".join(result))