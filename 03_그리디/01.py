# example

coins = [500, 100, 50, 10]
price = int(input())
num_of_coins = 0

for coin in coins:
    if price == 0:
        break
    num_of_coins += price // coin
    price %= coin

print(num_of_coins)