def solution(lines):
    # answer = 0
    # for i in range(len(lines)):
    #     for j in range(i + 1, len(lines)):
    #         if lines[i][1] > lines[j][0]:
    #             if answer < lines[i][1] - lines[j][0]:
    #                 answer = lines[i][1] - lines[j][0]
    #             print(lines[j][0], lines[i][1], answer)
                
    table = [set([]) for i in range(200)]
    
    for index, line in enumerate(lines):
        a, b = line
        for i in range(a, b):
            table[i + 100].add(index)
    
    count = 0
    for line in table:
        if len(line) > 1:
            count += 1
    
    return count