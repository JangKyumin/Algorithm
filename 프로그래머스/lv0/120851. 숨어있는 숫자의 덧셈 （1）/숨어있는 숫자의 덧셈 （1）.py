def solution(my_string):
    answer = 0
    for string in my_string:
        if string.isnumeric():
            answer += int(string)
    return answer