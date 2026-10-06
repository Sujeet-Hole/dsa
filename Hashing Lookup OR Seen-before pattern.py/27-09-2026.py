numbers = [3, 4, -2, 5, -5]
target = 5

prefix_sum = 0 
seen = {0 : -1}

for index , number in enumerate (numbers):

    prefix_sum += number

    required = prefix_sum - target 


    if required in seen : 
        print(seen[required]+1 , index)


    seen[prefix_sum] = index
s = "listen"
t = "silent"

if len(s) != len(t):
    print("Not anagram")

else:
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char in t:
        if char not in freq:
            print("Not anagram")
            break

        freq[char] -= 1


    else:
        if all(count == 0 for count in freq.values()):
            print("Anagram")
        else:
            print("Not anagram")


numbers = [4, 1, 2, 1, 2, 7, 4]
freq = {}
for char in numbers : 
    freq[char] = freq.get(char , 0) + 1 
for num in freq :
    if freq[num] == 1 :
        print(num)

l = [2, 7, 11, 2, 15, 7]
freq = {}
for num in l :

    if num in freq : 
        print(num)
        break

    freq[num] = freq.get(num , 0) + 1


s = "([{}])"
stack = []

hashmap = {
    ")" : "(",
    "]": "[",
    "}" : "{"
}

for char in s :
    if char not in hashmap:
        stack.append(char)

    else : 
          if not stack:
            print("Not Balanced")
            break      


          if hashmap[char] != stack[-1]:
            print("Not Balanced")
            break

          stack.pop()
else:
    if not stack:
        print("Balanced")
    else:
        print("Not Balanced")






s = "abbaca"
stack = []
for char in s : 
    if not stack :
        stack.append(char)
    elif stack[-1] == char : 
        stack.pop()
    else : 
        stack.append(char)
print(stack)
