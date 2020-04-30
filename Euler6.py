# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
sum_squares = 0
squares_sum = 0
sum = 0
for i in range(1,101,1):
    sum_squares += i**2
    print(sum_squares)
for i in range(1,101,1):
    sum += i
    print("Число i:{}".format(i))
    print(sum)
    if i == 100:
        squares_sum = sum**2

print("Сумма квадратов : {}".format(sum_squares))
print("Квадрат суммы: {}".format(squares_sum))
X = squares_sum-sum_squares
print("Разница квадратов: {}".format(squares_sum-sum_squares))
print(X)
