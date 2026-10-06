numbers = [2, 1, 5, 2, 3, 2]
S = 7
left = 0 
current_sum = 0
size = float("-inf")
for right in range(len(numbers)):

    current_sum+=numbers[right]

    while current_sum > S : 
        current_sum -= numbers[left]
        left+=1

    current_window =right - left + 1

    if current_window > size:
        size = current_window
print(size)

# "Mujhe array mein sabse lambi continuous window find karni hai jisme maximum 2 unique numbers ho."

numbers = [1, 2, 1, 2, 3]
unique = [1,2]

for num in numbers : 
    if num not in unique :
        numbers.remove(num)


print(numbers)

numbers = [1, 2, 1, 2, 3]
freq = {}
left = 0

for right in numbers : 
    if right not in freq :
        freq[right] = 0
    else :

        freq[right] += 1


numbers =  [1, 2, 1, 2, 3]
freq = {}
largest = float("-inf")
left = 0 
for right in range(len(numbers)):
    num = numbers[right]
    if num not in freq:
        freq[num] = 0
    freq[num] += 1
while len(freq) > 2 :
    left_num = numbers[left]
    freq[left_num] -= 1 

    if freq[left_num] == 0 :
        del freq[left_num]
    left+=1

current_window = right - left + 1
if current_window > largest:
        largest = current_window
print(largest)


# Find the length of the longest contiguous subarray that contains NO duplicate numbers

numbers = [1, 2, 1, 3, 4, 2, 3]
freq = {}
largest = float("-inf")
left = 0
for right in range(len(numbers)):
    num = numbers[right]
    if num not in freq:
        freq[num] = 0
    freq[num] += 1
        
    while freq[num] > 1 :

        left_num = numbers[left]
        freq[left_num] -= 1

        if freq[left_num] == 0 :
            del freq[left_num]
    
        left+=1

    current_window = right - left + 1

    if current_window > largest:
            largest = current_window
       
print(largest)





