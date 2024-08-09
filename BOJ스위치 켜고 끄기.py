import sys
sys.stdin = open('input.txt')


n=int(input())  # 스위치 개수
switch = list(map(int,input().split())) # 스위치 상태
k=int(input())  # 학생 수
changeSwitch=[[0]*2 for _ in range(k)]
for i in range(k):  # 학생 수만큼 입력 받기
    changeSwitch[i][0],changeSwitch[i][1]=list(map(int,input().split()))

for sn in changeSwitch:  # k번 스위치 상태 변경하기
    if sn[0]==1:    # 남자면
        for i in range(n):
            if (i+1)%sn[1]==0:
                if switch[i]==1:
                    switch[i]=0
                else:switch[i]=1
    else:   # 여자면
        if switch[sn[1]-1]==1:
            switch[sn[1]-1]=0
        else:
            switch[sn[1]-1]=1
        cnt=1
        while sn[1]-1-cnt>=0 and sn[1]-1+cnt<n and switch[sn[1]-1-cnt]==switch[sn[1]-1+cnt]:
            if switch[sn[1]-1-cnt]==0:
                switch[sn[1]-1-cnt]=1
                switch[sn[1]-1+cnt]=1
            else:
                switch[sn[1] - 1 - cnt] = 0
                switch[sn[1] - 1 + cnt] = 0
            cnt+=1
print(*switch[0:20])
print(*switch[20:40])
print(*switch[40:60])
print(*switch[60:80])
print(*switch[80:100])
