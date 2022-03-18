import sys

T = int(sys.stdin.readline())

for _ in range(T):
    bracket = sys.stdin.readline().strip()
    list=[]
    
    for x in range(len(bracket)):
        if bracket[x] == "(":
            list.append(bracket[x])
        elif bracket[x] == ")":
            if len(list)==0: 
                list.append(bracket[x])
                break
            else: list.pop()
    if len(list) == 0:
        print("YES")
    else:
        print("NO")