import sys
sys.setrecursionlimit(100000)
sys.stdin = open("이미지프로세싱.txt")
from pprint import pprint
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
    pprint(image)
    if image[x-1][y] == old_c:
        color(x-1, y, c)
    if image[x][y-1] == old_c:
        color(x, y-1, c)
    if x < h and image[x+1][y] == old_c:
        color(x+1, y, c)
    if y < w and image[x][y+1] == old_c:
        color(x, y+1, c)
    return



for i in range(q):
    x, y, c = map(int, input().split())
    if image[x][y] != c:
        color(x, y, c)
for i in range(1, h+1):
    for j in range(1, w+1):
        print(image[i][j], end=' ')
    print()