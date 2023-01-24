def solution(my_string):
    answer = ''
    for string in my_string:
        if string.islower():
            answer += string.upper()
        else:
            answer += string.lower()
    return answer