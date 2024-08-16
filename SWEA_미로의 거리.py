import sys
sys.stdin=open('input.txt')

def bfs(i,j):
    cnt=0
    q=[]
    q.append((i,j,cnt))
    visited[i][j]=1
    while q:
        cur = q.pop(0)
        for k in range(4):
            ny=cur[0]+dy[k]
            nx=cur[1]+dx[k]
            if 0<=ny<n and 0<=nx<n and visited[ny][nx]==0 and miro[ny][nx]==0:
                visited[ny][nx]=1
                q.append((ny,nx,cur[2]+1))
            if 0 <= ny < n and 0 <= nx < n and miro[ny][nx]==3:
                return cur[2]




T=int(input())
for tc in range(1,T+1):
    n=int(input())
    miro=[[0]*n for _ in range(n)]
    for i in range(n):
        temp=list(map(int,input()))
        miro[i]=temp
        for j in range(n):
            if temp[j]==2:
                start_y=i
                start_x=j
                break
    visited=[[0]*n for _ in range(n)]
    dy=[-1,1,0,0]
    dx=[0,0,1,-1]

    ans=bfs(start_y,start_x)
    if ans!=None:
        print(f'#{tc} {ans}')
    else: print(f'#{tc} 0')
