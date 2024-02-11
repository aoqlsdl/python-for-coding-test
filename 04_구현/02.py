# example 2

n = int(input())
count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            # if (str(i)=='3' or str(j)=='3' or str(k)=='3'): # 내 답변(틀림)
            if '3' in str(i) + str(j) + str(k): # 3시 35분 40초일 때 33540으로 만들어서 이 안에 3이 있는지 확인
                count += 1

print(count)