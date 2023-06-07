import sys
sys.stdin = open("성적평균.txt")
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(k):
    a, b, = map(int, input().split())
    result = round(sum(arr[a-1:b])/ (b-a+1) , 2)
    print(f'{result:.2f}')
