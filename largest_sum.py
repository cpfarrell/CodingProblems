import sys

def largest_sum(vals):
    min=0
    max=-1*sys.maxint
    max_sum=-1*sys.maxint
    sum=0
    count=0

    for val in vals:
        count+=1
        sum+=val
        if sum>max or count==1:
            max=sum

        #New min, reset partial sum
        if sum<=min:
            if (max-min)>max_sum:
                max_sum=max-min

            min=val
            max=val
            sum=val
            count=0

    #Add ending sum
    if (max-min)>max_sum and count>0:
        max_sum=(max-min)

    return max_sum

print largest_sum([1,0,4,3])
print largest_sum([2,4,-3,5])
print largest_sum([2,4,-8,5])
print largest_sum([2,4,-8,5,-6,3])
print largest_sum([2,4,-8,5,4,-6,3])
print largest_sum([-3,-2,-1])
print largest_sum([-3,-2,-1,0])
print largest_sum([-3,-2,-1,0,1])
