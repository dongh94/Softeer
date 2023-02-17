# 5
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2 "Case #(테스트 케이스 번호): "
import sys; sys.stdin=open("A+B.txt")
tc = int(input())
for t in range(tc):
    A, B = map(int, input().split())
    print(f"Case #{t+1}: {A + B}")

