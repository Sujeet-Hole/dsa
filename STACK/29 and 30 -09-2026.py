# nums = [1,2,3,4]

# running_sum = 0
# output = []
# for right in range(len(nums)):

#     running_sum += nums[right]

#     output.append(running_sum)

# print(output)



# candies = [2, 3, 5, 1, 3]
# extraCandies = 3


# output = []


# for candi in candies :

#     if candi+3 >= max(candies):
#         output.append("true")

#     else:
#         output.append("false")


# print(output)



n = 5
count = 0
for a in range(1, n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):

            if a*a + b*b == c*c :
                count+=1
print(count)

nums = [1,2,1]
# ans = []
# e = len(nums)+1

# for i in range (len(nums)) :

#     nums[e] = nums[i]

#     nums.append(nums[e])

#     print(nums)


ans = []

for i in range(len(nums)):
    ans.append(nums[i])

for i in range(len(nums)):
    ans.append(nums[i])

print(ans)

n = 15
outout = []
for i in range(1 , n+1):

    if i % 3 == 0 and i % 5 == 0 :
        outout.append("FizzBuzz")

    elif i % 3 == 0 :
        outout.append("Fizz")

    elif i % 5 == 0 :
        outout.append("Buzz")

    else : 
        outout.append(i)

print(outout)


