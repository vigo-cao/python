'''.format'''
print("my name is {},age is {} year old".format("vigo",24))
print("my name is {1},age is {0} year old".format(24,"vigo"))

li = ["yuyan",20]
print("her name is {0},age is {1} year old".format(*li))
lo = {"name":"yuyan","age":20}
print("her name is {name},age is {age} year old".format(**lo))

'''%s'''
print("you name is %s,age is %d year old"%("caoweiguo",24))
qw = ["fussen",8]
print("company name is %s,age is %d year old"%(qw[0],qw[1]))
