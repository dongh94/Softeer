import sys; sys.stdin = open('회의실예약.txt')
#회의실 수 / 회의 예약 수
N, M = map(int,input().split())

# 딕셔너리에 리스트를 담으면 추가인덱싱 가능하다는 점.
room_dict = {}
for _ in range(N):
    room_dict[input()] = [0] * 18

# 0, 1을 사용 !!
for m in range(M):
    roomname, start, end = input().split()
    start = int(start)
    end = int(end)
    for t in range(start, end):
        room_dict[roomname][t] = 1
# print(room_dict)

#정렬 => sorted 함수는 List로 return
room = sorted(room_dict.items())
# print(room)

#check이라는 하나의 조건문을 추가해 visited 했는지 확인가능하다는 것.
for n in range(N):
    check = 0
    start_t = end_t = 0
    temp = []
    for t in range(9, 18):
        if check == 0 and room[n][1][t] == 0:
            start_t = t
            check = 1

        elif check == 1 and room[n][1][t] == 1:
            end_t = t
            check = 0
            temp.append([start_t, end_t])
    # 끝 값 고려
    if check == 1:
        temp.append([start_t, 18])
    # print(temp)
    print(f"Room {room[n][0]}:")
    answer_length = len(temp)
    if not answer_length : print("Not available");
    else:
        print(f"{answer_length} available:")
        for i in range(answer_length):
            print(f"{temp[i][0]:02d}-{temp[i][1]}")
    if n != N-1:
        print("-----")

