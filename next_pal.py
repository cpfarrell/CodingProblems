def next_pal(number):
    number = [c for c in str(number + 1)]
    n = len(number)
    if n<2:
        return int(number[0])

    left = int(n/2)-1
    right = left + 1
    if n%2==1:
        right += 1
    next(left, right, number)
    return int(''.join(n for n in number))

def next(left, right, number):
    if left<0:
        return number

    if number[left]==number[right]:
        return next(left-1, right+1, number)

    if number[left]<number[right]:
        inc_center(number)

    sync(mid_idx(number), number)

def mid_idx(number):
    return (len(number)+1)/2 - 1

def inc_center(number):
    inc_number(mid_idx(number), number)

def inc_number(idx, number):
    new = int(number[idx])+1
    if new<10:
        number[idx] = str(new)
    else:
        number[idx] = "0"
        inc_number(idx-1, number)

def sync(left, number):
    n = len(number)-1
    for i in range(left+1):
        number[n-i] = number[i]

assert next_pal(0) == 1
assert next_pal(1) == 2
assert next_pal(8) == 9
assert next_pal(9) == 11
assert next_pal(1234) == 1331
assert next_pal(1324) == 1331
assert next_pal(12345) == 12421
assert next_pal(14325) == 14341
assert next_pal(194) == 202
assert next_pal(990) == 999
print next_pal(1997)
print next_pal(2001)
print next_pal(1091)
