# ============================================================
# SLIDING WINDOW NOTES + PRACTICE
# ============================================================


# PATTERN:

# Sliding Window


# WHEN:

# Contiguous / consecutive elements


# POINTERS:

# left = window start
# right = window end


# STATE:

# sum / count / frequency / etc.


# MOVEMENT:

# right -> expand
# left -> shrink


# Fixed K:

# window size = k


# Minimum:

# valid -> shrink -> minimum


# Maximum:

# invalid -> shrink -> maximum



# ============================================================
# 1. AVERAGE OF EVERY K CONSECUTIVE ELEMENTS
# ============================================================

numbers = [2, 1, 5, 1, 3, 2]

k = 3

window_sum = 0

left = 0

average = []

for i in range(k):

    window_sum += numbers[i]

current_average = window_sum / k

average.append(current_average)


for right in numbers[3:]:

    window_sum -= numbers[left]

    window_sum += right

    current_window_average = window_sum / k

    average.append(current_window_average)

    left += 1

print(average)



# ============================================================
# 2. MAXIMUM VOWELS IN K CONSECUTIVE CHARACTERS
# ============================================================

text = "abciiidef"

k = 3

vowels = ["a", "e", "i", "o", "u"]

left = 0

largest = 0

vowel_count = 0

for right in range(k):

    if text[right] in vowels:

        vowel_count += 1

largest = vowel_count

for right in range(k, len(text)):

    if text[left] in vowels:

        vowel_count -= 1

    if text[right] in vowels:

        vowel_count += 1

    left += 1

    if vowel_count > largest:

        largest = vowel_count

print(largest)



# ============================================================
# 3. MAXIMUM SUM OF K CONSECUTIVE ELEMENTS
# ============================================================

numbers = [2, 1, 5, 8, 2, 9, 1]

k = 3

left = 0

window_sum = 0

largest_sum = 0

for right in range(k):

    window_sum += numbers[right]

largest_sum = window_sum

for right in range(k, len(numbers)):

    window_sum -= numbers[left]

    window_sum += numbers[right]

    left += 1

    if largest_sum < window_sum:

        largest_sum = window_sum

print(largest_sum)



# ============================================================
# 4. MAXIMUM SUM - SAME PRACTICE AGAIN
# ============================================================

numbers = [2, 1, 5, 1, 3, 2]

k = 3

currant_sum = 0

largest_sum = float("-inf")

for i in range(k):

    currant_sum += numbers[i]

largest_sum = currant_sum

for right in range(k, len(numbers)):

    currant_sum -= numbers[right - k]

    currant_sum += numbers[right]

    if largest_sum < currant_sum:

        largest_sum = currant_sum

print(largest_sum)



# ============================================================
# 5. MINIMUM SUBARRAY - FIRST ATTEMPT    .     first me wrong kel hovt them mech te correct kel so aata 2 same version aahe , khali pan same version aahe 
# ============================================================

numbers = [2, 3, 1, 2, 4, 3]

S = 7
left = 0
minimum = float("inf")
window_sum = 0

for right in range(len(numbers)):

    window_sum += numbers[right]

    while window_sum >= S : 

        window_length = right - left + 1

        if window_length < minimum :
            minimum = window_length

        window_sum -= numbers[left]

        left+=1

print(f"the minimus sum is2 {minimum}")




# ============================================================
# 6. MINIMUM SUBARRAY - SECOND ATTEMPT
# ============================================================

numbers = [2, 3, 1, 2, 4, 3]

S = 7

left = 0

current_sum = 0

window_size = float("inf")

for right in range(len(numbers)):

    # Right se element window mein add karo

    current_sum += numbers[right]

    # Jab tak sum target se >= hai,
    # window ko left se chhota karte raho

    while current_sum >= S:

        # Current window ki length

        current_window = right - left + 1

        # Minimum length update karo

        if current_window < window_size:

            window_size = current_window

        current_sum -= numbers[left]

        # Left ko aage move karo

        left += 1

print(window_size)



# ============================================================
# 7. MINIMUM SUBARRAY - THIRD ATTEMPT
# ============================================================

numbers = [2, 3, 1, 2, 4, 3]

S = 7

current_sum = 0

window_size = float("inf")

left = 0

for right in range(len(numbers)):

    current_sum += numbers[right]

    while current_sum >= S:

        current_window = right - left + 1

        if current_window < window_size:

            window_size = current_window

        current_sum -= numbers[left]

        left += 1

print(window_size)



# ============================================================
# 8. MAXIMUM LENGTH SUBARRAY WITH SUM <= S
# ============================================================

numbers = [2, 1, 5, 2, 3, 2]

S = 7

left = 0

current_sum = 0

size = float("-inf")

