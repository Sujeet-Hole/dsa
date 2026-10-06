# Find all continuous subarrays 
# whose sum is exactly 2.

numbers = [3, 4, -2, 5, -5]
target = 2
seen = {}
prefix_sum = 0

for index , number in enumerate(numbers):

    prefix_sum += number

    required = prefix_sum - target 

    if required in seen :
        print(seen[required] +1 , index)

    seen[prefix_sum] = index

# output
# 1 2
# 1 4
# index 1 se index 2 ka sum 2 hai and 
# index 1 se index 4 tak ka sum 2 hai 

# Running sum → target minus karo → required 
# old prefix dhundo → mila 
# toh uske next index se subarray start.



numbers = [3, 4, -2, 5, -5]
target = 5

prefix_sum = 0 
seen = {0 :-1}

for index ,number in enumerate(numbers) : 

    prefix_sum += number

    required = prefix_sum - target 

    if required in seen : 
        print(seen[required]+1 , index)

    seen[prefix_sum] = index

print(seen)



numbers = [1, 2, -2, 3]
target = 3

prefix_sum = 0 
seen = {0 :-1}

for index ,number in enumerate(numbers) : 

    prefix_sum += number

    required = prefix_sum - target 

    if required in seen : 
        print(seen[required]+1 , index)

    seen[prefix_sum] = index











    