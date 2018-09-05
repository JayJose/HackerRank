# given an n
# and an arry
# find Q1 (median of left of median)
# find Q2 median
# find Q4 (median of right of median)

n = 9
arr = [3, 7, 8, 5, 12, 14, 21, 13, 18, ]

q1 = 6
q2 = 12
q3 = 16

# n = int(input())
# arr = sorted(list(map(int, input().split())))

median_i = n // 2

if median_i % 2 == 0:
    median = arr[median_i]
else:
    median = (arr[median_i] + arr[median_i + 1]) / 2


print('median:', median)
