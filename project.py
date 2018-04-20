#Nishant Kapoor(16csu229)

from tkinter import *
import tkinter
top=tkinter.Tk()
count=0

#my 5 constraints
Vid=StringVar()
Vname=StringVar()
price=StringVar()
colour=StringVar()
cc=StringVar()

def Add_Vehicle():
    f=open('project.txt','a')     #file is opened where database is created
    Vid=E1.get()
    Vname=E2.get()
    price=E3.get()
    colour=E4.get()
    cc=E5.get()
    if(Vid=='' or Vname=='' or  price=='' or colour=='' or cc==''):
        print("Details can't be empty!")
        exit()
    f.writelines(Vid.ljust(20)+Vname.ljust(20)+price.ljust(20)+colour.ljust(20)+cc.ljust(3)+"\n")
    print("Record added to file!")
    f.close()

def Delete_Vehicle():
    k=Vid.get()
    f=open('project.txt','r')     #file is opened where database is created
    lcount=0
    for line in f:
        lcount=lcount+1
    print("No. of lines in file:")
    print(lcount)
    f.seek(0)
    lines=f.readlines()
    print(lines)
    f.close()
    f=open('project.txt','w')
    for ve in lines: 
        j=ve.split()
        print(j)
        if(j[0]!=k): 
             f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(5)+"\n")
    f.close()
    
def Search_Vehicle():
    k=Vid.get()
    f=open('project.txt','r')
    lcount=0
    flag=0
    for line in f:
        lcount=lcount+1
    print("No. of lines in file:")
    print(lcount)
    f.seek(0)
    lines=f.readlines()         
    print(lines)
    for book in lines: 
        j=book.split() 
        if(j[0]==k):   
            print(j) 
            Vid.set(j[0]) 
            Vname.set(j[1]) 
            price.set(j[2]) 
            colour.set(j[3]) 
            cc.set(j[4])
            flag=1
            break
    if(flag==0):
        print("Record not found!")
    else:
        print("Record found!")
    f.close()

def Update_Vehicle():
    new_Vid=Vid.get()                           #get function reads data which is in entry
    new_Vname=Vname.get() 
    new_price=price.get() 
    new_colour=colour.get() 
    new_cc=cc.get() 
    f=open('project.txt','r')
    lcount=0
    for line in f:
        lcount=lcount+1
    print("No. of lines in file:")
    print(lcount)
    f.seek(0)
    lines=f.readlines() 
    f.close() 
    f=open('project.txt','w') 
    for vec in lines: 
        j=vec.split() 
        if(j[0]!=new_Vid): 
            f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(3)+"\n")     
        else:
            f.writelines(j[0].ljust(20)+new_Vname.ljust(20)+new_price.ljust(20)+new_colour.ljust(20)+new_cc.ljust(3)+"\n")
    print("Record updated!!")        
    f.close()        

def Get_First_Record():
    global count
    count=1
    f=open('project.txt','r')
    lcount=0
    flag=0
    for line in f:
        lcount=lcount+1
    print("No. of lines in file:")
    print(lcount)
    f.seek(0)
    lines=f.readlines()
    l=list(lines)
    print("\n")
    print(l)
    j=l[0].split()
    Vid.set(j[0])
    Vname.set(j[1]) 
    price.set(j[2]) 
    colour.set(j[3]) 
    cc.set(j[4])
    print("\n First Record of file is as:")
    print(l[0])
    f.close()
    
 
def Get_Last_Record():
    f=open('project.txt','r')
    lcount=0
    flag=0
    for line in f:
        lcount=lcount+1
    print("No. of lines in file:")    
    print(lcount)
    f.seek(0)
    lines=f.readlines()
    l=list(lines)
    print(l)
    j=l[lcount-1].split()
    Vid.set(j[0])
    Vname.set(j[1]) 
    price.set(j[2]) 
    colour.set(j[3]) 
    cc.set(j[4])
    print("\n Last Record of file is as:")
    print(l[lcount-1])
    f.close()
    global count
    count=lcount-1


