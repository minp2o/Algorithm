'''
1. 연구소를 돌아다니면서 0인 셀 3개를 정해서 벽을 세움.
2. 벽 3개가 정해졌을 때 바이러스를 퍼뜨리고 0의 개수 구하기
'''
# import sys, copy
# sys.stdin= open('input.txt')


n,m=list(map(int,input().split()))
lab=[[0]*m for _ in range(n)]
spaces=[]
viruss=[]
for i in range(n):
    temp =list(map(int,input().split()))
    for j in range(m):
        lab[i][j] = temp[j]
        if lab[i][j]==0:
            spaces.append((i,j))
        if lab[i][j]==2:
            viruss.append((i,j))

max_safe = float('-inf')
visited=[[0]*n for _ in range(m)]

def dfs(l,s):         # 벽 세우기 dfs
    global max_safe
    if l==3:        # 벽 3개를 세웠을 때
        cnt=0
        lab_copy = copy.deepcopy(lab)
        visited = [[0] * m for _ in range(n)]
        bfs(lab_copy,visited)       # 바이러스 퍼뜨리기
        for i in range(n):
            for j in range(m):
                if lab_copy[i][j]==0:
                    cnt+=1
        if max(cnt,max_safe)==cnt:
            max_safe = cnt

    else:
        for i in range(s,len(spaces)):
            lab[spaces[i][0]][spaces[i][1]] = 1
            dfs(l+1,i+1)
            lab[spaces[i][0]][spaces[i][1]] = 0

dy=[-1,1,0,0]
dx=[0,0,-1,1]

def bfs(lab_copy,visited):      # 바이러스 퍼지기 bfs
    q=[]
    for virus in viruss:
        q.append(virus)
        visited[virus[0]][virus[1]]=1
    while q:
        cur = q.pop(0)
        for i in range(4):
            ny=cur[0]+dy[i]
            nx=cur[1]+dx[i]
            if 0<=ny<n and 0<=nx<m and lab_copy[ny][nx]!=1 and visited[ny][nx]==0:
                visited[ny][nx]=1
                lab_copy[ny][nx]=2
                q.append((ny,nx))



dfs(0,0)
print(max_safe)
