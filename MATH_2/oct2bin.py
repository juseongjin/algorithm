print(format(int(input(),8),'b'))

# from sys import stdin

# def check(list):
#     for item in list:
#         if item == '0':
#             print(item)
#             return False

# oct = list(stdin.readline().strip())
# temp = ''
# if check(oct)==False:
#     print(0)
# else:
#     for i in range(len(oct)):
#         temp += str(int(oct[i])//4)
#         temp += str((int(oct[i])%4)//2)
#         temp += str(((int(oct[i])%4)%2)//1)
#     temp=temp.lstrip('0')
#     temp=temp.lstrip('00')
#     print(temp)

# oct = list(stdin.readline().strip())
# temp = ''
# for i in range(len(oct)):
#     if int(oct[i])%4==0:
#         temp+='100'
#     else:
#         if int(oct[i])//4==0:
#             if int(oct[i])%2==0:
#                 temp+='10'
#             elif int(oct[i])%3==0:
#                 temp+='11'
#             else:
#                 temp+='001'
#         else:
#             if int(oct[i])%2==0:
#                 temp+='110'
#             elif int(oct[i])%5==0:
#                 temp+='101'
#             else:
#                 temp+='111'
# temp=temp.lstrip('00')
# print(temp)