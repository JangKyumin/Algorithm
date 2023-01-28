import re

def solution(my_string):
    return sum([int(i) for i in re.findall(r'\d+', my_string)])