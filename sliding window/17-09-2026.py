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

numbers = [1, 2, 3, 1, 2, 3, 4]


