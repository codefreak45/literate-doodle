from tkinter import *
from tkinter import messagebox
count = 1 
a= 0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
z=False
def press(x):
    global count,a,b,c,d,e,f,g,h,i,z
    global l1,l2,l3,l4,l5,l6,l7,l8,l9
    if count % 2 == 0:
        l=Label(t,text="X's Turn",bg='white',            fg='navy',font=( 'icourier',40,'bold')).            place(x=100,y=300,w=900,h=200)
        if x == 9:
            l9=Button(t,text='O',                         fg='green',bd=8,font=('Courier',30,               'bold'))
            l9.place(x=730,y=1240,                     w=300,h=300)
            count=count+1
            i= 2
        if x == 8:
            l8=Button(t,text='O',                         fg='green',bd=8,font=('Courier',30,               'bold'))
            l8.place(x=410,y=1240,                     w=300,h=300)
            count=count+1
            h=2
        if x == 7:
            l7=Button(t,text='O',                         fg='green',bd=8,font=('Courier',30,               'bold'))
            l7.place(x=90,y=1240,                     w=300,h=300)
            count=count+1
            g=2
        if x == 6:
            l6=Button(t,text='O',                         fg='green',bd=8,font=('Courier',30,               'bold'))
            l6.place(x=730,y=920,                     w=300,h=300)
            count=count+1
            f=2
        if x == 5:
            l5=Button(t,text='O',                         fg='green',bd=8,font=('Courier',30,               'bold'))
            l5.place(x=410,y=920,                     w=300,h=300)
            count=count+1
            e=2
        if x == 4:
            l4=Button(t,text='O',                         fg='green',bd=8,font=('Courier',30,               'bold'))
            l4.place(x=90,y=920,                     w=300,h=300)
            count=count+1
            d=2
        if x == 3:
            l3=Button(t,text='O',                         fg='green',bd=8,font=('Courier',30,               'bold'))
            l3.place(x=730,y=600,                     w=300,h=300)
            count=count+1
            c=2
        if x == 2:
            l2=Button(t,text='O',                         fg='green',bd=8,font=('Courier',30,               'bold'))
            l2.place(x=410,y=600,                     w=300,h=300)
            count=count+1
            b=2
        if x == 1:
            l1=Button(t,text='O',                         fg='Green',bd=8,font=('Courier',30,               'bold'))
            l1.place(x=90,y=600,                     w=300,h=300)
            count=count+1
            a=2
    elif count % 2 != 0:
        l=Label(t,text="O's Turn",bg='white',            fg='navy',font=( 'icourier',40,'bold')).            place(x=100,y=300,w=900,h=200)
        if x == 9:
            l9=Button(t,text='X',                         fg='Blue',bd=8,font=('Courier',30,               'bold'))
            l9.place(x=730,y=1240,                     w=300,h=300)
            count=count+1
            i=1
        if x == 8:
            l8=Button(t,text='X',                         fg='Blue',bd=8,font=('Courier',30,               'bold'))
            l8.place(x=410,y=1240,                     w=300,h=300)
            count=count+1
            h=1
        if x == 7:
            l7=Button(t,text='X',                         fg='Blue',bd=8,font=('Courier',30,               'bold'))
            l7.place(x=90,y=1240,                     w=300,h=300)
            count=count+1
            g=1
        if x == 6:
            l6=Button(t,text='X',                         fg='Blue',bd=8,font=('Courier',30,               'bold'))
            l6.place(x=730,y=920,                     w=300,h=300)
            count=count+1
            f=1
        if x == 5:
            l5=Button(t,text='X',                         fg='Blue',bd=8,font=('Courier',30,               'bold'))
            l5.place(x=410,y=920,                     w=300,h=300)
            count=count+1
            e=1
        if x == 4:
            l4=Button(t,text='X',                         fg='Blue',bd=8,font=('Courier',30,               'bold'))
            l4.place(x=90,y=920,                     w=300,h=300)
            count=count+1
            d=1
        if x == 3:
            l3=Button(t,text='X',                         fg='Blue',bd=8,font=('Courier',30,               'bold'))
            l3.place(x=730,y=600,                     w=300,h=300)
            count=count+1
            c=1
        if x == 2:
            l2=Button(t,text='X',                         fg='Blue',bd=8,font=('Courier',30,               'bold'))
            l2.place(x=410,y=600,                     w=300,h=300)
            count=count+1
            b=1
        if x == 1:
            l1=Button(t,text='X',                         fg='Blue',bd=8,font=('Courier',30,               'bold'))
           
            l1.place(x=90,y=600,                           w=300,h=300)
            count=count+1
            a=1
    
    if (a==2 and b==2 and c ==2) or (a==2 and d==2 and g==2) or (a==2 and e==2 and i==2) or (b==2 and e==2 and h==2) or (c==2 and e==2 and g==2) or (c==2 and f==2 and i==2) or (d==2 and e==2 and f==2) or (g==2 and h==2 and i==2) :
        messagebox.showinfo('Congratulations',        'Player O has won the game')
        count=1
        
        z = True
        answer=messagebox.askyesno('Replay','Do you want to restart')
        if answer:
           count=1
           z=False
           if a==1 or a==2:
               l1.destroy()
           if b==1 or b==2:
               l2.destroy()
           if c==1 or c==2:
               l3.destroy()
           if d==1 or d==2: 
               l4.destroy()
           if e==1 or e==2:
               l5.destroy()
           if f==1 or f==2:
               l6.destroy()
           if g==1 or g==2:
               l7.destroy()
           if h==1 or h==2:
               l8.destroy()
           if i==1 or i==2:
               l9.destroy()
           a=0
           b=0
           c=0
           d=0
           e=0
           f=0
           g=0
           h=0
           i=0
        else:
           t.destroy()
 
    if (a==1 and b==1 and c ==1) or (a==1 and d==1 and g==1) or (a==1 and e==1 and i==1) or (b==1 and e==1 and h==1) or (c==1 and e==1 and g==1) or (c==1 and f==1 and i==1) or (d==1 and e==1 and f==1) or (g==1 and h==1 and i==1) :
        messagebox.showinfo('Congratulations',        'Player X has won the game')
        count=1
        
        z=True
        answer=messagebox.askyesno('Replay','Do you want to restart')
        if answer:
           count=1
           z=False
           z=False
           if a==1 or a==2:
               l1.destroy()
           if b==1 or b==2:
               l2.destroy()
           if c==1 or c==2:
               l3.destroy()
           if d==1 or d==2: 
               l4.destroy()
           if e==1 or e==2:
               l5.destroy()
           if f==1 or f==2:
               l6.destroy()
           if g==1 or g==2:
               l7.destroy()
           if h==1 or h==2:
               l8.destroy()
           if i==1 or i==2:
               l9.destroy()
           a=0
           b=0
           c=0
           d=0
           e=0
           f=0
           g=0
           h=0
           i=0
        else:
           t.destroy()


    if count==10 and z==False:
       messagebox.showinfo('Oops','Match Tied')
       answer=messagebox.askyesno('Replay','Do you want to restart')
       if answer:
           count=1
           a=0
           b=0
           c=0
           d=0
           e=0
           f=0
           g=0
           h=0
           i=0
           try:
               l1.destroy()
               l2.destroy()
               l3.destroy()
               l4.destroy()
               l5.destroy()
               l6.destroy()
               l7.destroy()
               l8.destroy()
               l9.destroy()
           except:
               t.destroy()
       else:
           t.destroy()



