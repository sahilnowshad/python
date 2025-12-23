#Return minimum coins needed for a certain fixed amount, if not possible return -1
coins = list(map(int, input("Enter coin values separated by spaces: ").split()))
amount = int(input("Enter amount: "))

def minCoins(coins, amount):
    if amount == 0:
        return 0  # 0 coins needed for amount 0
    res = float('inf')
    for coin in coins:
        if coin <= amount:
            sub_res = minCoins(coins, amount - coin)
            if sub_res != float('inf'):
                res = min(res, sub_res + 1)
    return res

result = minCoins(coins, amount)
if result == float('inf'):
    print(-1)
else:
    print("Minimum coins needed:", result)