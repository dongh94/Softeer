import sys; sys.stdin = open("근무시간.txt")

# 10:00 19:00
# 09:00 15:00
# 10:00 11:00
# 11:00 22:00
# 09:00 15:00
answer = 0
for i in range(5):
    start, end = input().split()
    starthour = int(start[:2])
    endhour = int(end[:2])
    startminute = int(start[-2:])
    endminute = int(end[-2:])
    if startminute > endminute:
        endhour -= 1
        endminute += 60
    answer += endminute - startminute
    answer += (endhour - starthour) * 60

print(answer)