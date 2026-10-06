# ============================================================
# PREVIOUS-CURRENT PATTERN
# ============================================================

# LEARNED:
# Previous aur current element ko track karke unke beech
# fixed difference check karna.
# Pattern: current - previous == expected_difference

numbers = [3, 5, 7, 9, 11]

left = 1
expected_difference = 2

for right in numbers[1:]:
    if right - numbers[left - 1] != expected_difference:
        print(False)
        break

    left += 1

else:
    print(True)


# ============================================================
# PREVIOUS-CURRENT PATTERN
# ============================================================

# LEARNED:
# Adjacent elements ka difference calculate karke
# running largest value maintain karna.
#
# IMPORTANT:
# Largest find karne ke liye saare differences list mein
# store karna zaroori nahi hai.
# Running maximum se O(1) extra space mein solve kar sakte hain.

numbers = [10, 12, 158, 19, 24, 54]

left = 1
largest = float("-inf")

for right in numbers[1:]:
    d = right - numbers[left - 1]

    if d > largest:
        largest = d

print(largest)


# ============================================================
# PREVIOUS-CURRENT PATTERN
# ============================================================

# LEARNED:
# Previous aur current ka difference calculate karke
# condition satisfy hone par counter increase karna.
#
# Pattern:
# previous + current
#        ↓
#    difference
#        ↓
#    condition
#        ↓
#      count

numbers = [10, 12, 158, 19, 24, 54]

left = 1
count = 0

for right in numbers[1:]:
    d = right - numbers[left - 1]

    if d > 3:
        count += 1

print(count)


# ============================================================
# PREVIOUS-CURRENT PATTERN
# ============================================================

# LEARNED:
# Difference calculate karne ke bajay directly check kar sakte hain
# ki current element = previous element + expected value hai ya nahi.
#
# Pattern:
# previous + 3 == current

numbers = [2, 5, 9, 12, 18, 21]

left = 1
count1 = 0

for right in numbers[1:]:
    if numbers[left - 1] + 3 == right:
        count1 += 1

    left += 1

print(count1)


# ============================================================
# TWO POINTERS — PAIR SUM
# ============================================================

# LEARNED:
# Sorted array mein pair ka target sum find karne ke liye
# left aur right pointers use kar sakte hain.
#
# Pattern:
# sum > target → right--
# sum < target → left++
# sum == target → answer found
#
# TC: O(n)
# SC: O(1)

numbers = [1, 2, 3, 4, 5, 6]

left = 0
right = len(numbers) - 1
target = 9

while left < right:
    total = numbers[left] + numbers[right]

    if total == target:
        print(True)
        break

    if total > target:
        right -= 1

    if total < target:
        left += 1

else:
    print(False)


# ============================================================
# TWO POINTERS — PAIR SUM
# ============================================================

# LEARNED:
# Same Two Pointers pattern ko different target ke saath
# independently apply karna.
#
# IMPORTANT:
# Sorted array hone ki wajah se pointer movement possible hai.

numbers = [1, 2, 3, 4, 6, 8, 10]

left = 0
right = len(numbers) - 1
target = 10

while left < right:
    total = numbers[left] + numbers[right]

    if total == target:
        print(True)
        break

    if total > target:
        right -= 1

    if total < target:
        left += 1

else:
    print(False)


# ============================================================
# TWO POINTERS — PAIR DIFFERENCE
# ============================================================

# LEARNED:
# Two Pointers sirf sum ke liye nahi hote.
# Sorted array mein current difference ko target ke saath
# compare karke pointers move kar sakte hain.
#
# Pattern:
# difference > target → right--
# difference < target → left++

numbers = [1, 2, 3, 4, 5, 6, 7]

left = 0
right = len(numbers) - 1
target = 4

while left < right:
    total = numbers[right] - numbers[left]

    if total == target:
        print("TRUE")
        break

    if total > target:
        right -= 1

    if total < target:
        left += 1

else:
    print(False)


# ============================================================
# PREVIOUS-CURRENT PATTERN
# ============================================================

# LEARNED:
# Adjacent elements ke difference mein minimum value
# running minimum ke through find kar sakte hain.
#
# IMPORTANT:
# Saare differences store karne ki zarurat nahi.
# Running minimum → O(1) extra space.

numbers = [1, 2, 4, 7, 9, 12]

left = 0
minimum = float("inf")

for right in range(1, len(numbers)):
    difference = numbers[right] - numbers[left]

    if difference > 0 and difference < minimum:
        minimum = difference

    left += 1

print(minimum)


# ============================================================
# TWO POINTERS — PAIR SUM
# ============================================================

# LEARNED:
# Two Pointers ko repeatedly use karne ka goal template
# memorize karna nahi, pointer movement ka reason samajhna hai.
#
# Sorted array:
# sum > target → right--
# sum < target → left++

numbers = [1, 2, 3, 4, 6, 8, 9]

left = 0
right = len(numbers) - 1
target = 10

while left < right:
    total = numbers[left] + numbers[right]

    if total == target:
        print(True)
        break

    if total > target:
        right -= 1

    if total < target:
        left += 1

else:
    print(False)


# ============================================================
# TWO POINTERS — REVERSE ARRAY IN-PLACE
# ============================================================

# LEARNED:
# Two Pointers ka use sirf searching ke liye nahi hai.
# Opposite ends se start karke elements swap kar sakte hain.
#
# Pattern:
# left/right → swap → left++ → right--
#
# SC: O(1) because new array create nahi ki.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

left = 0
right = len(numbers) - 1

while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]

    left += 1
    right -= 1

print(numbers)


# ============================================================
# MOVE ZEROES — FIRST APPROACH
# ============================================================

# LEARNED:
# Zeroes ko identify karke remove karna aur baad mein
# unhe end mein add karna possible hai.
#
# BUT:
# pop(index) repeatedly use karne se elements shift hote hain,
# isliye worst-case TC O(n²) ho sakti hai.
#
# This approach helped identify the bottleneck:
# repeated pop / shifting.

numbers = [1, 0, 3, 0, 5, 0, 7]

left = 0

for right in range(len(numbers) - 1, -1, -1):
    if numbers[right] == 0:
        numbers.pop(right)

    left += 1

for _ in range(left, len(numbers)):
    numbers[left] = 0

print(numbers)


# ============================================================
# MOVE ZEROES — OPTIMIZED TWO POINTERS
# ============================================================

# LEARNED:
# Two Pointers mein ek pointer scanning ke liye aur
# ek pointer placement ke liye use ho sakta hai.
#
# right  → array scan karta hai
# left   → next non-zero ki position track karta hai
#
# Non-zero mila:
# → left position par place/swap
# → left++
#
# Zero mila:
# → kuch nahi
#
# TC: O(n)
# SC: O(1)

numbers = [0, 1, 0, 3, 12]

left = 0

for right in range(len(numbers)):
    if numbers[right] != 0:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1

print(numbers)


# ============================================================
# TWO POINTERS — PALINDROME
# ============================================================

# LEARNED:
# Array ke opposite ends ko compare karke palindrome check karna.
#
# Pattern:
# left/right → compare
# match → dono inward move
# mismatch → immediately False
#
# TC: O(n)
# SC: O(1)

numbers = [1, 2, 3, 2, 1]

left = 0
right = len(numbers) - 1

while left < right:
    if numbers[left] != numbers[right]:
        print(False)
        break

    left += 1
    right -= 1

else:
    print(True)


    