def solution(numbers):
    numbers.sort()
    numbers.reverse()
    return numbers[0] * numbers[1]