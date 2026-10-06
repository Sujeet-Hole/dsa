numbers = [1, 2, 3, 1, 2, 3, 4]

left = 0 
freq = {}
maximum = float("-inf") 

for right in range(len(numbers)):
    number = numbers[right]
    

    if number not in freq:
        freq[number] = 1

    else :
        freq[number] += 1


    while freq[number] > 1:

        left_number = numbers[left]

        freq[left_number] -= 1
        left += 1

        if freq[left_number] == 0 :
            del freq[left_number]


    length = right - left + 1

    if length > maximum :
        maximum = length

print(maximum)



# Window maintain करायची आहे → dictionary (freq) window 
# मधले elements track करते → duplicate मिळाला → left कडून 
# elements remove करायचे → remove केलेल्या प्रत्येक element ची frequency -1 करायची →
#  duplicate संपेपर्यंत shrink करायचं → मग valid window ची length काढायची → maximum
#  सोबत compare करायची.






