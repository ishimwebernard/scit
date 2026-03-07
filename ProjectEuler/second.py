sum = 0
real_sum = 0
for i in range(1, 101):
    sum += i **2
    real_sum += i
print("The sum of squares is", sum)
print(real_sum**2-sum)