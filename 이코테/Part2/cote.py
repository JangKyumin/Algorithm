"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


def solution(A):
    A.sort()
    temp = 0
    state = True

    for a in set(A):
        if a < 0:
            temp = 1
            continue

        if not temp:
            temp = a

        if a - temp > 1:
            temp += 1
            state = False
        else:
            temp = a

        if state and A[-1] == a:
            temp = a + 1

    return temp


def solution2(A):
    positive_set = set()
    for i in A:
        if i > 0:
            positive_set.add(i)

    positive_A = list(positive_set)
    positive_A.sort()

    missing_int = 1
    for i in positive_A:
        if missing_int < i:
            break
        else:
            missing_int += 1

    return missing_int


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))
