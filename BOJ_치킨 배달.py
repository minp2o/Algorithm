'''
1. 치킨집 M개 고르는 조합 DFS
2. 각각의 집에서 치킨 거리 구하기 BFS ----> BFS쓰면 시간초과남. 각 집에 대해 모든 치킨 집까지 거리의 최소값을 반복문으로 알아내야함.
'''

import copy

# def bfs(i,j,city_copy):       # 집에서 치킨거리 반환
#     q=[]
#     q.append((i,j))
#     while q:
#         cur=q.pop(0)
#         for k in range(4):
#             ny=cur[0]+dy[k]
#             nx=cur[1]+dx[k]
#             if 0<=ny<n and 0<=nx<n:
#                 if city_copy[ny][nx]==2:
#                     return abs(i-ny)+abs(j-nx)
#                 else:
#                     q.append((ny,nx))

# def getDist(i,j):       # 특정 집에서 치킨 거리 구하기
#
#



def dfs(l,s):
    global minDist
    if l==m:        # m개의 치킨 집 선택
        city_copy=copy.deepcopy(city)
        for chicken in selected_chickens:
            city_copy[chicken[0]][chicken[1]]=2          # 고른 치킨집들 city에 넣기
        temp=0
        for i in range(n):
            for j in range(n):
                if city_copy[i][j]==1:
                    temp+=bfs(i,j,city_copy)
        if min(temp,minDist)==temp:
            minDist=temp
    else:
        for i in range(s,len(chickens)):
            selected_chickens[l]=chickens[i]
            dfs(l+1,i+1)

dy=[-1,1,0,0]
dx=[0,0,-1,1]

n,m=list(map(int,input().split()))
city=[[0] for _ in range(n)]
chickens=[]
selected_chickens=[0]*m
houses=[]
for i in range(n):
    tempInput=list(map(int,input().split()))
    city[i]=tempInput
    for j in range(n):
        if tempInput[j]==2:
            chickens.append((i,j))
            city[i][j]=0    # city에서 치킨집 다없애기
        if tempInput[j]==1:
            houses.append((i,j))


minDist=float('inf')
dfs(0,0)

print(minDist)



