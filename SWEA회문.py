import sys
sys.stdin = open('input.txt')


tc = int(input())


for mm in range(tc):
    n, m = list(map(int, input().split()))
    answer=''
    table = [input() for _ in range(n)]
    for i in range(n):
        if answer!='':
            break
        for j in range(0,n-m+1):
            temp1=table[i][j:j+m]
            if temp1==temp1[::-1]:
                answer=temp1
                break
            temp2 = ''.join([table[j+k][i] for k in range(m)])
            if temp2 == temp2[::-1]:
                answer = temp2
                break

    print(f'#{mm+1} {answer}')


