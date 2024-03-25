qujian1=int(input())
qujian2=int(input())
list=[]
for i in range(qujian1,qujian2+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
             list.append(i)
print(list)

#for...else 为特殊用法

