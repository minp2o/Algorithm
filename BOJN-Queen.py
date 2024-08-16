'''
1. 첫째 행에 임의로 퀸 하나를 배치시킴.
2. 다음 행에 들어갈 수 있는 퀸 위치를 가지치기함.
'''
import pprint as pp
import sys
sys.stdin = open('input.txt')

dy=[-1,1,0,0,1,1,-1,-1]
dx=[0,0,-1,1,1,-1,1,-1]

def zero_to_one(cur,chess_board):       # 어떤 위치에 퀸을 놓았을 때 바뀌는 체스판
    chess_board[cur[0]][cur[1]]=1
    for i in range(8):
        increase=1
        ny=cur[0]+increase*dy[i]
        nx=cur[1]+increase*dx[i]
        while 0<=ny<n and 0<=nx<n:
            chess_board[ny][nx]=1
            ny = cur[0] + increase * dy[i]
            nx = cur[1] + increase * dx[i]
            increase+=1


n=int(input())
queens=[0]*n        # 퀸이 배치 될 수 있는 좌표

for i in range(n):
    chess_board = [[0] * n for _ in range(n)]





