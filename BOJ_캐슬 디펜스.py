import sys
from itertools import combinations
from collections import deque
import copy
sys.stdin=open('input.txt')


n,m,d = list(map(int,input().split()))
board=[list(map(int,input().split())) for _ in range(n)]
board.append([0]*m)

dy=[0,-1,0]      # 왼 위 오
dx=[-1,0,1]
def bfs(i,j,visited):
    q=deque()
    q.append((i,j,0))
    visited[i][j]=1
    while q:
        cur = q.popleft()
        for k in range(3):
            ny=cur[0]+dy[k]
            nx=cur[1]+dx[k]
            if 0<=ny<n+1 and 0<=nx<m and visited[ny][nx]==0:
                if cur[2]+1<=d:
                    visited[ny][nx]=1
                    if board_copy[ny][nx]==1:
                        catch.add((ny,nx))
                        return

                    q.append((ny,nx,cur[2]+1))



maxKill=float('-inf')

for i in combinations([j for j in range(m)],3):     # 궁수 배치 조합 구하기 i=(0,2,4)
    cnt=0
    board_copy=copy.deepcopy(board)
    while True:
        catch = set()

        for t in range(3):  # 3번의 궁수 공격
            visited=[[0]*m for _ in range(n+1)]
            bfs(n,i[t],visited)
        for kill in list(catch):
            board_copy[kill[0]][kill[1]] =0
            cnt+=1
        for ii in range(n-1,-1,-1):
            for jj in range(m):
                if board_copy[ii][jj]==1:
                    if ii+1==n:
                        board_copy[ii][jj]=0
                    else:
                        board_copy[ii][jj]=0
                        board_copy[ii+1][jj]=1
        if all(all(cell == 0 for cell in row) for row in board_copy[:n]):
            break


    maxKill=max(maxKill,cnt)
print(maxKill)