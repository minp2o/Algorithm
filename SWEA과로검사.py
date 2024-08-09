import sys, queue
sys.stdin=open('input.txt')

tc=int(input())
for mm in range(tc):
    answer=1
    stack=[]
    str=input()
    for i in str:
        if i=='(' or i=='{' or i=='[':
            stack.append(i)
        if stack:
            if i==')' and (stack[-1]=='{' or stack[-1]=='['):
                answer=0
                break
            if i=='}' and (stack[-1]=='(' or stack[-1]=='['):
                answer=0
                break
            if i==']' and (stack[-1]=='(' or stack[-1]=='{'):
                answer=0
                break

            if i==')' and stack[-1]=='(':
                stack.pop()
            elif i=='}' and stack[-1]=='{':
                stack.pop()
            elif i==']' and stack[-1]=='[':
                stack.pop()
        else:
            if i==')' or i=='}' or i==']':
                answer=0
                break

    if stack:
        answer=0
    print(f'#{mm+1} {answer}')