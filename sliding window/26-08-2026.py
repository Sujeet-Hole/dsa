numbers = [4, 7, 2, 9, 1, 6]

for i in range(len(numbers)):
    largest = True

    for j in range(len(numbers)):
        if numbers[j] > numbers[i]:
            largest = False
            break

    if largest:
        print(numbers[i])
        break




number = [1,2,3,5,6,8,9]
left = 0
largest = 0

for i in range(len(numbers)):
    largest = True

    for j in range(len(numbers)):
        if numbers[j] > numbers[i]:
            largest = False
            break

    if largest:
        print(numbers[i])
        break












