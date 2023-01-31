import sys; sys.stdin=open("바이러스.txt")
#바이러스의 수 K, 증가율 P, 총 시간 N(초)
K, P, N = map(int, sys.stdin.readline().split())
for n in range(N): K *= P; K%=1000000007
print(K)