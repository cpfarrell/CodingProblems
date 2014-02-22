def even_elements(values):
    seen = set()
    #Add once to make for even, odd would not do this
    for val in values:
        seen.add(val)

    for val in values:
        if val in seen:
            seen.remove(val)
        else:
            seen.add(val)
    if len(seen)!=1:
        print "Input list contains " + str(len(seen)) + " even occurences"
    return seen.pop()

print even_elements([2,2,3,3,3])
