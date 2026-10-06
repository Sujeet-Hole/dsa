numbers = [2, 1, 5, 1, 3, 2]
k = 3
largest = float("-inf")
window_sum = 0 

left = 0
for right in range(k):

    window_sum += numbers[right]

largest = window_sum

for right in range (k, len(numbers)):

    window_sum -= numbers[left]

    window_sum += numbers[right]

    left += 1

    if window_sum > largest:
        largest = window_sum

print(largest)




numbers = [2, 3, 1, 2, 4, 3]
S = 7

minimum = float("inf")
left = 0
window_sum = 0
for right in range(len(numbers)):

    window_sum += numbers[right]

    while window_sum >=S:
         length = right - left +1 

         if length < minimum :
            minimum = length

         window_sum -= numbers[left]

         left+=1

print(length)



