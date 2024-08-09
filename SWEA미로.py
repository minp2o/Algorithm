from collections import deque 
sys.stdin = open('input.txt')


tc=int(input())
for mm in range(tc):
    n=int(input())
    miro=[list(map(int,list(input()))) for _ in range(n)]
    answer=0
    dy=[-1,0,1,0]
    dx=[0,-1,0,1]
    y_start=-1
    x_start=-1
    visited=[[0]*n for _ in range(n)]

    # 출발점 찾기
    for i in range(n):
        if y_start!=-1:
            break
        for j in range(n):
            if miro[i][j]==2:
                y_start,x_start=i,j
                break

    # def dfs(y,x):
    #     global answer, visited
    #     if answer==1:
    #         return
    #     for i in range(4):
    #         ny=y+dy[i]
    #         nx=x+dx[i]
    #         if 0<=ny<n and 0<=nx<n and visited[ny][nx]==0:
    #             if miro[ny][nx]==0:
    #                 visited[ny][nx] = 1
    #                 dfs(ny,nx)
    #                 visited[ny][nx]=0
    #             elif miro[ny][nx]==3:
    #                 answer=1
    #                 return

    def bfs():
        global answer,visited
        q = queue.Queue()
        q.put((y_start, x_start))
        while not q.empty():
            cur=q.get()
            for i in range(4):
                ny=cur[0]+dy[i]
                nx=cur[1]+dx[i]
                if 0<=ny<n and 0<=nx<n and visited[ny][nx]==0:
                    if miro[ny][nx]==3:
                        answer=1
                        return
                    elif miro[ny][nx]==0:
                        visited[ny][nx]=1
                        q.put((ny,nx))



    visited[y_start][x_start]=1
    #dfs(y_start,x_start)
    bfs()
    print(f'#{mm+1} {answer}')
