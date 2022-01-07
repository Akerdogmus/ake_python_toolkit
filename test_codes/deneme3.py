"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first
half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

    For n = 1230, the output should be
    solution(n) = true;
    For n = 239017, the output should be
    solution(n) = false.
"""
def solution(n):
    list_num = list(str(n))
    split_len = int(len(list_num)/2)
    first_part = 0
    last_part = 0
    for i in range(split_len):
        first_part+= int(list_num[i])
    
    for i in range(split_len):
        last_part += int(list_num[i+split_len])

    if first_part == last_part:
        return True
    else:
        return False

print(solution(239017))