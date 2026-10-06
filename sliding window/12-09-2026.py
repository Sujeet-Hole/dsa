numbers = [1, 1, 2, 2, 3, 4, 4]
# left = 1
# for right in range(len(numbers)):

#     if numbers[left - 1] == numbers[right] : 
#         numbers.pop(right)


#     left+=1

# print(numbers)

numbers = [1, 1, 2, 2, 3, 4, 4]

left = 0 

for right in range(1,len(numbers)):

    if numbers[right] != numbers[left] : 
        left+=1
        numbers[left] = numbers[right]
        
print(numbers[:left+1])