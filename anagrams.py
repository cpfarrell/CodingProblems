from collections import defaultdict
import string

def letters(word):
    return [char for char in word if char in string.lowercase]

def anagrams(word1, word2):
    counts = defaultdict(int)
    word1 = letters(word1.lower())
    word2 = letters(word2.lower())

    if len(word1)!=len(word2):
        return False

    for char in word1:
        counts[char]+=1

    for char in word2:
        counts[char]-=1
        if counts[char]<0:
            return False

    return True

print anagrams("god", "dog")
print anagrams("god", "dod")
print anagrams("god", "dogs")
print anagrams("gods", "dog")
print anagrams("", "a")
print anagrams("a", "")
print anagrams("", "")