global f1

t=Tk()
'''can=Canvas(t)
can.config(bg='teal')
can.pack(expand=True,fill=BOTH)'''
f1 = Frame(t,bg='black').place(x=90,y=600,w=940,h=940)
btn1=Button(t,bg='black',bd=8,command=lambda : press(1)).place(x=90,y=600,w=300,h=300)

btn2=Button(t,bg='black',bd=8,command=lambda : press(2)).place(x=410,y=600,w=300,h=300)
btn3=Button(t,bg='black',bd=8,command=lambda : press(3)).place(x=730,y=600,w=300,h=300)
btn4=Button(t,bg='black',bd=8,command=lambda : press(4)).place(x=90,y=920,w=300,h=300)
btn5=Button(t,bg='black',bd=8,command=lambda : press(5)).place(x=410,y=920,w=300,h=300)
btn6=Button(t,bg='black',bd=8,command=lambda : press(6)).place(x=730,y=920,w=300,h=300)
btn7=Button(t,bg='black',bd=8,command=lambda : press(7)).place(x=90,y=1240,w=300,h=300)
btn8=Button(t,bg='black',bd=8,command=lambda : press(8)).place(x=410,y=1240,w=300,h=300)
btn9=Button(t,bg='black',bd=8,command=lambda : press(9)).place(x=730,y=1240,w=300,h=300)
if count % 2 != 0:
    l=Label(t,text="X's Turn",bg='white',fg='navy',font=( 'icourier',40,'bold')).place(x=100,y=300,w=900,h=200)

   
#t.destroy()
t.mainloop()