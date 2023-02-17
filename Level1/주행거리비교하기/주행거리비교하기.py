import sys; sys.stdin = open("주행거리비교하기.txt")

A, B = map(int, input().split())

print("A") if A > B else print("same") if A == B  else print("B")