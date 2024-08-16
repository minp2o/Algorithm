import sys
sys.stdin=open('input.txt')

from collections import deque
'''
 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소한다.
1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
'''

n,k = list(map(int,input().split()))    #n:벨트길이,k:내구도 0인 칸의 개수가 k개 이상이면 과정 종료
arr = list(map(int,input().split()))    #arr:벨트의 내구도
belt = deque([[i,False] for i in range(2*n)])

cnt=1
while True:
    belt.rotate(1)  # 1단계
    if belt[n-1][1]==True:
        belt[n-1][1]=False
    for i in range(n-1,-1,-1):   # 2단계
        if belt[i][1]==True:
            if belt[i+1][1]==False and arr[belt[i+1][0]]>=1:
                belt[i][1]=False
                belt[i+1][1]=True
                arr[belt[i+1][0]]-=1
                if belt[n-1][1] == True:
                    belt[n-1][1] = False
    if arr[belt[0][0]]>0:   # 3단계
        belt[0][1]=True
        arr[belt[0][0]]-=1
    if arr.count(0)>=k:   # 4단계
        break
    cnt+=1
print(cnt)

