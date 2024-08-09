import sys
sys.stdin = open('input.txt')

tc=int(input())
for mm in range(tc):
    text,pattern = list(input().split())
    n = len(text)
    m = len(pattern)
    cnt=0

    for i in range(n-m+1):
        zz = True
        for j in range(i,i+m):
            if text[j]!=pattern[j-i]:
                zz=False
                break
        if zz==True:
            cnt+=1
    answer=n-cnt*m+cnt
    print(f'#{mm+1} {answer}')
