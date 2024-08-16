'''
1. 만약에 위쪽으로 이동시키려면
2. 블록을 모두 위로 옮김     # 근데 어떻게 한 열에 있는 블록을 빈 공간 없이 모두 위로 올릴까?
3. 위쪽부터 아래로 내려가면서 같은 숫자가 연속으로 있으면 두 숫자를 더하고
4. 합쳐져서 공간이 남으면 블록을 모두 위로 옮김
'''
import sys
sys.stdin=open('input.txt')
import copy

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]

def move(board,dir):        # dir: 0,1,2,3=상하좌우
    if dir==2:  # 좌로 밀기
        for i in range(n):      # board의 i번째 행
            cursor=0
            for j in range(1,n):
                if board[i][j]!=0:      # j번째 열의 값이 0이 아니면
                    temp=board[i][j]
                    board[i][j]=0
                    if board[i][cursor]==0:
                        board[i][cursor]=temp
                    elif board[i][cursor]==temp:
                        board[i][cursor]*=2
                        cursor+=1
                    else:
                        cursor+=1
                        board[i][cursor]=temp

    if dir==0:  # 위로 밀기
        for i in range(n):      # board의 i번째 열
            cursor=0
            for j in range(1,n):
                if board[j][i]!=0:
                    temp=board[j][i]
                    board[j][i]=0
                    if board[cursor][i]==0:
                        board[cursor][i]=temp
                    elif board[cursor][i]==temp:
                        board[cursor][i]*=2
                        cursor+=1
                    else:
                        cursor+=1
                        board[cursor][i]=temp

    if dir==1:  # 밑으로 밀기
        for i in range(n):      # board의 i번째 열
            cursor=n-1
            for j in range(n-2,-1,-1):
                if board[j][i]!=0:
                    temp=board[j][i]
                    board[j][i]=0
                    if board[cursor][i]==0:
                        board[cursor][i]=temp
                    elif board[cursor][i]==temp:
                        board[cursor][i]*=2
                        cursor-=1
                    else:
                        cursor-=1
                        board[cursor][i]=temp

    if dir==3:  # 우로 밀기
        for i in range(n):      # board의 i번째 행
            cursor=n-1
            for j in range(n-2,-1,-1):
                if board[i][j]!=0:      # j번째 열의 값이 0이 아니면
                    temp=board[i][j]
                    board[i][j]=0
                    if board[i][cursor]==0:
                        board[i][cursor]=temp
                    elif board[i][cursor]==temp:
                        board[i][cursor]*=2
                        cursor-=1
                    else:
                        cursor-=1
                        board[i][cursor]=temp

    return board

maxNum=float('-inf')

def dfs(l,board):
    if l==5:
        global maxNum
        for i in range(n):
            for j in range(n):
                maxNum=max(maxNum,board[i][j])
    else:
        for i in range(4):
            board_copy=copy.deepcopy(board)
            dfs(l+1,move(board_copy,i))

dfs(0,board)
print(maxNum)





