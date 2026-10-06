
# accounts = [[1,2,3],[3,2,1]]
# Output: 6

# largest = float("-inf")
# for i in accounts :
#     if sum(i) > largest :
#         largest = sum(i)

# print(largest)

# nums = [3,2,3,2]
# val = 2

# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:

#         k = 0

#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k += 1

#         return k


# solution = Solution()
# solution.removeElement(nums, val)




# nums1 = [1,2,3,0,0,0]
# m = 3
# k=3
# nums2 = [2,5,6]
# n = 3

# for j in nums2 :
#     nums1[k] = j

#     k+=1

# left = 0 
# right = len(nums1) -1

# while left < right : 

#     if nums1[left] > nums1[right] :
#         nums1[left] = nums1[right]


#     left += 1
#     right-=1

# print(nums1)




s = [1,2,3,2,6,5]

left = 0 

for right in range(1 , len(s)):

    if s[left] > s[right] :
        s[left] = s[right]

    left+=1
      


print(s)





