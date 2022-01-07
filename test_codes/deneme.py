def solution(sequence):
    sol = []
    neg_sum = 0
    pos_sum = 0
    for i in range(len(sequence)):
        if (i+1) < len(sequence):
            x = sequence[i]
            y = sequence[i+1]
            print(x,y)
            if x > y:
                sol.append(-1) #azalma
            else:
                sol.append(1) #artma
    
    for i, j in enumerate(sol):
        if j == -1:
            neg_sum+=1
        else:
            pos_sum+=1
    print(sol)
    print("\n",neg_sum, pos_sum)
    if neg_sum %2 == 0:
        if neg_sum != 0:
            return False
        else:
            return True
    else:
        return True 
print(solution(sequence=[1, 2, 1, 2]))
