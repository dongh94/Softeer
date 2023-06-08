import sys
sys.stdin = open("스마트물류.txt")
input = sys.stdin.readline

N, K, = map(int, input().split())
STR = list(input())
answer = 0
for i in range(len(STR)):
    if STR[i] == 'P':
        for j in range(i-K, i+K+1):
            if j >= 0 and j < len(STR) and STR[j] == 'H':
                STR[j] = 'O'
                answer += 1
                break
print(answer)