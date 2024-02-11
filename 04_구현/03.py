# unsolved
# 왕실의 나이트

# row = ['1','2','3','4','5','6','7','8']
# column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#
# location = str(input())
# x = location[0]
# y = location[1]
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# a, b / g, h는 오른쪽/왼쪽으로 두 번 이동 불가하므로 경우의 수 -2 ---> column[0], column[1], column[n], column[n-1]
# 1, 2 / 7, 8은 위쪽/아래쪽으로 두 번 이동 불가하므로 경우의 수 -2 ---> row - 2 <= 0 일 때
# 위 경우를 제외한 모든 경우의 수는 8번

# movement = 8
#
# if '1' or '2' or '7' or '8' in x:
#     movement -= 2
# if 'a' or 'b' or 'g' or 'h' in y:
#     movement -= 2


# example
# 해설: 나이트가 이동할 수 있는 경로를 하나씩 확인하되, 8*8 평면을 벗어나는지 체크하기
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의(좌우, 상하)
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대해 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
