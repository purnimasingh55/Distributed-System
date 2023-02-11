def ChangeList(ls,maxi,r):
    ls[r] = maxi


def vector_compare(vector1,vector2):
    vector = [max(value) for value in zip(vector1,vector2)]
    return vector


n1 = int(input("Enter the size of process 1: "))
n2 = int(input("Enter the size of process 2: "))
l1 = []
l2 = []
k =1

for i in range(n1):
    l1.append([])
    l1[i].append(k)
    l1[i].append(0)
    k=k+1
       # print(l1[i])


print(l1)
m=1
for i in range(n2):
    l2.append([])
    l2[i].append(0)
    l2[i].append(m)
    m = m + 1

print(l2)
ln1= int(input("Enter the list from which you want to send the data: "))
s = int(input("Enter the index from which you want to send data "))
r = int(input("Enter the reciving index: "))
if ln1 == 1:
    for i in range(2):
        maxi = vector_compare(l1[r[1]],l1[r[0]],l1[r])
        ChangeList(l1,maxi,r)



else:
    for i in range(2):
        maxi1 = vector_compare(l2[r[1]],l2[r[0]],l1[r])
        ChangeList(l1,maxi1,r)


print(l1)
print(l2)