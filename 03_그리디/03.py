# solved

# 낮은 숫자 중에서 가장 높은 숫자 뽑기
# n: 행의 개수 m: 열의 개수
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

print("n, m: ")
n, m = map(int, input().split())

max_num = 0

for i in range(n):
    # 열마다 가장 작은 수 구해서 저장
    # 그 다음 열에서 가장 작은 수 구한 다음 수 비교
    # 가장 작은 수 < 현재 열에서 가장 작은 수이면 현재 열에서 가장 작은 수로 저장
    print("arr: ")
    arr = list(map(int, input().split()))
    arr.sort()

    if arr[0] > max_num:
        max_num = arr[0]

print(max_num)

# sol 1. min()함수 이용하기
for i in range(n):
    data = list(map(int, input().split))
    # 현재 줄에서 가장 작은 수
    min_value = min(data)
    result = max(max_num, min_value)

print(max_num)

# sol 2. 2중 반복문 구조
for i in range(n):
    data = list(map(int, input().split()))

    # 현재 줄에서 가장 작은 수
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)