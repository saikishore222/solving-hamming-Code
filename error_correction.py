data_stream=list(map(int,input().split()))
print("recieved message = ",end=" ")
for i in data_stream:
        print(i,end=" ")
print("\n")
l1=[data_stream[6],data_stream[4],data_stream[2],data_stream[0]]
print(l1)
ones_count=l1.count(1)
if((ones_count%2)!=0):
        p1=0
else:
        print("error occured at p1")
        p1=1
l2=[data_stream[5],data_stream[4],data_stream[1],data_stream[0]]
print(l2)
ones_count=l2.count(1)
if((ones_count%2)!=0):
        p2=0
else:
        print("error occured at p2")
        p2=1
l4=[data_stream[3],data_stream[2],data_stream[1],data_stream[0]]
print(l4)
ones_count=l4.count(1)
if((ones_count%2)!=0):
        p4=0
else:
        print("error occured at p4")
        p4=1
error=[]
error.append(p4)
error.append(p2)
error.append(p1)
print(error)
error=error[::-1]
decimal=0
i=0
for j in error:
    decimal+=j * pow(2,i)
    i=i+1
print("error occurred at %d position"%decimal)
print("recieved message = ",end=" ")
for i in data_stream:
        print(i,end=" ")
print("\n")
data_stream=data_stream[::-1]
if(data_stream[decimal-1]==0):
    data_stream[decimal-1]=1
else:
    data_stream[decimal-1]=0
data_stream=data_stream[::-1]
print("correction of data",end=" ")
for i in data_stream:
        print(i,end=" ")
print("\n")
transmit_message=[data_stream[0],data_stream[1],data_stream[2],data_stream[4]]
print("transmit_message:- " ,end=" ")
for i in transmit_message:
            print(i,end=" ")