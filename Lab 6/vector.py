'''def vector_compare(vector1,vector2):
    vector = [max(value) for value in zip(vector1,vector2)]
    return vector


P = {1:{}, 2:{}, 3:{}} 

inc = 0

n1 = int(input("Enter the no. of events in Process 1 : "))
e1 = [i for i in range(1, n1 + 1)]
P[1] = {key: [inc + key, 0, 0] for key in e1}
print(P[1])
print("\n")

n2 = int(input("Enter the no. of events in Process 2 : "))
e2 = [i for i in range(1, n2 + 1)]
P[2] = {key: [0, inc + key, 0] for key in e2}
print(P[2])
print("\n")

n3 = int(input("Enter the no. of events in Process 3 : "))
e3 = [i for i in range(1, n3 + 1)]
P[3] = {key: [0, 0, inc + key] for key in e3}
print(P[3])
print("\n")

comm = int(input("Enter the no of communication lines : "))
print("\n")

while inc < comm:
    sent = int(input("Enter the sending process number : "))
    recv = int(input("Enter the receiving process number : "))
    sent_event_no = int(input("Enter the sending event number : "))
    recv_event_no = int(input("Enter the receiving event number : "))
    if sent <= 3 and recv <= 3:
        print ("P{} --> P{}".format(sent,recv))
        new_vector = vector_compare(P[sent][sent_event_no],P[recv][recv_event_no])
        P[recv][recv_event_no] = new_vector
        print("New vector value of \"event {}\"  in process P{} is : {} \n".format(recv_event_no,recv,P[recv][recv_event_no]))
        
        if (recv_event_no + 1) in P[recv]:
            for i in range(recv_event_no + 1, len(P[recv]) + 1):
                P[recv][i] = vector_compare(P[recv][i-1],P[recv][i])
    else:
        print ("Enter the sent/recv within existing process")
    inc += 1

print("Final vectors of the 3 process are")
print(P[1])
print(P[2])
print(P[3])'''

def vector_compare(v1,v2):
    v = [max(value) for value in zip(v1,v2)]
    return v


p = {1: {},2: {}}
n1 = int(input())
e1 = [i for i in range(n1+1)]
p[1] = {key: [key,0,0] for key in e1 }
print(p[1])

n2 = int(input())
e2 = [i for i in range(n2+1)]
p[2] = {key: [0,key,0] for key in e2}
print(p[2])

send = int(input("Enter the sending process  number:"))
#recv = int(input("Enter the recieving process number: "))
si = int(input("enter senders index number: "))
ri = int(input("Enter the recievers index number: "))

if send<= 2:
    if send == 2:
        print("P{} --> P{}".format(send, 1))
        new_ele = vector_compare(p[send][si],p[1][ri])
        p[1][ri] = new_ele
        print("New vector value of \"event {}\"  in process P{} is : {} \n".format(ri, 1,p[1][ri]))
        if (ri+ 1) in p[1]:
            for i in range(ri + 1, len(p[1]) + 1):
                p[1][i] = vector_compare(p[1][i - 1], p[1][i])
    elif send == 1:
        print("p{} --> p{}".format(send,2))
        new_ele = vector_compare(p[send][si],p[2][ri])
        p[2][ri] = new_ele
        print("The new ele value of \"event{}\" in process p{} is: {} \n".format(ri,2,p[2][ri]))
        if (ri+ 1) in p[2]:
            for i in range(ri + 1, len(p[2]) + 1):
                p[2][i] = vector_compare(p[2][i - 1], p[2][i])
    else:
        print("Enter a valid choice")
print("Final vectors of the 3 process are")
print(p[1])
print(p[2])




