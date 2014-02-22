import string
from collections import defaultdict

words = defaultdict(list)

def build_hash(file):
    f = open(file, 'r')
    pos = 0
    for line in f.readlines():
        start = 0
        length = 0
        for i, char in enumerate(line):
            if char not in string.whitespace:
                length+=1
            else:
                if length>0:
                    words[line[start:start+length]].append(pos+start)
                    start+=length + 1
                else:
                    start+=1
                length = 0

                #In case word doesn't end with newline
        if length>0:
            words[line[start:start+length]].append(pos+start)            
            start+=length
        pos += start


build_hash("text.txt")
print words["dog"]
print words["there"]
print words["a"]
