# solved
# 1이 될 때까지 수행하는 과정
# 1. n - 1 2. n / k (단, n % k == 0일 때만) 중 하나만 선택

n, k = map(int, input().split())

count = 0

print("==== 첫번째 방법 ====")
while True:
    if n == 1: break

    if n % k == 0:
        n /= k
    else:
        n -= 1

    count += 1

print(count)

# 나눗셈을 최소화하고, 한 번에 많은 수를 줄일 수 있어 더 효율적인 방법.
# 단순히 뭔가 이뤄지는 순서를 생각하기 보다는 규칙.. 혹은 가장 빠르게 연산할 수 있는 방법이 없을지 떠올려보기
print("==== 두번째 방법 ====")
n, k = map(int, input().split())
result = 0

while True:
    # (n == k로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    print("target", target)
    result += (n - target)
    print("result", result)
    n = target
    print("n", n)

    # n < k일 때 더이상 나눌 수 없으므로 반복문 탈출
    if n < k:
        break

    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)