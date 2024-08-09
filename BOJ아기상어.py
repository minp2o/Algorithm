import sys, queue
sys.stdin=open('input.txt')

# 방향 정의 (상좌우하)
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 입력 처리
n = int(input())
ocean = [list(map(int, input().split())) for _ in range(n)]

# 초기 설정
sharkSize = 2
eat = 0
answer = 0

# 아기 상어의 초기 위치 찾기
for i in range(n):
    for j in range(n):
        if ocean[i][j] == 9:
            sharkX, sharkY = i, j
            ocean[i][j] = 0  # 아기 상어 초기 위치를 0으로 설정

def bfs(x, y):
    global answer, sharkSize, eat, ocean
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    q = queue.Queue()
    q.put((x, y, 0))  # (현재 x, 현재 y, 현재 거리)
    possible_targets = []
    while not q.empty():
        cx, cy, dist = q.get()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if ocean[nx][ny] <= sharkSize:  # 상어가 이동할 수 있는 칸
                    visited[nx][ny] = 1
                    q.put((nx, ny, dist + 1))
                    if 0 < ocean[nx][ny] < sharkSize:  # 먹을 수 있는 물고기
                        possible_targets.append((dist + 1, nx, ny))
    if possible_targets:
        possible_targets.sort()  # 거리, 행, 열 순으로 정렬
        d, nx, ny = possible_targets[0]
        ocean[nx][ny] = 0
        eat += 1
        if eat == sharkSize:
            sharkSize += 1
            eat = 0
        answer += d
        return nx, ny
    else:
        return -1, -1

while True:
    sharkX, sharkY = bfs(sharkX, sharkY)
    if sharkX == -1 and sharkY == -1:
        break

print(answer)
