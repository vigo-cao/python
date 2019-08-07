def MyPlus(l):
    new_l = []
    for i in l:
        if i not in new_l:
            new_l.append(i)
    return(sum(new_l))

print(MyPlus(l = [3,4,1,2,5,6,6,5,4,3,3]))