'''去重'''
# a = [0,2,5,6,2,0,3,4,8,1,2,5,2,5,3,0]
# print(list(set(a)))

''''1','2','3'如何变成['1','2','3']'''
# a = '1','2','3'
# b = []
# for i in a:
#     b.append(i)
# print(b)
#
# c = []
# for i in a:
#     c.append(int(i))
# print(c)

# '''Python一行print出1-100的偶数列表：'''
# print(i for i in range(1-101) if i%2 == 0)

with open("mytest.txt","a") as f:
    f.write("\n") #换行
    f.write("helo,vigo!85")