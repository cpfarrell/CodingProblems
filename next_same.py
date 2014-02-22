def next_same(number):
    number_str = str(number)
    counts = [0]*10
    larger = [False]*10
    for i, c in enumerate(reversed(number_str)):
        digit = int(c)
        counts[digit]+=1
        if larger[digit]:
            return combine(number_str, i, digit, counts)
        else:
            for j in reversed(range(digit)):
                if larger[j]:
                    break
                else:
                    larger[j]=True

def combine(number_str, i, digit, counts):
    end = len(number_str) - i - 1
    output = number_str[:end]
    next_num = next_count(digit, counts)
    counts[next_num]-=1
    output += str(next_num)
    for i in range(10):
        output += str(i)*counts[i]
    return output

def next_count(digit, counts):
    for i in range(digit+1, 10):
        if counts[i]>0:
            return i

print next_same(45342)
print next_same(9)
print next_same(12)
print next_same(1234)
print next_same(43215)
print next_same(5654321)
