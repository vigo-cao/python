'''
如何统计数组中出现次数最多的数据，按出现次数由大到小排序
'''
a = ["a", "b", "a", "c", "a", "c", "b", "d", "e", "c", "a", "c"]

dx = set(a)
# print (dx)
#保存为dict
d = {}
for i in dx:
    d[i] = a.count(i)
print (d)

#对字典按value排序
# a = sorted(d.items(),key=lambda x:x[1],reverse=True)
# print (a)
print(d(1))
