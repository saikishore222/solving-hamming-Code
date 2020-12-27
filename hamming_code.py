from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Hamming Code")
root.geometry('500x450')
root.configure(bg="#11f18e")
root.resizable(0,0)
def error_solution(msg_data,v):
    global label5,root3
    root3=Tk()
    root3.title("Error Detection Solution")
    root3.geometry('1000x700')
    root3.configure(bg="#11f18e")
    Entry_form=Frame(root3)
    Entry_form.pack(side=TOP)
    lbl_title =Label(Entry_form, text="Solution", font="Arial 15 bold", bg="orange",  width = 300,fg="blue")
    lbl_title.pack(fill=X)
    d3=""
    d4=""
    print(d3)
    j=0
    k=7
    for i in range(0,7):
            if(i==3 or i==5 or i==6):
                    d3=d3+"?"
                    d3=d3+"\t"
            else:
                    d3=d3+msg_data[j]
                    d3=d3+"\t"
                    j+=1
            if(k==4 or k==2 or k==1):
                    d4=d4+"P"+str(k)
                    d4=d4+"\t"
                    k=k-1
            else:
                    d4=d4+"D"+str(k)
                    d4=d4+"\t"
                    k=k-1
    print(d3)
    print(msg_data) 
    print(d4)          
    label5=Label(root3,text=d3,bg='#88324f',fg='yellow',font='Arial 15 bold')
    label5.place(x=120,y=50)  
    label6=Label(root3,text=d4,bg='#88324f',fg='yellow',font='Arial 15 bold')
    label6.place(x=120,y=80)
    if(v=="Odd parity"):
        print("question for odd parity")
        data_stream=""
        data_stream+=msg_data[0]+msg_data[1]+msg_data[2]+"0"+msg_data[3]+"0"+"0"
        print(data_stream)
        l=[]
        for i in data_stream:
            l.append(i)
        p1=msg_data[-1]+msg_data[-2]+msg_data[0]
        count=p1.count("1")
        print(count)
        print(p1)
        if((count%2)!=0):
            l[-1]="0"
            label6=Label(root3,text="p1-> 1,3,5,7 -> p1 %s %s %s -> should have %s -> p1 =%d"%(msg_data[-1],msg_data[-2],msg_data[0],v,0),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=150)  
        else:
            l[-1]="1"
            label6=Label(root3,text="p1-> 1,3,5,7 -> p1 %s %s %s -> should have %s -> p1 =%d"%(msg_data[-1],msg_data[-2],msg_data[0],v,1),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=150)  
        p2=msg_data[-1]+msg_data[1]+msg_data[0]
        count=p2.count("1")
        print(count)
        print(p2)
        if((count%2)!=0):
            l[-2]="0"
            label6=Label(root3,text="p2-> 2,3,6,7 -> p2 %s %s %s -> should have %s -> p2 =%d"%(msg_data[-1],msg_data[1],msg_data[0],v,0),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=210)  
        else:
            l[-2]="1"
            label6=Label(root3,text="p2-> 2,3,6,7 -> p2 %s %s %s -> should have %s -> p2 =%d"%(msg_data[-1],msg_data[1],msg_data[0],v,1),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=210)  
        p4=msg_data[2]+msg_data[1]+msg_data[0]
        count=p4.count("1")
        print(count)
        print(p4)
        if((count%2)!=0):
            l[-4]="0"
            label7=Label(root3,text="p4-> 4,5,6,7 -> p4 %s %s %s -> should have %s -> p4 =%d"%(msg_data[2],msg_data[1],msg_data[0],v,0),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label7.place(x=120,y=270)  
        else:
            l[-4]="1"
            label7=Label(root3,text="p4-> 4,5,6,7 -> p4 %s %s %s -> should have %s -> p4 =%d"%(msg_data[2],msg_data[1],msg_data[0],v,1),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label7.place(x=120,y=270)
        print(l)
        data_stream=""
        for i in l:
            data_stream+=i
            data_stream+="\t"
        label5=Label(root3,text="transmitted data ->%s"%(data_stream),bg='#88324f',fg='yellow',font='Arial 15 bold')
        label5.place(x=120,y=420) 
        print(data_stream)
    else:
        print("even parity")
        data_stream=""
        data_stream+=msg_data[0]+msg_data[1]+msg_data[2]+"0"+msg_data[3]+"0"+"0"
        print(data_stream)
        l=[]
        for i in data_stream:
            l.append(i)
        p1=msg_data[-1]+msg_data[-2]+msg_data[0]
        count=p1.count("1")
        print(count)
        print(p1)
        if((count%2)!=0):
            l[-1]="1"
            label6=Label(root3,text="p1-> 1,3,5,7 -> p1 %s %s %s -> should have %s -> p1 =%d"%(msg_data[-1],msg_data[-2],msg_data[0],v,1),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=150)  
        else:
            l[-1]="0"
            label6=Label(root3,text="p1-> 1,3,5,7 -> p1 %s %s %s -> should have %s -> p1 =%d"%(msg_data[-1],msg_data[-2],msg_data[0],v,0),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=150)  
        p2=msg_data[-1]+msg_data[1]+msg_data[0]
        count=p2.count("1")
        print(count)
        print(p2)
        if((count%2)!=0):
            l[-2]="1"
            label6=Label(root3,text="p2-> 2,3,6,7 -> p2 %s %s %s -> should have %s -> p2 =%d"%(msg_data[-1],msg_data[1],msg_data[0],v,1),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=210)  
        else:
            l[-2]="0"
            label6=Label(root3,text="p2-> 2,3,6,7 -> p2 %s %s %s -> should have %s -> p2 =%d"%(msg_data[-1],msg_data[1],msg_data[0],v,0),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=210)  
        p4=msg_data[2]+msg_data[1]+msg_data[0]
        count=p4.count("1")
        print(count)
        print(p4)
        if((count%2)!=0):
            l[-4]="1"
            label7=Label(root3,text="p4-> 4,5,6,7 -> p4 %s %s %s -> should have %s -> p4 =%d"%(msg_data[2],msg_data[1],msg_data[0],v,1),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label7.place(x=120,y=270)  
        else:
            l[-4]="0"
            label7=Label(root3,text="p4-> 4,5,6,7 -> p4 %s %s %s -> should have %s -> p4 =%d"%(msg_data[2],msg_data[1],msg_data[0],v,0),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label7.place(x=120,y=270)
        print(l)
        data_stream=""
        for i in l:
            data_stream+=i
            data_stream+="\t"
        label5=Label(root3,text="transmitted data ->%s"%(data_stream),bg='#88324f',fg='yellow',font='Arial 15 bold')
        label5.place(x=120,y=420) 
        print(data_stream)
def Error_Detection():
    global root1
    root1=Tk()
    root1.title("Error_Detection")
    root1.geometry('700x300')
    root1.configure(bg="#11f18e")
    Entry_form=Frame(root1)
    Entry_form.pack(side=TOP)
    lbl_title = Label(Entry_form, text="Error Detection", font="Arial 15 bold", bg="orange",  width = 300,fg="blue")
    lbl_title.pack(fill=X)
    label_message=Label(root1,text="Message:-",font="Arial 15 bold",bg="#11f18e",fg="blue")
    label_message.place(x=20,y=70)
    msg_field=Entry(root1,width=30,font=("helvetica",14))
    msg_field.place(x=150,y=75)
    label_parity=Label(root1,text="Parity:-",font="Arial 15 bold",bg="#11f18e",fg="blue")
    label_parity.place(x=20,y=120)
    OptionList = ["Odd parity","Even parity"]
    v= StringVar(root1)
    v.set(OptionList[0])
    opt = OptionMenu(root1,v,*OptionList)
    opt.config(font=('Helvetica', 14))
    opt.place(x=150,y=120)
    b3=Button(root1,text="Find",width=25,fg="blue",font="Arial 15 bold",bg="pink",activebackground="pink",activeforeground="blue",command= lambda:error_solution(msg_field.get(),v.get()))
    b3.place(x=150,y=200)
def correct_solution(msg_data,v):
    global label5,root4
    root4=Tk()
    root4.title("Error Correction Solution")
    root4.geometry('1000x700')
    root4.configure(bg="#11f18e")
    Entry_form=Frame(root4)
    Entry_form.pack(side=TOP)
    lbl_title =Label(Entry_form, text="Solution", font="Arial 15 bold", bg="orange",  width = 300,fg="blue")
    lbl_title.pack(fill=X)
    d3=""
    d4=""
    print(d3)
    k=7
    j=0
    for i in range(0,7):
            d3=d3+msg_data[j]
            d3=d3+"\t"
            j=j+1
            if(k==4 or k==2 or k==1):
                d4+="P"+str(k)
                d4+='\t'
            else:
                d4+="D"+str(k)
                d4+='\t'
            k=k-1
    print(d3)
    print(msg_data) 
    print(d4)          
    label5=Label(root4,text=d3,bg='#88324f',fg='yellow',font='Arial 15 bold')
    label5.place(x=120,y=50)  
    label6=Label(root4,text=d4,bg='#88324f',fg='yellow',font='Arial 15 bold')
    label6.place(x=120,y=80)
    if(v=="Odd parity"):
        p1=msg_data[6]+msg_data[4]+msg_data[2]+msg_data[0]
        count=p1.count("1")
        if((count%2)!=0):
            p11=0
            label6=Label(root4,text="p1-> 1,3,5,7 -> %s %s %s %s -> oddparity,no error occured -> p1 =%d"%(msg_data[6],msg_data[4],msg_data[2],msg_data[0],0),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=150) 
        else:
            p11=1
            label6=Label(root4,text="p1-> 1,3,5,7 -> %s %s %s %s -> evenparity  error occured -> p1 =%d"%(msg_data[6],msg_data[4],msg_data[2],msg_data[0],1),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=150) 
        p2=msg_data[5]+msg_data[4]+msg_data[1]+msg_data[0]
        count=p2.count("1")
        if((count%2)!=0):
            p22=0
            label6=Label(root4,text="p2-> 2,3,6,7 -> %s %s %s %s -> oddparity,no error occured -> p2 =%d"%(msg_data[5],msg_data[4],msg_data[1],msg_data[0],0),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=210) 
        else:
            p22=1
            label6=Label(root4,text="p2-> 2,3,6,7 -> %s %s %s %s -> evenparity  error occured -> p2 =%d"%(msg_data[5],msg_data[4],msg_data[1],msg_data[0],1),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=210) 
        p4=msg_data[3]+msg_data[2]+msg_data[1]+msg_data[0]
        count=p4.count("1")
        
        if((count%2)!=0):
            p44=0
            label6=Label(root4,text="p4-> 4,5,6,7 -> %s %s %s %s -> oddparity,no error occured -> p4 =%d"%(msg_data[3],msg_data[2],msg_data[1],msg_data[0],0),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=270) 
        else:
            p44=1
            label6=Label(root4,text="p4-> 4,5,6,7 -> %s %s %s %s -> evenparity  error occured -> p4 =%d"%(msg_data[3],msg_data[2],msg_data[1],msg_data[0],1),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=270) 
        paritysum=[]
        paritysum.append(p11)
        paritysum.append(p22)
        paritysum.append(p44)
        decimal=0
        i=0
        for j in paritysum:
            decimal+=j * pow(2,i)
            i+=1
        label7=Label(root4,text="p4 p2 p1 --> %d %d %d --> error occured at %d position"%(p44,p22,p11,decimal),bg='#88324f',fg='yellow',font='Arial 20 bold')
        label7.place(x=120,y=350)    
        final_list=[]
        for i in msg_data:
            final_list.append(i)
        print(final_list)
        print(decimal)
        if(decimal==0):
            label2=Label(root4,text="There was no error occuredd",bg='#88324f',fg='yellow',font='Arial 15 bold')
            label2.place(x=120,y=490) 
        else:
            final_list=final_list[::-1]
            print(final_list)
            if(final_list[decimal-1]=="0"):
                final_list[decimal-1]="1"
            else:
                final_list[decimal-1]="0"
            print(final_list)
            final_list=final_list[::-1]
            msg1=""
            for i in final_list:
                msg1+=i
                msg1+="\t"
            tmsg=""
            tmsg+=final_list[0]+"\t   "+final_list[1]+"\t"+final_list[2]+"\t"+final_list[4]
            label9=Label(root4,text="correction Data : %s "%(msg1),bg='#88324f',fg='yellow',font='Arial 15 bold')
            label9.place(x=120,y=490) 
            label2=Label(root4,text="Transmitted message : %s "%(tmsg),bg='#88324f',fg='yellow',font='Arial 15 bold')
            label2.place(x=120,y=560) 
    else:
        p1=msg_data[6]+msg_data[4]+msg_data[2]+msg_data[0]
        count=p1.count("1")
        if((count%2)!=0):
            p11=1
            label6=Label(root4,text="p1-> 1,3,5,7 -> %s %s %s %s -> oddparity,error occured -> p1 =%d"%(msg_data[6],msg_data[4],msg_data[2],msg_data[0],1),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=150) 
        else:
            p11=0
            label6=Label(root4,text="p1-> 1,3,5,7 -> %s %s %s %s -> evenparity ,no error occured -> p1 =%d"%(msg_data[6],msg_data[4],msg_data[2],msg_data[0],0),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=150) 
        p2=msg_data[5]+msg_data[4]+msg_data[1]+msg_data[0]
        count=p2.count("1")
        if((count%2)!=0):
            p22=1
            label6=Label(root4,text="p2-> 2,3,6,7 -> %s %s %s %s -> oddparity, error occured -> p2 =%d"%(msg_data[5],msg_data[4],msg_data[1],msg_data[0],1),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=210) 
        else:
            p22=0
            label6=Label(root4,text="p2-> 2,3,6,7 -> %s %s %s %s -> evenparity ,no error occured -> p2 =%d"%(msg_data[5],msg_data[4],msg_data[1],msg_data[0],0),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=210) 
        p4=msg_data[3]+msg_data[2]+msg_data[1]+msg_data[0]
        count=p4.count("1")
        if((count%2)!=0):
            p44=1
            label6=Label(root4,text="p4-> 4,5,6,7 -> %s %s %s %s -> oddparity, error occured -> p4 =%d"%(msg_data[3],msg_data[2],msg_data[1],msg_data[0],1),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=270) 
        else:
            p44=0
            label6=Label(root4,text="p4-> 4,5,6,7 -> %s %s %s %s -> evenparity ,no  error occured -> p4 =%d"%(msg_data[3],msg_data[2],msg_data[1],msg_data[0],0),bg="#11f18e",fg='yellow',font='Arial 20 bold')
            label6.place(x=120,y=270) 
        paritysum=[]
        paritysum.append(p11)
        paritysum.append(p22)
        paritysum.append(p44)
        decimal=0
        i=0
        for j in paritysum:
            decimal+=j * pow(2,i)
            i+=1
        label7=Label(root4,text="p4 p2 p1 --> %d %d %d --> error occured at %d position"%(p44,p22,p11,decimal),bg='#88324f',fg='yellow',font='Arial 20 bold')
        label7.place(x=120,y=350)    
        final_list=[]
        for i in msg_data:
            final_list.append(i)
        print(final_list)
        print(decimal)
        if(decimal==0):
            label2=Label(root4,text="There was no error occuredd",bg='#88324f',fg='yellow',font='Arial 15 bold')
            label2.place(x=120,y=490) 
        else:
            final_list=final_list[::-1]
            print(final_list)
            if(final_list[decimal-1]=="0"):
                final_list[decimal-1]="1"
            else:
                final_list[decimal-1]="0"
            print(final_list)
            final_list=final_list[::-1]
            msg1=""
            for i in final_list:
                msg1+=i
                msg1+="\t"
            tmsg=""
            tmsg+=final_list[0]+"\t   "+final_list[1]+"\t"+final_list[2]+"\t"+final_list[4]
            label9=Label(root4,text="correction Data : %s "%(msg1),bg='#88324f',fg='yellow',font='Arial 15 bold')
            label9.place(x=120,y=490) 
            label2=Label(root4,text="Transmitted message : %s "%(tmsg),bg='#88324f',fg='yellow',font='Arial 15 bold')
            label2.place(x=120,y=560) 
def Error_Correction():
    root2=Tk()
    root2.title("Error Correction")
    root2.geometry('700x300')
    root2.configure(bg="#11f18e")
    lbl_title = Label(root2, text="Error Correction", font="Arial 15 bold", bg="orange",  width = 450,fg="blue")
    lbl_title.pack(side=TOP,fill=X)
    Entry_form=Frame(root2)
    Entry_form.pack(side=TOP)
    label_message=Label(root2,text="Message:-",font="Arial 15 bold",bg="#11f18e",fg="blue")
    label_message.place(x=20,y=70)
    msg_field=Entry(root2,width=30,font=("helvetica",14))
    msg_field.place(x=150,y=75)
    label_parity=Label(root2,text="Parity:-",font="Arial 15 bold",bg="#11f18e",fg="blue")
    label_parity.place(x=20,y=120)
    OptionList = ["Odd parity","Even parity"]
    v= StringVar(root2)
    v.set(OptionList[0])
    opt = OptionMenu(root2,v,*OptionList)
    opt.config(font=('Helvetica', 14))
    opt.place(x=150,y=120)
    b3=Button(root2,text="Find",width=25,fg="blue",font="Arial 15 bold",bg="pink",activebackground="pink",activeforeground="blue",command= lambda:correct_solution(msg_field.get(),v.get()))
    b3.place(x=150,y=200)
def Exit():
    root.destroy()
    root1.destroy()
    root2.destroy()
    root3.destroy()
b1=Button(root,text="Error Detection",width=25,fg="blue",font="Arial 15 bold",bg="pink",activebackground="pink",activeforeground="blue",command=Error_Detection)
b1.pack(padx=0,pady=70)
b2=Button(root,text="Error Correction",width=25,fg="blue",font="Arial 15 bold",bg="pink",activebackground="pink",activeforeground="blue",command=Error_Correction)
b2.pack()
b3=Button(root,text="Exit",width=25,fg="blue",font="Arial 15 bold",bg="pink",activebackground="pink",activeforeground="blue",command=Exit)
b3.pack(padx=0,pady=80)
root.mainloop()