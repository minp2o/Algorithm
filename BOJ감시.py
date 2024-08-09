'''
CCTV는 벽(6)을 통과할 수 없다.
CCTV는 CCTV(1~5)를 통과할 수 있다.
'''

'''
모든 CCTV를 배열에 넣는다.
각 CCTV의 방향 조합을 DFS로 정한다.
'''

import sys
sys.stdin = open('input.txt')

CCTVS = []
n,m=list(map(int,input().split()))
samushil = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if 1<=samushil[i][j]<=5:
            CCTVS.append(samushil[i][j])