for right in range(len(numbers)):

    current_sum += numbers[right]

    while current_sum > S:

        current_sum -= numbers[left]

        left += 1

    current_window = right - left + 1

    if current_window > size:

        size = current_window

print(size)



# ============================================================
# 9. AT MOST 2 UNIQUE NUMBERS - FIRST ATTEMPT
# ============================================================

# "Mujhe array mein sabse lambi continuous window
# find karni hai jisme maximum 2 unique numbers ho."

numbers = [1, 2, 1, 2, 3]

unique = [1, 2]

for num in numbers:

    if num not in unique:

        numbers.remove(num)

print(numbers)



# ============================================================
# 10. FREQUENCY COUNT - FIRST ATTEMPT
# ============================================================

numbers = [1, 2, 1, 2, 3]

freq = {}

left = 0

for right in numbers:

    if right not in freq:

        freq[right] = 0

    else:

        freq[right] += 1



# ============================================================
# 11. AT MOST 2 UNIQUE NUMBERS - FREQUENCY APPROACH
# ============================================================

numbers = [1, 2, 1, 2, 3]

freq = {}

largest = float("-inf")

left = 0

for right in range(len(numbers)):

    num = numbers[right]

    if num not in freq:

        freq[num] = 0

    freq[num] += 1

    while len(freq) > 2:

        left_num = numbers[left]

        freq[left_num] -= 1

        if freq[left_num] == 0:

            del freq[left_num]

        left += 1

    current_window = right - left + 1

    if current_window > largest:

        largest = current_window

print(largest)



# ============================================================
# 12. LONGEST CONTIGUOUS SUBARRAY WITH NO DUPLICATES
# ============================================================

numbers = [1, 2, 1, 3, 4, 2, 3]

freq = {}

largest = float("-inf")

left = 0

for right in range(len(numbers)):

    num = numbers[right]

    if num not in freq:

        freq[num] = 0

    freq[num] += 1

    while freq[num] > 1:

        left_num = numbers[left]

        freq[left_num] -= 1

        if freq[left_num] == 0:

            del freq[left_num]

        left += 1

    current_window = right - left + 1

    if current_window > largest:

        largest = current_window

print(largest)



# ============================================================
# 13. AVERAGE OF EVERY K CONSECUTIVE ELEMENTS - REPEATED
# ============================================================

numbers = [2, 1, 5, 1, 3, 2]

k = 3

window_sum = 0

left = 0

average = []

for i in range(k):

    window_sum += numbers[i]

current_average = window_sum / k

average.append(current_average)


for right in numbers[3:]:

    window_sum -= numbers[left]

    window_sum += right

    current_window_average = window_sum / k

    average.append(current_window_average)

    left += 1

print(average)



# ============================================================
# 14. MAXIMUM VOWELS - REPEATED
# ============================================================

text = "abciiidef"

k = 3

vowels = ["a", "e", "i", "o", "u"]

left = 0

largest = 0

vowel_count = 0

for right in range(k):

    if text[right] in vowels:

        vowel_count += 1

largest = vowel_count

for right in range(k, len(text)):

    if text[left] in vowels:

        vowel_count -= 1

    if text[right] in vowels:

        vowel_count += 1

    left += 1

    if vowel_count > largest:

        largest = vowel_count

print(largest)



# ============================================================
# 15. MAXIMUM SUM - REPEATED
# ============================================================

numbers = [2, 1, 5, 8, 2, 9, 1]

k = 3

left = 0

window_sum = 0

largest_sum = 0

for right in range(k):

    window_sum += numbers[right]

largest_sum = window_sum

for right in range(k, len(numbers)):

    window_sum -= numbers[left]

    window_sum += numbers[right]

    left += 1

    if largest_sum < window_sum:

        largest_sum = window_sum

print(largest_sum)



# ============================================================
# 16. TEST SESSION - MAXIMUM SUM
# ============================================================

numbers = [2, 1, 5, 1, 3, 2]

k = 3

left = 0

window_sum = 0

currant_sum = 0

for right in range(k):

    window_sum += numbers[right]

currant_sum = window_sum

for right in range(k, len(numbers)):

    window_sum -= numbers[left]

    window_sum += numbers[right]

    left += 1

    if window_sum < currant_sum:

        window_sum = currant_sum

print(f"largest sum is {window_sum}")



# ============================================================
# 17. TEST SESSION - MINIMUM LENGTH
# ============================================================

numbers = [2, 3, 1, 2, 4, 3]

S = 7

minimum = float("inf")

left = 0

window_sum = 0

for right in range(len(numbers)):

    window_sum += numbers[right]

    while window_sum >= S:

        length = right - left + 1

        if minimum > length:

            minimum = length

        window_sum -= numbers[left]

        left += 1

print(minimum)


