numbers = [1, 3, 4, 7, 8, 10]
target = 15

found = False

for i in range(len(numbers) - 2):

    left = i + 1
    right = len(numbers) - 1

    while left < right:

        total = numbers[i] + numbers[left] + numbers[right]

        if total == target:
            found = True
            break

        if total > target:
            right -= 1
        else:
            left += 1

    if found:
        break

print(found)


numbers = [1, 2, 3, 4, 5, 6]


left = 0 
right = len(numbers)-1


while left < right :

    if numbers[left] != numbers[right] :
        print(False)
        break
    left+=1
    right-=1

else :
    print(True)


