def equal(weights):
    known = set([5])
    for weight in weights:
        if weight in known:
            return True
        else:
            for key in list(known):
                known.add(abs(weight - key))
    return False

print equal([2,4,1])
