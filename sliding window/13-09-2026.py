numbers = [2, 1, 5, 1, 3, 2]
k = 3
currant_sum = 0 
largest_sum = float("-inf")

for i in range(k):
    currant_sum += numbers[i]

largest_sum = currant_sum


for right in range(k, len(numbers)):

    currant_sum -= numbers[right - k]  

    currant_sum+= numbers[right]   


    if largest_sum < currant_sum :
        largest_sum = currant_sum

print(largest_sum)



numbers = [2, 3, 1, 2, 4, 3]
S = 7


window_size = float("inf")
current_sum = 0

for right in range (len(numbers)):

    current_sum += numbers[right]
    current_win+=1

    while currant_sum >= S :
        if current_win < window_size :
            window_size = current_win

        

print(window_size)




# __________________________________________________________________________________________________


# Mujhe contiguous subarray ki minimum length chahiye jiska sum S se at least ho.

# Isliye main right pointer se window ko expand karta hoon aur elements ka current_sum maintain karta hoon.

# Jaise hi current_sum >= S hota hai, iska matlab valid window mil gayi.

# Ab mujhe minimum length chahiye, isliye main left pointer se elements remove karke window ko jitna chhota kar sakta hoon utna chhota karta hoon.

# Har valid window ki length compare karke minimum save karta hoon.

# Jab sum S se neeche chala jaata hai, aur shrink nahi kar sakta, toh right ko aage badha kar window mein naye elements add karta hoon.


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

        # Left wala element remove karo
        current_sum -= numbers[left]

        # Left ko aage move karo
        left += 1

print(window_size)

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
