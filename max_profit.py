#Find maximum profit you can achieve from one transaction
# Input stock prices
prices = list(map(int, input("Enter stock prices separated by spaces: ").split()))

min_price = prices[0]  # minimum price seen so far
max_profit = 0         # maximum profit

for price in prices:
    if price < min_price:
        min_price = price       # update minimum price
    profit = price - min_price   # profit if sold today
    if profit > max_profit:
        max_profit = profit     # update max profit

print("Maximum profit is:", max_profit)