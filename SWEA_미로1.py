def dfs(i,j):
    global ans
    for k in range(4):
        ny=i+dy[k]
        nx=j+dx[k]
        if 0<=ny<16 and 0<=nx<16 and miro[ny][nx]==0 and visited[i][j]==0:
            visited[i][j]=1
            dfs(ny,nx)
            visited[i][j]=0
        elif 0<=ny<16 and 0<=nx<16 and miro[ny][nx]==3:
            ans=1

for tc in range(1,11):
    n=int(input())
    miro=[list(map(int,input())) for _ in range(16)]
    ans=0

    dy=[-1,1,0,0]
    dx=[0,0,-1,1]
    visited=[[0]*16 for _ in range(16)]

    start_x=-1

    for i in range(16):
        if start_x!=-1:
            break
        for j in range(16):
            if miro[i][j]==2:
                start_x=i
                start_y=j
                break
    dfs(start_x,start_y)
    print(f'#{tc} {ans}')