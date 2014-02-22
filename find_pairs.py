def add_key(pairs, key, spot):
    insert = [0,0]
    if key in pairs:
        insert = list(pairs[key])
    insert[spot] += 1
    pairs[key] = tuple(insert)

def find_pairs(values, k):
    a = k/2;
    pairs = {}
    for val in values:
        if val <= a:
            add_key(pairs, val, 0)
        else:
            add_key(pairs, k-val, 1)

    matches=0
    if k%2==0:
        halves = pairs[a][0]
        matches = halves*(halves-1)/2
        
    for key in pairs:
        info = pairs[key]
        matches += info[0]*info[1]

    return matches
    
values = [3,-4,9,-4,-3,-9,0,0,0]
print find_pairs(values, 0)
