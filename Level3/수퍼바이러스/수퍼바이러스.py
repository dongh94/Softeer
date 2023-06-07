import sys
sys.stdin = open("수퍼파이러스.txt")
input = sys.stdin.readline
sys.setrecursionlimit(10000)

K, P, N = map(int, input().split())
def f(i, n):
    if n == 1:
        return i % 1000000007

    if n % 2 == 0:
        a = f(i, n // 2) % 1000000007
        return a  * a % 1000000007

    if n % 2 == 1:
        a = f(i, n // 2) % 1000000007
        return a * a * i % 1000000007

mult = f(P, 10 * N)
print(K * mult % 1000000007)