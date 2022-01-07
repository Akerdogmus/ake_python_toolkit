"""
Some people are standing in a row in a park. There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in a non-descending order without moving the
trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""
def solution(a):
    last_list = []
    sol_list = []

    for i,j in enumerate(a):
        sol_list.append(j)

    while -1 in sol_list:
        sol_list.remove(-1)
    
    sol_list.sort()
    x=0
    for i, j in enumerate(a):
        if j == -1:
            last_list.append(-1)
        else:
            last_list.append(sol_list[x])
            x+=1
    
    return last_list


print(solution([-1, 150, 190, 170, -1, -1, 160, 180]))