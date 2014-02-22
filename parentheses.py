def parentheses(word):
    matching = {"}":"{", ")":"(", "]":"["}
    open = set(["{", "(", "["])
    close = set(["}", ")", "]"])
    stack = []

    for char in word:
        if char in close:
            if len(stack)==0:
                return False
            next = stack.pop()
            if matching[char]!=next:
                return False

        elif char in open:
            stack.append(char)

    if len(stack)==0:
        return True
    else:
        return False

print parentheses("[{}]()")
print parentheses("[[{}]()")
print parentheses("[{}]()]")
print parentheses(")")
print parentheses("[{rt}43](s33)")
