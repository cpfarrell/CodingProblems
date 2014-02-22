def odd_element(values):
    sum = 0
    seen = set([])
    for val in values:
        if val in seen:
            seen.remove(val)
            sum -= val
        else:
            seen.add(val)
            sum += val
    return sum

print odd_element([4,6,4,7,7])
print odd_element([4,6,4,0,0])
print odd_element([4,6,4,0,6])
print odd_element([4,6,4,-1,-1])
print odd_element([4,6,4,-2,6])
print odd_element([1])
