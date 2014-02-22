def can_balance(weights, initial):
    #Might be possible with an array instead of set for better memory
    past_differences = set([initial])
    for weight in weights:
        if weight in past_differences:
            return True
        else:
            for old_diff in list(past_differences):
                past_differences.add(weight - old_diff)
                past_differences.add(weight + old_diff)
    return False

print can_balance([2,4,8,10,19], 5)
