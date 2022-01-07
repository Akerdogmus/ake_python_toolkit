
def solution(n):
    sum = 0
    print(list(str(n)))
    for i, j in enumerate(list(str(n))):
        sum+=int(j)
    return sum

print(solution(11))