def Get_Next_Record():
    global count 
    i=0
    lcount=0
    f=open('project.txt','r')
    for line in f:
        lcount=lcount+1
    print("No. of lines in file:")    
    print(lcount)                         #counts number of lines
    f.seek(0)
    try: 
        while(i<=count): 
            l=f.readline() 
            i=i+1 
        m=l.split() 
        Vid.set(m[0]) 
        Vname.set(m[1]) 
        price.set(m[2]) 
        colour.set(m[3]) 
        cc.set(m[4]) 
        print(m)
    except:
        Vid.set("") 
        Vname.set("") 
        price.set("") 
        colour.set("") 
        cc.set("")
        print("Sorry, no more records are there in database!")
    count=count+1 
    f.close()

def Get_Prev_Record():
    global count 
    i=0
    lcount=0
    f=open('project.txt','r')
    for line in f:
        lcount=lcount+1
    print("No. of lines in file:")    
    print(lcount)
    f.seek(0)
    try: 
        while(i<=count-1): 
            l=f.readline() 
            i=i+1 
        m=l.split() 
        Vid.set(m[0]) 
        Vname.set(m[1]) 
        price.set(m[2]) 
        colour.set(m[3]) 
        cc.set(m[4]) 
        print(m)
    except:
        Vid.set("") 
        Vname.set("") 
        price.set("") 
        colour.set("") 
        cc.set("")
        print("Sorry, no more records are there in database!")
    count=count-1 
    f.close()
    
tkinter.Label(top, text="Vehicle Id:",font=('comic sans ms',15,'bold'),bg="lightcoral").grid(row=0)          #label creation
tkinter.Label(top, text="Vehicle Name:",font=('comic sans ms',15,'bold'),bg="lightcoral").grid(row=1)
tkinter.Label(top, text="Vehicle Price:",font=('comic sans ms',15,'bold'),bg="lightcoral").grid(row=2)
tkinter.Label(top, text="Vehicle Colour:",font=('comic sans ms',15,'bold'),bg="lightcoral").grid(row=3)
tkinter.Label(top, text="Vehicle  Cc:",font=('comic sans ms',15,'bold'),bg="lightcoral").grid(row=4)
E1 = tkinter.Entry(top,textvariable=Vid)
E2 = tkinter.Entry(top,textvariable=Vname)
E3 = tkinter.Entry(top,textvariable=price)
E4 = tkinter.Entry(top,textvariable=colour)
E5 = tkinter.Entry(top,textvariable=cc)
E1.grid(row=0, column=1)
E2.grid(row=1, column=1)
E3.grid(row=2, column=1)
E4.grid(row=3, column=1)
E5.grid(row=4, column=1)

b1=tkinter.Button(top,text="First Record |<",width=15,bg="lightseagreen",font=('comic sans ms',15,'bold'),command=Get_First_Record).grid(row=5, column=0) #button creation
b2=tkinter.Button(top,text="<",width=15,bg="yellow",font=('comic sans ms',15,'bold'),command=Get_Prev_Record).grid(row=5, column=1)
b3=tkinter.Button(top,text=">",width=15,bg="yellow",font=('comic sans ms',15,'bold'),command=Get_Next_Record).grid(row=5, column=2)
b4=tkinter.Button(top,text="Last Record >|",width=15,bg="lightseagreen",font=('comic sans ms',15,'bold'),command=Get_Last_Record).grid(row=5, column=3)

b5=tkinter.Button(top,text="ADD",width=15,bg="lightseagreen",font=('comic sans ms',15,'bold'),command=Add_Vehicle).grid(row=6, column=0)
b6=tkinter.Button(top,text="DELETE",width=15,bg="yellow",font=('comic sans ms',15,'bold'),command=Delete_Vehicle).grid(row=6, column=1)
b7=tkinter.Button(top,text="SEARCH",width=15,bg="yellow",font=('comic sans ms',15,'bold'),command=Search_Vehicle).grid(row=6, column=2)
b8=tkinter.Button(top,text="UPDATE",width=15,bg="lightseagreen",font=('comic sans ms',15,'bold'),command=Update_Vehicle).grid(row=6, column=3)

b9=tkinter.Button(top,text="EXIT",width=63,bg="red",font=('comic sans ms',15,'bold'),command=top.destroy).grid(row=7, column=0,columnspan=4)

top.configure(bg="lightcoral")
top.mainloop()
