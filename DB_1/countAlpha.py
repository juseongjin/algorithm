word = input()

stack=[0]*26

for s in word:
    stack[ord(s) - 97] += 1
print(*stack)