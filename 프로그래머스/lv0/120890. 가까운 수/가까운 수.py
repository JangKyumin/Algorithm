def solution(array, n):
    value_group = {}
    for i in range(len(array)):
        value = n - array[i] if n > array[i] else array[i] - n
        if value not in value_group:
            value_group[value] = [array[i]]
        else:
            value_group[value].append(array[i])
    return min(value_group.get(min(value_group.keys())))