#for single machine
p1 = []
print("Enter the number of msges: ")
n = int(input())

for i in range(n):
    a = int(input())
    p1.append(a)
print(p1)
for i in range(1,n):
    if p1[i-1] < p1[i]:
        print("True")
    else:
        print("False")