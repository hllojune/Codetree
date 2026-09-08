arr = list(map(int, input().split()))

sum_even = 0
avg_val = arr[2::3]
for i in range(len(arr)):
    if(i%2 == 0):
        sum_even += arr[i-1]
avg = round(sum(avg_val) / len(avg_val), 1)
print(sum_even, avg)