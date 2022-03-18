from sys import stdin

exp = list(stdin.readline().strip())
stack=[]
res=""

while exp:
    if exp[0].isalpha() :
        res+=exp.pop(0)
    # 편집점
    elif exp[0] == '(':
        stack.append(exp.pop(0))
    elif exp[0] == ')':
        while stack and stack[-1] !='(':
            res+=stack.pop()
        # 여는 괄호를 만나면 stack에서 pop
        stack.pop()
        exp.pop(0) 
    elif exp[0] == '+' or exp[0] == '-':
        # 본인보다 우선순위가 높거나 같은 연산은 res에 담고 본인은 stack에
        while stack and stack[-1] !='(':
            res+=stack.pop()
        stack.append(exp.pop(0))
    elif exp[0] == '*' or exp[0] =='/':
        # 본인보다 우선순위가 높거나 같은 연산은 res에 담고 본인은 stack에
        while stack and (stack[-1] =='*' or stack[-1] =='/'):
            res+=stack.pop()
        stack.append(exp.pop(0))
while stack:
    res+=stack.pop()
print(res)