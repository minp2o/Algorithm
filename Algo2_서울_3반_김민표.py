

def makeUp(idx):        # 오르막이 시작하는 인덱스부터 오르막길 배열 만들기
    global up,n,load,temp
    up.append(load[idx])
    for i in range(idx,n):
        if i+1<n and load[i+1]>=load[i]:
            up.append(load[i+1])
        else:
            temp=i+1
            return



tc = int(input())
for t in range(tc):
    temp=0
    n=int(input())
    ups = []        # 오르막길 배열
    load=list(map(int,input().split()))
    for i in range(n):
        up=[]       # 오르막길
        if i ==temp:
            makeUp(i)
            ups.append(up)
    for i in range(len(ups)):   # 오르막길 배열에서 길이가 1인 오르막길(그냥 평지) 없애기
        if len(ups[i])==1:
            ups.remove(ups[i])


    inclineLength = {}          # 오르막길 배열의 각 오르막길에 대한 경사도와 길이
    for i in range(len(ups)):
        miin=float('inf')
        maax=float('-inf')
        for j in range(len(ups[i])):

            if ups[i][j]<=miin: miin=ups[i][j]
            if ups[i][j]>=maax: maax=ups[i][j]
        incline = (maax-miin)/len(ups[i])
        inclineLength[i]=[incline,len(ups[i])]

    # 최소 경사도 구하기
    miinIncline =float('inf')
    for i in range(len(inclineLength)):
        if inclineLength[i][0]<=miinIncline: miinIncline=inclineLength[i][0]
    # 최소 경사도에 해당하는 최대 길이 구하기
    maaxLength = float('-inf')
    for i in range(len(inclineLength)):
        if inclineLength[i][0]==miinIncline and inclineLength[i][1]>=maaxLength:
            maaxLength=inclineLength[i][1]
    # 오르막이 없는 경우 0을 출력
    if len(ups)==0:
        print(f'#{t+1} 0')
    else: print(f'#{t+1} {maaxLength}')











