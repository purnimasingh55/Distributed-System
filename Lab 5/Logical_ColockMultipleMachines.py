l1=[]
l2=[]

n1 = int(input("Enter the number of elements for list1: "))
n2 = int(input("Enter the number of elements for list2: "))
print("Enter the elements for list 1: ")
for i in range(n1):
    a1 = int(input("Enter the element of list1: "))
    l1.append(a1)
print("Enter the elements for list 2: ")
for i in range(n2):
    a2 = int(input("Enter the element of list2: "))
    l2.append(a2)
print("The 1st list elements are: ",l1)
print("The 2nd  list elements are: ",l2)
n = int(input("Enter the list from which you want to send the msg: "))
s = int(input("Enter the sender's index: "))
r = int(input("Enter the reciever's index: "))
if(n==1):
     if(l1[s]<l2[r]):
        m = max(l1[s],l2[r])+1
        l2[r] = m
        for i in range(r+1,n2):
            m=m+1
            l2[i] = m
        print("Msg is sent successfully.")
        print("Your list2 is updated as: ", l2)
     else:
         print("Sorry! Your Msg can't be delivered.")
elif n==2:
    if (l2[s] < l1[r]):
        m = max(l2[s], l1[r]) + 1
        l1[r] = m
        for i in range(r+1,n1):
            m=m+1
            l1[i] = m
        print("Msg is sent successfully.")
        print("Your list1 is updated as: ",l1)
    else:
        print("Sorry! Your msg can't be delivered.")
else:
    print("Please enter a valid list.")
