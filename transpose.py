def old_to_new(index, M, N):
    row = int(index/N)
    column = index%N
    return column*M + row

def new_cycle(index, M, N):
    new_index = old_to_new(index, M, N)
    while new_index > index:
        new_index = old_to_new(new_index, M, N)
    return new_index==index

def transpose(vals, M, N):
    for index in range(len(vals)):
        if not new_cycle(index, M, N):
            continue

        new_index = old_to_new(index, M, N)
        temp_insert = vals[index]
        while new_index!=index:
            temp_hold = vals[new_index]
            vals[new_index] = temp_insert
            new_index = old_to_new(new_index, M, N)
            temp_insert = temp_hold

        vals[new_index] = temp_insert
        
    return vals


print transpose([0,1,2,3], 2, 2)
print transpose([0,1,2,3,4,5], 2, 3)
print transpose([0,1,2,3,4,5], 3, 2)
print transpose([0,1,2,3,4,5,6,7,8,9,10,11], 4, 3)
print transpose([0,1,2,3,4,5,6,7,8], 3, 3)
print transpose([0,1,2,3,4,5,6,7,8,9,10,11], 3, 4)
