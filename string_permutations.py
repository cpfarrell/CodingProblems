def print_perms(word, used_words, excluded=None, perm=[]):
    if not excluded:
        excluded = set([])

    for i in range(len(word)):
        if i not in excluded:
            excluded.add(i)
            perm.append(word[i])
            if len(perm)==len(word):
                output = list_print(perm)
                if output not in used_words:
                    used_words.add(output)
                    print output
            else:
                print_perms(word, used_words, excluded, perm)

            perm.pop()
            excluded.remove(i)

def list_print(chars):
    output = ""
    for char in chars:
        output += char.strip()
    return output

print_perms("abacsfrgs", set([]))
