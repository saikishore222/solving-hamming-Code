l=list(map(int,input().split()))
data_stream=[]
for i in range(0,7):
        data_stream.append(0)
data_bits=[0,1,2,4]
k=0
for i in data_bits:
        data_stream[i]=l[k]
        k+=1
for i in data_stream:
        print(i,end=" ")
print("\n")
p1=[data_stream[4],data_stream[2],data_stream[0]]
ones_count=p1.count(1)
print(ones_count)
if((ones_count%2)!=0):
        data_stream[6]=0
else:
        data_stream[6]=1
p2=[data_stream[4],data_stream[1],data_stream[0]]
ones_count=p2.count(1)
print(ones_count)
if((ones_count%2)!=0):
        data_stream=data_stream[:5]+"0"
else:
        data_stream=data_stream[:5]+"0"
p4=[data_stream[2],data_stream[1],data_stream[0]]
ones_count=p4.count(1)
print(ones_count)
if((ones_count%2)!=0):
        data_stream[3]=0
else:
        data_stream[3]=1
        
print("Transmitted Data:- ",end=" ")
for i in data_stream:
        print(i,end=" ")
