def print_n_k(n,k,exclude=[]):
    for i in range(n):
        if i in exclude:
            continue
        exclude.append(i)
        if k==1:
            print exclude
        else:
            print_n_k(n,k-1, exclude)

        exclude.pop()

print_n_k(5,5)
        
