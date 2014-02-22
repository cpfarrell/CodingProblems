def remove_dup(text):
    chars = set([])
    output = []
    for char in text:
        if char not in chars:
            output.append(char)
            chars.add(char)
    return ''.join(output)

print remove_dup("tree traversal")
print remove_dup("a")
print remove_dup("aa")
print remove_dup("ababa")
