import sys
sys.stdin = open("징검다리.txt")
sys.setrecursionlimit(1000)
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
length = len(arr)

rocks = [1]*length
for i in range(length-1):
    for j in range(i+1, length):
        if arr[i] < arr[j]:
            rocks[j] = max(rocks[j], rocks[i] + 1)
print(max(rocks))

