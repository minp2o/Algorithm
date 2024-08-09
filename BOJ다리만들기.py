'''
모든 섬을 연결
다리의 길이>=2
'''
import sys,pprint
sys.stdin=open('input.txt')

n,m=list(map(int,input().split()))
map=[list(map(int,input().split())) for _ in range(n)]
dy=[1,-1,0,0]
dx=[0,0,1,-1]

# 1. 각 섬마다 번호부여하기
def bfs(i,j,num):
    global visited
    map[i][j]=num
    q=[]
    q.append((i,j))
    while q:
        cur = q.pop(0)
        for k in range(4):
            ny=cur[0]+dy[k]
            nx=cur[1]+dx[k]
            if 0<=ny<n and 0<=nx<m and map[ny][nx]==1 and visited[ny][nx]==0:
                visited[ny][nx]=1
                map[ny][nx] = num
                q.append((ny,nx))


# 맵의 모든 점을 돌면서 1이면 섬 마킹
visited = [[0] * m for _ in range(n)]
marking_number=1
for i in range(n):
    for j in range(m):
        if map[i][j]==1 and visited[i][j]==0:
            bfs(i,j,marking_number)
            marking_number += 1


# 2. 각 섬의 점마다 이을 수 있는 간선을 탐색해서 edges 세트에 넣기
edges = set()

# 각 섬의 점에서 그 수보다 큰 섬까지의 다리 만들기
def makingEdge(i,j,island_number):
    global edges

    for k in range(4):
        cnt = 1
        ny=i+dy[k]*cnt
        nx=j+dx[k]*cnt
        while 0<=ny<n and 0<=nx<m and map[ny][nx]==0:
            if 0<=i+dy[k]*(cnt+1)<n and 0<=j+dx[k]*(cnt+1)<m and map[i+dy[k]*(cnt+1)][j+dx[k]*(cnt+1)]>island_number and cnt>=2:
                edges.add((cnt,island_number,map[i+dy[k]*(cnt+1)][j+dx[k]*(cnt+1)]))
                break
            else:
                cnt+=1
                ny = i + dy[k] * cnt
                nx = j + dx[k] * cnt

# 3. 맵의 모든 점을 돌면서 섬 각 점에서 가능한 다리 간선 넣기 (가중치,섬 번호,섬 번호)
for i in range(n):
    for j in range(m):
        if map[i][j]!=0:
            makingEdge(i,j,map[i][j])

# 4. 간선들을 가중치 기준으로 오름차순 정렬 (그리디)
edgesList = list(edges)
edgesList.sort()


# 섬의 수
islandsCnt = marking_number-1

# 총 다리 길이
totalLength=0

# 간선 수
cnt=0

# 5. union & find를 통해 간선의 수 구하기 (간선의 수는 섬의 수 -1임)
def find(a):
    global unf
    if a==unf[a]:
        return a
    else:
        unf[a]=find(unf[a])
        return unf[a]
def union(a,b):
    global unf
    fa = find(a)
    fb = find(b)
    if fa>fb:
        unf[fb]=unf[fa]
    else:
        unf[fa]=unf[fb]

unf=[i for i in range(islandsCnt+1)]

for edge in edgesList:
    if find(edge[1])!=find(edge[2]):
        totalLength+=edge[0]
        union(edge[1],edge[2])
        cnt+=1
if cnt == islandsCnt-1:
    print(totalLength)
else:
    print(-1)











