def sq_root(val):
    return bin_search(val, 0, int(val)+1)

def bin_search(val, low, high):
    if (high-low)<2:
        return low

    mid = low + (high - low)/2
    if val < mid*mid:
        return bin_search(val, low, mid)
    else:
        return bin_search(val, mid, high)

print sq_root(13)
print sq_root(18)
print sq_root(25)
print sq_root(0.1)
print sq_root(1.1)
print sq_root(0)
print sq_root(1)
