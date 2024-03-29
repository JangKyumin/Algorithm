"""
    0 0 1
    0 1 0
    1 0 1

    (0, 0)에서 시작하여 상하좌우를 다 체크하고 한 묶음으로 생각한다.
    (0, 0), (0, 1), (1, 0) 이 하나의 얼음 (1, 2)와 (2, 1) 이 각각 하나의 얼음이다.

"""
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x: int, y: int):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)  # 상
        dfs(x, y - 1)  # 좌
        dfs(x + 1, y)  # 하
        dfs(x, y + 1)  # 우
        return True
    return False


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j):
            result += 1

print(result)  # 정답 출력
