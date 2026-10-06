# number = [3, 8, 2, 10, 5, 7]
# smallest = number[0]

# for i in range(len(number)-1):
#     if number[i]< smallest :
#         smallest = number[i]
# print(smallest)



number = [3, 8, 2, 10, 5, 7]
largest = number[0]
second_largest = 0
for i in range(len(number)-1):
    if number[i]> largest :
        second_largest = largest
        largest = number[i]
print(second_largest)




