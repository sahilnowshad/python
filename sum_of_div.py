#Sum of numbers divisible by 3 from 1 to 100
sum = 0

for i in range(1, 101):
    if i % 3 == 0:
        sum = sum + i

print("Sum of numbers divisible by 3 from 1 to 100 is:", sum)