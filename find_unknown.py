#Check if num below idx. True if idx out of range or idx value greater than num
def below(num, values, idx):
    try:
        idx_value = values[idx]
    except IndexError:
        return True
    return num < idx_value

#Find range containing num taking exponential steps
def find_range(num, values, start=0):
    end = 2*start + 1
    if below(num, values, end):
        return start, end
    else:
        return find_range(num, values, end)

#Binary search allowing for index error through below function
def bi_search(num, values, start, end):
    mid = start + (end-start)/2
    if below(num, values, mid):
        return bi_search(num, values, start, mid)
    elif values[mid]==num:
        return mid
    else:
        #Edge case if num not in values
        if mid==start:
            return -1
        else:
            return bi_search(num, values, mid, end)

#Find index of num in sorted array of unknown length
def find_unknown(num, values):
    start, end = find_range(num, values)
    return bi_search(num, values, start, end)

assert find_unknown(0, [0,1,3,4,6,8])==0
assert find_unknown(1, [0,1,3,4,6,8])==1
assert find_unknown(3, [0,1,3,4,6,8])==2
assert find_unknown(4, [0,1,3,4,6,8])==3
assert find_unknown(6, [0,1,3,4,6,8])==4
assert find_unknown(8, [0,1,3,4,6,8])==5
assert find_unknown(7, [0,1,3,4,6,8])==-1
