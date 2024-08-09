import sys

sys.stdin = open('input.txt')


def calc1(input):
    stack = []
    output = ''

    for char in input:
        if char.isdigit():
            output += char
        elif char == '+':
            while stack and stack[-1] == '+':
                output += stack.pop()
            stack.append(char)

    while stack:
        output += stack.pop()

    return output


def cal2(input):
    stack = []
    for char in input:
        if char.isdigit():
            stack.append(int(char))
        elif char == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)

    return stack[0]


for mm in range(10):
    n = int(input())
    inputStr = input().strip()
    inputStr2 = calc1(inputStr)
    print(f'#{mm + 1} {cal2(inputStr2)}')



