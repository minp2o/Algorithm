import sys
sys.stdin = open('input.txt')


for mm in range(10):
    n=int(input())
    table=[input() for _ in range(100)]
    maxLen=1
    for i in range(100):        #현재 행or열 인덱스
        if maxLen==100:
            break
        for j in range(100,1,-1):       #글자 수가 100개인 단어부터 2개인 단어까지 회문이 있는지 확인
            if j>maxLen:        #현재까지 찾은 회문의 최대 글자수 이하인 단어는 그냥 넘기기
                for k in range(100-j+1):    #현재 행or열에서 해당 글자 수에 해당하는 회문 검사
                    temp1=table[i][k:k+j]
                    if temp1==temp1[::-1]:
                        maxLen=j
                        break
                    temp2=''.join([table[k+t][i] for t in range(j)])
                    if temp2==temp2[::-1]:
                        maxLen=j
                        break

    print(maxLen)
