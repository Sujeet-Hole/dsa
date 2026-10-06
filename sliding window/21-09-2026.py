text = "eceba"

# freqHumein sabse lambi continuous 
# (contiguous) subarray find karni hai 
# jisme maximum 2
#  different/unique elements ho.


freq = {}
left = 0 
maximum = 0
for right in range (len(text)):
    number = text[right]

    if number not in freq :
        freq[number] = 1
    else : 
        freq[number] +=1
    while len(freq) > 2 :
        left_number = text[left]

        freq[left_number] -= 1


        if freq[left_number] == 0 :
            del freq[left_number]

        left+=1

    length = right - left + 1

    if length > maximum :
        maximum = length

print(maximum)


numbers = [1, 2, 1, 3, 4, 2, 3]

# freqHumein sabse lambi continuous 
# (contiguous) subarray find karni hai 
# jisme maximum 2
#  different/unique elements ho.


freq = {}
left = 0 
maximum = 0
for right in range (len(numbers)):
    number = numbers[right]

    if number not in freq :
        freq[number] = 1
    else : 
        freq[number] +=1
    while len(freq) > 2 :
        left_number = numbers[left]

        freq[left_number] -= 1


        if freq[left_number] == 0 :
            del freq[left_number]

        left+=1

    length = right - left + 1

    if length > maximum :
        maximum = length

print(maximum)






text = "abcabcbb"


freq = {}
left = 0 
maximum = 0
for right in range (len(text)):
    number = text[right]

    if number not in freq :
        freq[number] = 1
    else : 
        freq[number] +=1
    while freq[number] > 1 :
        left_number = text[left]

        freq[left_number] -= 1


        if freq[left_number] == 0 :
            del freq[left_number]

        left+=1

    length = right - left + 1

    if length > maximum :
        maximum = length

print(maximum)




numbers = [2, 1, 5, 1, 3, 2]
k = 3


left = 0
maximum_average = float("-inf")
window_sum = 0
for right in range(k) :

    window_sum+=numbers[right]

    a = window_sum / k

maximum_average = a

for right in range(k , len(numbers)):

    window_sum -= numbers[left]

    window_sum += numbers[right]

    av = window_sum / k

    left+=1

    if maximum_average < av :
        maximum_average = av

print(maximum_average)








numbers = [2, 3, 1, 2, 4, 3]
S = 7


left = 0 
window_sum = 0
minimum = float("inf")


for right in range(len(numbers)) :

    window_sum+=numbers[right]

    while window_sum >= S:

        length = right - left + 1

        if length < minimum:
            minimum = length

        window_sum -= numbers[left]
        left += 1

print(f"minimum {minimum}")




text = "aabacbebebe"

freq = {}
left = 0 
largest = 0

for right in range(len(text)):

    char= text[right]

    if char not in freq :
        freq[char] = 1

    else : 
        freq[char] +=1

    while (len(freq)) > 2 :

        left_text = text[left]

        freq[left_text] -= 1

        if freq[left_text] == 0 :
            del freq[left_text]

        left+=1

    length = right - left + 1

    if length > largest :
            largest = length 

print(largest)

        