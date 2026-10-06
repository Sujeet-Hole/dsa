
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




s = "aabbcc"


stack = []

for char in s : 

    if not stack : 
        stack.append(char)

    elif stack[-1] == char :
        stack.pop()

    else :
        stack.append(char)

print(stack)



pending
# temperatures = [30, 32, 31, 35, 33]

# # Har temperature ke liye 
# # find karo ki next greater temperature
# #  kitne steps baad aata hai.

# stack = []
# steps = 0
# for index , temperature in enumerate (temperatures ):










