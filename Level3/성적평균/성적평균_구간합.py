import sys
sys.stdin = open("성적평균.txt")
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

sum = [0] * (n + 1)
sum[1] = arr[0]
for i in range(1, n+1):
    sum[i] = sum[i-1] + arr[i-1]

for j in range(k):
    a, b = map(int, input().split())
    answer = sum[b] - sum[a-1]
    print(f'{round(answer/(b-a+1)*100)/100:.2f}')

