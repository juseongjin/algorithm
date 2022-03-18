from sys import stdin

n = int(input())
exp = list(stdin.readline().strip())
stack=[]
num=[0]*n

for _ in range(n):
    num[_]=int(input())

while exp:
    if 'A' <= exp[0] <= 'Z':
        stack.append(num[ord(exp[0])-ord('A')])
        exp.pop(0)
    else:
        temp1=stack.pop()
        temp2=stack.pop()
        if exp[0]=='+':
            stack.append(temp1+temp2)
        elif exp[0]=='*':
            stack.append(temp1*temp2)
        elif exp[0]=='/':
            stack.append(temp2/temp1)
        else:
            stack.append(temp2-temp1)
        exp.pop(0)
        
print("{:.2f}".format(stack.pop()))