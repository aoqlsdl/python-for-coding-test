# unsolved
# 음료수 얼려 먹기

# 세로, 가로 길이 받기
n, m = map(int, input().split())

# DFS로 구현해보기
# 1. 상하좌우를 살펴본 다음 주변 지점 중에 값이 0이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
# 2. 방문한 지점에서 다시 상하좌우를 살펴보면서 방문을 다시 진행하기

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면 -> 문제에서 0을 방문한 것, 1을 이미 방문한 걸로 취급한 것!
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1

        # 상하좌우의 위치도 모두 재귀적으로 호출
        # 이때 이동하는 좌표는 함수의 이동을 생각해야 함.. 그 먼 이동이냐 평행이동(ㅎㅎ ㅠ) dx, dy.. 그거 있잖아
        dfs(x - 1, y) # 상
        dfs(x, y - 1) # 좌
        dfs(x + 1, y) # 하
        dfs(x, y + 1) # 우
        return True

    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0

for i in range(n): # 세로줄
    for j in range(m): # 가로줄
        # 현재 위치에서 DFS 수행
        if dfs(i, j):
            result += 1

print(result)