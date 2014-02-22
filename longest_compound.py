def is_compound(word, dictionary):
    valid_w = [False]*len(word)
    valid_c = [False]*len(word)
    for i,_ in enumerate(word):
        for j in reversed(range(i+1)):
            begin = i-j
            end = i+1
            if word[begin:end] in dictionary:
                if begin<1:
                    valid_w[i]=True
                elif valid_w[begin-1]:
                    valid_w[i]=True
                    valid_c[i]=True
    return valid_c[-1]


def longest_com(words):
    dictionary = set([])
    for word in words:
        dictionary.add(word)
    longest = ""
    for word in words:
        if len(word)<=len(longest):
            continue
        if is_compound(word, dictionary):
            longest = word

    return longest

words = ['cat', 'cats', 'catsdogcats', 'catxdogcatsrat', 'dog', 'dogcatsdog', 'hippopotamuses', 'rat', 'ratcat', 'ratcatdog', 'ratcatdogcat']
print longest_com(words)
                    
