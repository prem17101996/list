lst=[1,1,2,3,1,4,5,6,8,88,8]
lst1=[]
for i in lst:

    if i not in lst1:
        lst1.append(i)
print(lst1)
