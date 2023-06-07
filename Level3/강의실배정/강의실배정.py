import sys
from heapq import heapify, heappop, heappush
sys.stdin = open("강의실배정.txt")
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    s, e = map(int, input().split())
    heappush(heap, (e, s))
# 끝나는 시간이 이를 수록 공간이 많이 나와 더욱 많은 강의를 배치할 수 있다.
# 정렬하는데 시간이 많이 걸릴 수 있다..

answer = 0
last_num = 0
while heap:
    e, s = heappop(heap)
    if last_num <= s:
        last_num = e
        answer += 1
print(answer)




