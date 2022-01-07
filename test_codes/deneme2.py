
"""
For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""
def solution(s1, s2):
    list_s1 = list(s1)
    list_s2 = list(s2)

    list_s1.sort()
    list_s2.sort()

    same_word = 0

    for i, j in enumerate(list_s1):
        if j in list_s2:
            same_word+=1
            list_s2.remove(j)

    return same_word



print(solution("aabcc", "adcaa"))