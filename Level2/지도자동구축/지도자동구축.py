import sys; sys.stdin = open("지도자동구축.txt")

N = int(input())
arr = [4]
square = 1
for i in range(N):
    if i == 0:
        new = arr[i] + square * 4 + square * 1
        arr.append(new)

        square *= 4
    else:
        a = int(square**(1/2) * (square**(1/2)-1) * 2 )
        new = arr[i] + square * 4 + square * 1 - a
        arr.append(new)
        square *= 4
print(arr[-1])