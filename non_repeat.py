from collections import defaultdict
def non_repeat(word):
    counts = defaultdict(int)
    for char in word:
        counts[char]+=1
    for char in word:
        if counts[char]==1:
            return char

print non_repeat("abacb")
print non_repeat("a")
print non_repeat("abab")
