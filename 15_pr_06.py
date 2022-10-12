# n! = 1 x 2 x 3 x........x n
# 5! = 1 x 2 x 3 x 4 x 5

from math import factorial


num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial*i
print(f"The factorial oof {num} is {factorial}")
