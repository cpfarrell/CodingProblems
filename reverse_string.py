def reverse(text):
    new_word = []
    i = len(text) - 1
    while i>= 0:
        if not text[i].isspace():
            j = beg_word(text, i)
            new_word.append(text[j:i+1] + " ")
            i = j
        i-=1
    output = ""
    for word in new_word:
        output += word
    return output[:-1]

def beg_word(word, i):
    for k in range(i, -1, -1):
        if word[k].isspace():
            return k+1

    return 0

print reverse("I love coding")
print reverse("lets see if   this works!      ok?")
