import sys
from pprint import pprint

sys.setrecursionlimit(100000)
sys.stdin = open("이미지프로세싱.txt")
h, w = map(int, input().split())
image = [[0] * (w+1)]
for i in range(h):
    temp = list(map(int, input().split()))
    image.append([0] + temp)
# print(image)

q = int(input())

def color(x, y, c):
    old_c = image[x][y]
    image[x][y] = c

    stack = [(x, y)]
    while stack:
        pprint(image)
        x, y = stack.pop()
        if image[x-1][y] == old_c:
            image[x-1][y] = c
            stack.append((x-1, y))
        if image[x][y-1] == old_c:
            image[x][y-1] = c
            stack.append((x, y-1))
        if x < h and image[x+1][y] == old_c:
            image[x+1][y] = c
            stack.append((x+1, y))
        if y < w and image[x][y+1] == old_c:
            image[x][y+1] = c
            stack.append((x, y+1))

for i in range(q):
    x, y, c = map(int, input().split())
    if image[x][y] != c:
        color(x, y, c)

for i in range(1, h+1):
    for j in range(1, w+1):
        print(image[i][j], end=' ')
    print()