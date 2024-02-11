# unsolved

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
first = arr[0]
second = arr[1]

# 2 4 5 4 6
# 6 6 6 5 / 6 6 6 5

# 가장 큰 수가 더해지는 횟수 계산
# 더해지는 횟수 m에서 수열이 반복되는 횟수를 나누어준다. (가장 큰 수 k개 + 그 다음으로 큰 수 1개 더하면 최댓값)
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수
result += (m - count) * second # 두 번째로 큰 수(더해지는 전체 횟수 m에서 가장 큰 수를 더하는 횟수인 count를 빼주면 두 번째로 큰 수를 더하는 횟수

print(result)

