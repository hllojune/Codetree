arr = list(map(int, input().split()))
odd_arr = arr[0::2]
even_arr = arr[1::2]

odd_sum = 0
even_sum = 0

for i in range(5):
    odd_sum += odd_arr[i]
    even_sum += even_arr[i]
    
result = max(odd_sum, even_sum) - min(odd_sum, even_sum)

print(result)