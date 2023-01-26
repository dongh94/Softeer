import sys; sys.stdin=open("8단변속기.txt")

arr = list(map(int,input().split()))
N = len(arr)
init_v = arr[0]
for i in range(1, N-1):
    if init_v < arr[i] and arr[i] < arr[i+1]:
        init_v = arr[i]
        answer = 'ascending'

    elif init_v > arr[i] and arr[i] > arr[i+1]:
        init_v = arr[i]
        answer = 'descending'

    else:
        answer = 'mixed'
        break
print(answer)