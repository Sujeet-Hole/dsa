# Delayed Recall — Sliding Window



numbers = [4, 2, 7, 1, 8, 3]
k = 3
maximum = float("-inf")
left = 0

window_sum = 0

for right in range(k):

    window_sum += numbers[right]

maximum = window_sum

for right in range(k , len(numbers)):

    window_sum -= numbers[left]

    window_sum += numbers[right]


    left += 1 

    if maximum < window_sum :
        maximum = window_sum 

print(maximum)



numbers = [1, 2, 1, 3, 2, 3, 4]
left = 0 
largest = float("-inf")
freq = {}

for right in range(len(numbers)):

    number = numbers[right]

    if number not in freq : 
        freq[number] = 1 

    else : 
        freq[number]+=1

    while freq[number] > 1 :

        left_number = numbers[left]

        freq[left_number] -= 1

        if freq[left_number] == 0 :
            del freq[left_number]
        left+=1

    length = right - left + 1 

    if length > largest : 
        largest = length 

print(largest)




numbers = [2, 7, 11, 15]
target = 9

freq = {}

for number in numbers : 

    remaining = target - number

    if remaining in freq :
        print(number , remaining)
        break
        
    freq[number] = 1




    

numbers = [4, 7, 2, 7, 9, 4]

# brute forece approch  
seen = {}

for number in numbers : 
    if number not in seen :
        seen[number] = 1 
    else : 
        seen[number] += 1

for number in seen :
    if seen[number] > 1 :
        print(number)
        break


numbers = [4, 7, 2, 7, 9, 4]


seen= { }

for number in numbers :

    if number in seen : 
        print(number)
        break

    seen[number] = 1

numbers = [5, 3, 7, 3, 9, 5, 2]
seen = {}

for index ,number in enumerate (numbers) :
    seen[number] = index

# my mistake 
    if number == 3 :
        print(f"is index {index}")
        break


numbers = [5, 3, 7, 3, 9, 5, 2]

seen = {}

for index, number in enumerate(numbers):

    if number not in seen:
        seen[number] = index

print(seen[3])




numbers = [8, 3, 5, 8, 2, 3, 9]

seen = {}

for index , number in enumerate(numbers):

    if number not in seen : 
       seen[number] = index



numbers = [8, 3, 5, 8, 2, 3, 9]

seen = {}

for index , number in enumerate(numbers):

       seen[number] = index
print(seen)


students = [
    ("Amit", "IT"),
    ("Rahul", "CS"),
    ("Sneha", "IT"),
    ("Priya", "CS"),
    ("Rohan", "ENTC")
]

group = {}
for name , department in  students :

    if department not in group :
        group[department] = []

    group[department].append(name)

print(group)

products = [
    ("Laptop", 50000),
    ("Mouse", 1000),
    ("Keyboard", 2000)
]

prices = {}

for name, price in products:
    prices[name] = price

print(prices)


# prefix_sum  = Find all continuous subarrays whose sum is exactly 2.

numbers = [3, 4, -2, 5, -5]
target = 2

current_sum = 0
seen = {0: -1}

for index, number in enumerate(numbers):

    current_sum += number

    required = current_sum - target

    if required in seen:
        print(seen[required] + 1, index)

    if current_sum not in seen:
        seen[current_sum] = index
        