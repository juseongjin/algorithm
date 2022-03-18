suf = input()
list=[]
string=''
for s in range(len(suf)):
    string+=suf[s:]
    list.append(string)
    string=''
list.sort()
for s in list:
    print(s)