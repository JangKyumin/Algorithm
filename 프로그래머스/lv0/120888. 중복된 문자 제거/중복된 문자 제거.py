def solution(my_string):
    answer = ''
    for string in my_string:
        if string not in answer:
            answer += string
    return answer