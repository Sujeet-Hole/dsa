# numbers = [4, 7, 2, 7, 9, 7, 3]

# count_of_7 = 0 


# for num in numbers :
#     if num == 7 :
#         count_of_7+=1

# print(count_of_7)


# numbers = [4, 7, 2, 7, 9, 7, 3]

# even_count = 0

# for num in numbers :

#     if num % 2 != 0 and num > 5 :
#         print(num)
#         break


# numbers = [4, 2, 7, 2, 4, 9, 2, 7]

# freq = {}
# has_duplicate = False

# for num in numbers :

#     if num in freq :
#         freq[num] +=1

#     else :
#         freq[num]=1

# for num,count in freq.items() :

#     if count > 1 :
#         has_duplicate = True
        
# print(has_duplicate)


# numbers = [1, 2, 3, 4, 5]
# has_duplicate = False
# duplicate = []
# new_l = []
# for num in numbers :
#     if num not in new_l :
#         new_l.append(num)

#     else:
#         duplicate.append(num)
#         has_duplicate = True





numbers = [4, 2, 7, 2, 4, 9, 2, 7]

duplicate = set()
new_l = []

for num in numbers :
    if num not in new_l :
        new_l.append(num)

    else :
        duplicate.add(num)


print(new_l)






duplicate = []
new_l = []

for num in numbers :
    if num not in new_l :
        new_l.append(num)

    else :
        duplicate.append(num)


print(new_l)




numbers = [4, 2, 7, 2, 4, 9, 2, 7]
freq = {}
for num in numbers :

    if num in freq :
        freq[num] +=1

    else :
        freq[num]=1


for num,count in freq.items():
    if count > 1 :
        print(num)
        break




numbers = [4, 2, 7, 2, 4, 9, 2, 7]
seen = set()
new_l = []
for i in numbers : 
    if i not in new_l :
        new_l.append(i)
    if i in new_l :
        seen.add(i)
        break

print(seen)















