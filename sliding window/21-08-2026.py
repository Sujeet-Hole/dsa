numbers = [4, 7, 2, 9, 1, 6]
# largest = float("-inf")

# for i in numbers :
#     if i > largest :
#         largest = i


        
left = 0
right = len(numbers)-1
largest = 0

while left > right :

    n = numbers[left] > numbers[right]

    if largest < n :
        largest = n

    left+=1
    right-=1

print(largest) 



