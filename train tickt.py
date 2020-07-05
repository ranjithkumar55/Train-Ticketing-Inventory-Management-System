
from tkinter import*
from tkinter import ttk,StringVar,Tk,messagebox
import random
import time;

tk=Tk()
tk.geometry('1350x750+0+0')
tk.title("Train Ticket")
tk.configure(background='black')

Top=Frame(tk,width=1350,height=100,bd=14,relief="raise")
Top.pack(side=TOP)
f1=Frame(tk,width=900,height=650,bd=8,relief='raise')
f1.pack(side=LEFT)
f2=Frame(tk,width=440,height=650,bd=8,relief="raise")
f2.pack(side=RIGHT)

frtopright=Frame(f2,width=440,height=650,bd=12,relief='raise')
frtopright.pack(side=TOP)
frbottomright=Frame(f2,width=440,height=50,bd=16,relief='raise')
frbottomright.pack(side=BOTTOM)

f1a=Frame(f1,width=900,height=320,bd=8,relief='raise')
f1a.pack(side=TOP)
f2a=Frame(f1,width=900,height=330,bd=6,relief='raise')
f2a.pack(side=BOTTOM)
topleft1=Frame(f1a,width=300,height=200,bd=16,relief='raise')
topleft1.pack(side=LEFT)
topleft2=Frame(f1a,width=300,height=200,bd=16,relief='raise')
topleft2.pack(side=RIGHT)
topleft3=Frame(f1a,width=300,height=200,bd=12,relief='raise')
topleft3.pack(side=RIGHT)


bottomleft1=Frame(f2a,width=450,height=450,bd=14,relief='raise')
bottomleft1.pack(side=LEFT)
bottomleft2=Frame(f2a,width=450,height=450,bd=14,relief='raise')
bottomleft2.pack(side=RIGHT)


f1.configure(background='black')
f2.configure(background='black')
Top.configure(background='black')
#=============================variables============================================
    
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=StringVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=StringVar()
var10=IntVar()
var11=StringVar()
var12=StringVar()
var13=StringVar()
var14=StringVar()
var15=StringVar()
var16=StringVar()
var17=StringVar()
var18=StringVar()
var19=StringVar()
var20=StringVar()
statetax=StringVar()
date1=StringVar()
time1=StringVar()
subtotal=StringVar()
total=StringVar()
var1.set('0')
var2.set('0')
var3.set('0')
var4.set('0')
var5.set('0')
var6.set('0')
var7.set('0')
var8.set('0')
var9.set('0')
var10.set('0')
var11.set('0')
statetax.set('0')
subtotal.set('0')
total.set('0')
var12.set("")
var13.set("")
var14.set("")
var15.set("")
var16.set("")
var17.set("")
var18.set("")
var19.set("")
var20.set("")

operator=""





date1.set(time.strftime("%d/%m/%y"))
time1.set(time.strftime("%H:%M:%S"))

l1=Label(Top,text="Train Tickting System",font=('arial',40,'bold'),width=41,justify='center')
l1.grid(column=0,row=0)
labspace=Label(frtopright,font=('arial',12,'bold'),justify='center',width=34
               ,height=2)
labspace.grid(column=0,row=1,columnspan=4)

labtra=Label(frtopright,text='Traveling Tickting System',font=('arial',14,'bold'),width=32,
    bd=10,justify='center')
labtra.grid(column=0,row=0)

labclass=Label(frbottomright,text='Class',font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labclass.grid(column=0,row=0)

labclass1=Label(frbottomright,textvariable=var12,font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labclass1.grid(column=0,row=1)
labticket=Label(frbottomright,text='Ticket',font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labticket.grid(column=1,row=0)

labticket1=Label(frbottomright,textvariable=var13,font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labticket1.grid(column=1,row=1)

labadult=Label(frbottomright,text='Adult',font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labadult.grid(column=2,row=0)

labadult1=Label(frbottomright,textvariable=var14,font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labadult1.grid(column=2,row=1)

labchild=Label(frbottomright,text='Child',font=('arial',12,'bold'),width=8,
    relief='sunken',justify='center')
labchild.grid(column=3,row=0)

labchild1=Label(frbottomright,textvariable=var15,font=('arial',12,'bold'),width=8,
    relief='sunken',justify='center')
labchild1.grid(column=3,row=1)
labspace=Label(frbottomright,font=('arial',12,'bold'),justify='center',width=36
               ,height=1)
labspace.grid(column=0,row=2,columnspan=4)

labfrom=Label(frbottomright,text='From',font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labfrom.grid(column=1,row=3)

labfrom1=Label(frbottomright,textvariable=var16,font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labfrom1.grid(column=2,row=3)
labto=Label(frbottomright,text='To',font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labto.grid(column=1,row=4)

labto1=Label(frbottomright,textvariable=var17,font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labto1.grid(column=2,row=4)

labprice=Label(frbottomright,text='Price',font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labprice.grid(column=1,row=5)

labprice1=Label(frbottomright,textvariable=var18,font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labprice1.grid(column=2,row=5)
labspace=Label(frbottomright,font=('arial',12,'bold'),justify='center',width=34
               ,height=1)
labspace.grid(column=0,row=6,columnspan=4)

labref=Label(frbottomright,text='Ref no',font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labref.grid(column=0,row=7)

labref1=Label(frbottomright,textvariable=var19,font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labref1.grid(column=0,row=8)
labtime=Label(frbottomright,text='Time',font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labtime.grid(column=1,row=7)

labtime1=Label(frbottomright,text='',font=('arial',14,'bold'),width=8,textvariable=time1,
    relief='sunken',justify='center')
labtime1.grid(column=1,row=8)

labdate=Label(frbottomright,text='Date',font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center')
labdate.grid(column=2,row=7)

labdate1=Label(frbottomright,text='',font=('arial',14,'bold'),width=8,
    relief='sunken',justify='center',textvariable=date1)
labdate1.grid(column=2,row=8)

labroute=Label(frbottomright,text='Route',font=('arial',12,'bold'),width=8,
    relief='sunken',justify='center')
labroute.grid(column=3,row=7)

labroute1=Label(frbottomright,font=('arial',12,'bold'),width=8,textvariable=var20,
    relief='sunken',justify='center')
labroute1.grid(column=3,row=8)
labspace=Label(frbottomright,font=('arial',12,'bold'),justify='center',width=36
               ,height=1)
labspace.grid(column=0,row=9,columnspan=4)


#=================================functions==================================

def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)

def btnclearDisplay():
    global operator
    operator=""
    text_input.set("")
    
def btnequals():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

def iExit():
    qExit=messagebox.askyesno("Quite System","Do you want to quit?")
    if qExit> 0:
        tk.destroy()
        return
        
        
                            
    
   

def Total_Cost():
    date1.set(time.strftime("%d/%m/%y"))
    time1.set(time.strftime("%H:%M:%S"))
    if(var4.get()=='Covai' and var1.get()==1 and var5.get()==1):
        Tcost=float(80.0)                
        single=float(var8.get())
        returntype=float(var9.get())
        adult_tax="Rs.",str("%.2f"%((((Tcost*returntype)*0.03)*2)+((Tcost*single)*0.03)))
        adult_fees="Rs." ,str("%.2f" %(((Tcost*returntype)*2)+(Tcost*single)))
        adult_total="Rs." ,str("%.2f" %((((Tcost*returntype)*2)+(((Tcost*returntype)
                                        *0.03)*2))+((Tcost*single)+((Tcost*single)*0.03))))
        statetax.set(adult_tax)
        subtotal.set(adult_fees)
        total.set(adult_total)
        var12.set("standard")
        var13.set(adult_fees)
        var14.set("No")
        var15.set("Yes")
        var16.set("Salem")
        var17.set("Covai")
        var18.set(adult_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)
        
    elif(var4.get()=='Covai' and var1.get()==1 and var6.get()==1):
        Tcost=float(42.0)                
        single=float(var8.get())
        returntype=float(var9.get())
        child_tax="Rs.",str("%.2f"%(Tcost*0))
        child_fees="Rs." ,str("%.2f" %((Tcost*single)+(Tcost*returntype)*2))
        child_total="Rs." ,str("%.2f" %(((Tcost*single)+(Tcost*0))+
                                        ((Tcost*single)+(Tcost*returntype)*2)))
        statetax.set(child_tax)
        subtotal.set(child_fees)
        total.set(child_total)
        var12.set("standard")
        var13.set(child_fees)
        var14.set("No")
        var15.set("Yes")
        var16.set("Salem")
        var17.set("Covai")
        var18.set(child_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)

    if(var4.get()=='Chennai' and var1.get()==1 and var5.get()==1):
        Tcost=float(92.0)                
        single=float(var8.get())
        returntype=float(var9.get())
        adult_tax="Rs.",str("%.2f"%((((Tcost*returntype)*0.03)*2)+((Tcost*single)*0.03)))
        adult_fees="Rs." ,str("%.2f" %(((Tcost*returntype)*2)+(Tcost*single)))
        adult_total="Rs." ,str("%.2f" %((((Tcost*returntype)*2)+(((Tcost*returntype)
                                        *0.03)*2))+((Tcost*single)+((Tcost*single)*0.03))))
        statetax.set(adult_tax)
        subtotal.set(adult_fees)
        total.set(adult_total)
        var12.set("standard")
        var13.set(adult_fees)
        var14.set("yes")
        var15.set("No")
        var16.set("Salem")
        var17.set("Chennai")
        var18.set(adult_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)
        
    elif(var4.get()=='Chennai' and var1.get()==1 and var6.get()==1):
        Tcost=float(42.0)                
        single=float(var8.get())
        returntype=float(var9.get())
        child_tax="Rs.",str("%.2f"%(Tcost*0))
        child_fees="Rs." ,str("%.2f" %((Tcost*single)+(Tcost*returntype)*2))
        child_total="Rs." ,str("%.2f" %(((Tcost*single)+(Tcost*0))+
                                        ((Tcost*single)+(Tcost*returntype)*2)))
        statetax.set(child_tax)
        subtotal.set(child_fees)
        total.set(child_total)
        var12.set("standard")
        var13.set(child_fees)
        var14.set("No")
        var15.set("Yes")
        var16.set("Salem")
        var17.set("Chennai")
        var18.set(child_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)

    if(var4.get()=='Madurai' and var1.get()==1 and var5.get()==1):
        Tcost=float(138.0)                
        single=float(var8.get())
        returntype=float(var9.get())
        adult_tax="Rs.",str("%.2f"%((((Tcost*returntype)*0.03)*2)+((Tcost*single)*0.03)))
        adult_fees="Rs." ,str("%.2f" %(((Tcost*returntype)*2)+(Tcost*single)))
        adult_total="Rs." ,str("%.2f" %((((Tcost*returntype)*2)+(((Tcost*returntype)
                                        *0.03)*2))+((Tcost*single)+((Tcost*single)*0.03))))
        statetax.set(adult_tax)
        subtotal.set(adult_fees)
        total.set(adult_total)
        var12.set("standard")
        var13.set(adult_fees)
        var14.set("yes")
        var15.set("No")
        var16.set("Salem")
        var17.set("Madurai")
        var18.set(adult_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)
        
    elif(var4.get()=='Madurai' and var1.get()==1 and var6.get()==1):
        Tcost=float(82.0)                
        single=float(var8.get())
        returntype=float(var9.get())
        child_tax="Rs.",str("%.2f"%(Tcost*0))
        child_fees="Rs." ,str("%.2f" %((Tcost*single)+(Tcost*returntype)*2))
        child_total="Rs." ,str("%.2f" %(((Tcost*single)+(Tcost*0))+
                                        ((Tcost*single)+(Tcost*returntype)*2)))
        statetax.set(child_tax)
        subtotal.set(child_fees)
        total.set(child_total)
        var12.set("standard")
        var13.set(child_fees)
        var14.set("No")
        var15.set("Yes")
        var16.set("Salem")
        var17.set("Madurai")
        var18.set(child_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)

    if(var4.get()=='Kerala' and var1.get()==1 and var5.get()==1):
        Tcost=float(108.0)                
        single=float(var8.get())
        returntype=float(var9.get())
        adult_tax="Rs.",str("%.2f"%((((Tcost*returntype)*0.03)*2)+((Tcost*single)*0.03)))
        adult_fees="Rs." ,str("%.2f" %(((Tcost*returntype)*2)+(Tcost*single)))
        adult_total="Rs." ,str("%.2f" %((((Tcost*returntype)*2)+(((Tcost*returntype)
                                        *0.03)*2))+((Tcost*single)+((Tcost*single)*0.03))))
        statetax.set(adult_tax)
        subtotal.set(adult_fees)
        total.set(adult_total)
        var12.set("standard")
        var13.set(adult_fees)
        var14.set("yes")
        var15.set("No")
        var16.set("Salem")
        var17.set("Kerala")
        var18.set(adult_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)
        
    elif(var4.get()=='Kerala' and var1.get()==1 and var6.get()==1):
        Tcost=float(72.0)                
        single=float(var8.get())
        returntype=float(var9.get())
        child_tax="Rs.",str("%.2f"%(Tcost*0))
        child_fees="Rs." ,str("%.2f" %((Tcost*single)+(Tcost*returntype)*2))
        child_total="Rs." ,str("%.2f" %(((Tcost*single)+(Tcost*0))+
                                        ((Tcost*single)+(Tcost*returntype)*2)))
        statetax.set(child_tax)
        subtotal.set(child_fees)
        total.set(child_total)
        var12.set("standard")
        var13.set(child_fees)
        var14.set("No")
        var15.set("Yes")
        var16.set("Salem")
        var17.set("Kerala")
        var18.set(child_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)


    if(var4.get()=='Covai' and var2.get()==1 and var5.get()==1):
        Tcost=float(88.9)                
        single=float(var8.get())
        returntype=float(var9.get())
        adult_tax="Rs.",str("%.2f"%((((Tcost*returntype)*0.03)*2)+((Tcost*single)*0.03)))
        adult_fees="Rs." ,str("%.2f" %(((Tcost*returntype)*2)+(Tcost*single)))
        adult_total="Rs." ,str("%.2f" %((((Tcost*returntype)*2)+(((Tcost*returntype)
                                        *0.03)*2))+((Tcost*single)+((Tcost*single)*0.03))))
        statetax.set(adult_tax)
        subtotal.set(adult_fees)
        total.set(adult_total)
        var12.set("Economy")
        var13.set(adult_fees)
        var14.set("No")
        var15.set("Yes")
        var16.set("Salem")
        var17.set("Covai")
        var18.set(adult_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)
        
    elif(var4.get()=='Covai' and var2.get()==1 and var6.get()==1):
        Tcost=float(48.7)                
        single=float(var8.get())
        returntype=float(var9.get())
        child_tax="Rs.",str("%.2f"%(Tcost*0))
        child_fees="Rs." ,str("%.2f" %((Tcost*single)+(Tcost*returntype)*2))
        child_total="Rs." ,str("%.2f" %(((Tcost*single)+(Tcost*0))+
                                        ((Tcost*single)+(Tcost*returntype)*2)))
        statetax.set(child_tax)
        subtotal.set(child_fees)
        total.set(child_total)
        var12.set("Economy")
        var13.set(child_fees)
        var14.set("No")
        var15.set("Yes")
        var16.set("Salem")
        var17.set("Covai")
        var18.set(child_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)

    if(var4.get()=='Chennai' and var2.get()==1 and var5.get()==1):
        Tcost=float(102.0)                
        single=float(var8.get())
        returntype=float(var9.get())
        adult_tax="Rs.",str("%.2f"%((((Tcost*returntype)*0.03)*2)+((Tcost*single)*0.03)))
        adult_fees="Rs." ,str("%.2f" %(((Tcost*returntype)*2)+(Tcost*single)))
        adult_total="Rs." ,str("%.2f" %((((Tcost*returntype)*2)+(((Tcost*returntype)
                                        *0.03)*2))+((Tcost*single)+((Tcost*single)*0.03))))
        statetax.set(adult_tax)
        subtotal.set(adult_fees)
        total.set(adult_total)
        var12.set("Economy")
        var13.set(adult_fees)
        var14.set("yes")
        var15.set("No")
        var16.set("Salem")
        var17.set("Chennai")
        var18.set(adult_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)
        
    elif(var4.get()=='Chennai' and var2.get()==1 and var6.get()==1):
        Tcost=float(57.3)                
        single=float(var8.get())
        returntype=float(var9.get())
        child_tax="Rs.",str("%.2f"%(Tcost*0))
        child_fees="Rs." ,str("%.2f" %((Tcost*single)+(Tcost*returntype)*2))
        child_total="Rs." ,str("%.2f" %(((Tcost*single)+(Tcost*0))+
                                        ((Tcost*single)+(Tcost*returntype)*2)))
        statetax.set(child_tax)
        subtotal.set(child_fees)
        total.set(child_total)
        var12.set("Economy")
        var13.set(child_fees)
        var14.set("No")
        var15.set("Yes")
        var16.set("Salem")
        var17.set("Chennai")
        var18.set(child_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)

    if(var4.get()=='Madurai' and var2.get()==1 and var5.get()==1):
        Tcost=float(147.7)                
        single=float(var8.get())
        returntype=float(var9.get())
        adult_tax="Rs.",str("%.2f"%((((Tcost*returntype)*0.03)*2)+((Tcost*single)*0.03)))
        adult_fees="Rs." ,str("%.2f" %(((Tcost*returntype)*2)+(Tcost*single)))
        adult_total="Rs." ,str("%.2f" %((((Tcost*returntype)*2)+(((Tcost*returntype)
                                        *0.03)*2))+((Tcost*single)+((Tcost*single)*0.03))))
        statetax.set(adult_tax)
        subtotal.set(adult_fees)
        total.set(adult_total)
        var12.set("Economy")
        var13.set(adult_fees)
        var14.set("yes")
        var15.set("No")
        var16.set("Salem")
        var17.set("Madurai")
        var18.set(adult_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)
        
    elif(var4.get()=='Madurai' and var2.get()==1 and var6.get()==1):
        Tcost=float(87.6)                
        single=float(var8.get())
        returntype=float(var9.get())
        child_tax="Rs.",str("%.2f"%(Tcost*0))
        child_fees="Rs." ,str("%.2f" %((Tcost*single)+(Tcost*returntype)*2))
        child_total="Rs." ,str("%.2f" %(((Tcost*single)+(Tcost*0))+
                                        ((Tcost*single)+(Tcost*returntype)*2)))
        statetax.set(child_tax)
        subtotal.set(child_fees)
        total.set(child_total)
        var12.set("Economy")
        var13.set(child_fees)
        var14.set("No")
        var15.set("Yes")
        var16.set("Salem")
        var17.set("Madurai")
        var18.set(child_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)

    if(var4.get()=='Kerala' and var2.get()==1 and var5.get()==1):
        Tcost=float(121.5)                
        single=float(var8.get())
        returntype=float(var9.get())
        adult_tax="Rs.",str("%.2f"%((((Tcost*returntype)*0.03)*2)+((Tcost*single)*0.03)))
        adult_fees="Rs." ,str("%.2f" %(((Tcost*returntype)*2)+(Tcost*single)))
        adult_total="Rs." ,str("%.2f" %((((Tcost*returntype)*2)+(((Tcost*returntype)
                                        *0.03)*2))+((Tcost*single)+((Tcost*single)*0.03))))
        statetax.set(adult_tax)
        subtotal.set(adult_fees)
        total.set(adult_total)
        var12.set("Economy")
        var13.set(adult_fees)
        var14.set("yes")
        var15.set("No")
        var16.set("Salem")
        var17.set("Kerala")
        var18.set(adult_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)
        
    elif(var4.get()=='Kerala' and var2.get()==1 and var6.get()==1):
        Tcost=float(79.7)                
        single=float(var8.get())
        returntype=float(var9.get())
        child_tax="Rs.",str("%.2f"%(Tcost*0))
        child_fees="Rs." ,str("%.2f" %((Tcost*single)+(Tcost*returntype)*2))
        child_total="Rs." ,str("%.2f" %(((Tcost*single)+(Tcost*0))+
                                        ((Tcost*single)+(Tcost*returntype)*2)))
        statetax.set(child_tax)
        subtotal.set(child_fees)
        total.set(child_total)
        var12.set("Economy")
        var13.set(child_fees)
        var14.set("No")
        var15.set("Yes")
        var16.set("Salem")
        var17.set("Kerala")
        var18.set(child_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)

    if(var4.get()=='Covai' and var3.get()==1 and var5.get()==1):
        Tcost=float(96.9)                
        single=float(var8.get())
        returntype=float(var9.get())
        adult_tax="Rs.",str("%.2f"%((((Tcost*returntype)*0.03)*2)+((Tcost*single)*0.03)))
        adult_fees="Rs." ,str("%.2f" %(((Tcost*returntype)*2)+(Tcost*single)))
        adult_total="Rs." ,str("%.2f" %((((Tcost*returntype)*2)+(((Tcost*returntype)
                                        *0.03)*2))+((Tcost*single)+((Tcost*single)*0.03))))
        statetax.set(adult_tax)
        subtotal.set(adult_fees)
        total.set(adult_total)
        var12.set("FirstClass")
        var13.set(adult_fees)
        var14.set("No")
        var15.set("Yes")
        var16.set("Salem")
        var17.set("Covai")
        var18.set(adult_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)
        
    elif(var4.get()=='Covai' and var3.get()==1 and var6.get()==1):
        Tcost=float(56.7)                
        single=float(var8.get())
        returntype=float(var9.get())
        child_tax="Rs.",str("%.2f"%(Tcost*0))
        child_fees="Rs." ,str("%.2f" %((Tcost*single)+(Tcost*returntype)*2))
        child_total="Rs." ,str("%.2f" %(((Tcost*single)+(Tcost*0))+
                                        ((Tcost*single)+(Tcost*returntype)*2)))
        statetax.set(child_tax)
        subtotal.set(child_fees)
        total.set(child_total)
        var12.set("FirstClass")
        var13.set(child_fees)
        var14.set("No")
        var15.set("Yes")
        var16.set("Salem")
        var17.set("Covai")
        var18.set(child_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)

    if(var4.get()=='Chennai' and var3.get()==1 and var5.get()==1):
        Tcost=float(116.0)                
        single=float(var8.get())
        returntype=float(var9.get())
        adult_tax="Rs.",str("%.2f"%((((Tcost*returntype)*0.03)*2)+((Tcost*single)*0.03)))
        adult_fees="Rs." ,str("%.2f" %(((Tcost*returntype)*2)+(Tcost*single)))
        adult_total="Rs." ,str("%.2f" %((((Tcost*returntype)*2)+(((Tcost*returntype)
                                        *0.03)*2))+((Tcost*single)+((Tcost*single)*0.03))))
        statetax.set(adult_tax)
        subtotal.set(adult_fees)
        total.set(adult_total)
        var12.set("FirstClass")
        var13.set(adult_fees)
        var14.set("yes")
        var15.set("No")
        var16.set("Salem")
        var17.set("Chennai")
        var18.set(adult_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)
        
    elif(var4.get()=='Chennai' and var3.get()==1 and var6.get()==1):
        Tcost=float(67.3)                
        single=float(var8.get())
        returntype=float(var9.get())
        child_tax="Rs.",str("%.2f"%(Tcost*0))
        child_fees="Rs." ,str("%.2f" %((Tcost*single)+(Tcost*returntype)*2))
        child_total="Rs." ,str("%.2f" %(((Tcost*single)+(Tcost*0))+
                                        ((Tcost*single)+(Tcost*returntype)*2)))
        statetax.set(child_tax)
        subtotal.set(child_fees)
        total.set(child_total)
        var12.set("FirstClass")
        var13.set(child_fees)
        var14.set("No")
        var15.set("Yes")
        var16.set("Salem")
        var17.set("Chennai")
        var18.set(child_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)

    if(var4.get()=='Madurai' and var3.get()==1 and var5.get()==1):
        Tcost=float(156.7)                
        single=float(var8.get())
        returntype=float(var9.get())
        adult_tax="Rs.",str("%.2f"%((((Tcost*returntype)*0.03)*2)+((Tcost*single)*0.03)))
        adult_fees="Rs." ,str("%.2f" %(((Tcost*returntype)*2)+(Tcost*single)))
        adult_total="Rs." ,str("%.2f" %((((Tcost*returntype)*2)+(((Tcost*returntype)
                                        *0.03)*2))+((Tcost*single)+((Tcost*single)*0.03))))
        statetax.set(adult_tax)
        subtotal.set(adult_fees)
        total.set(adult_total)
        var12.set("FirstClass")
        var13.set(adult_fees)
        var14.set("yes")
        var15.set("No")
        var16.set("Salem")
        var17.set("Madurai")
        var18.set(adult_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)
        
    elif(var4.get()=='Madurai' and var3.get()==1 and var6.get()==1):
        Tcost=float(97.6)                
        single=float(var8.get())
        returntype=float(var9.get())
        child_tax="Rs.",str("%.2f"%(Tcost*0))
        child_fees="Rs." ,str("%.2f" %((Tcost*single)+(Tcost*returntype)*2))
        child_total="Rs." ,str("%.2f" %(((Tcost*single)+(Tcost*0))+
                                        ((Tcost*single)+(Tcost*returntype)*2)))
        statetax.set(child_tax)
        subtotal.set(child_fees)
        total.set(child_total)
        var12.set("FirstClass")
        var13.set(child_fees)
        var14.set("No")
        var15.set("Yes")
        var16.set("Salem")
        var17.set("Madurai")
        var18.set(child_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)

    if(var4.get()=='Kerala' and var3.get()==1 and var5.get()==1):
        Tcost=float(129.5)                
        single=float(var8.get())
        returntype=float(var9.get())
        adult_tax="Rs.",str("%.2f"%((((Tcost*returntype)*0.03)*2)+((Tcost*single)*0.03)))
        adult_fees="Rs." ,str("%.2f" %(((Tcost*returntype)*2)+(Tcost*single)))
        adult_total="Rs." ,str("%.2f" %((((Tcost*returntype)*2)+(((Tcost*returntype)
                                        *0.03)*2))+((Tcost*single)+((Tcost*single)*0.03))))
        statetax.set(adult_tax)
        subtotal.set(adult_fees)
        total.set(adult_total)
        var12.set("FirstClass")
        var13.set(adult_fees)
        var14.set("yes")
        var15.set("No")
        var16.set("Salem")
        var17.set("Kerala")
        var18.set(adult_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)
        
    elif(var4.get()=='Kerala' and var3.get()==1 and var6.get()==1):
        Tcost=float(87.7)                
        single=float(var8.get())
        returntype=float(var9.get())
        child_tax="Rs.",str("%.2f"%(Tcost*0))
        child_fees="Rs." ,str("%.2f" %((Tcost*single)+(Tcost*returntype)*2))
        child_total="Rs." ,str("%.2f" %(((Tcost*single)+(Tcost*0))+
                                        ((Tcost*single)+(Tcost*returntype)*2)))
        statetax.set(child_tax)
        subtotal.set(child_fees)
        total.set(child_total)
        var12.set("FirstClass")
        var13.set(child_fees)
        var14.set("No")
        var15.set("Yes")
        var16.set("Salem")
        var17.set("Kerala")
        var18.set(child_total)
        var20.set("Direct")
        x=random.randint(136,1539)
        randomref=str(x)
        var19.set("TFL" + randomref)

        

def CheckButtonValue():
    if(var7.get()==1):
        var8.set('')
        ensingle.configure(state=NORMAL)
    elif(var7.get()==0):
        ensingle.configure(state=DISABLED)
        var8.set("0")                
    if(var10.get()==1):
        var9.set("")
        enreturntype.configure(state=NORMAL)                
    elif(var10.get()==0):
        enreturntype.configure(state=DISABLED)                        
        var9.set("0")                
        
        

def reset():
    var1.set('0')
    var2.set('0')
    var3.set('0')
    var4.set('0')
    var5.set('0')
    var6.set('0')
    var7.set('0')
    var8.set('0')
    var9.set('0')
    var10.set('0')
    var11.set('0')
    var12.set("")
    var13.set("")
    var14.set("")
    var15.set("")
    var16.set("")
    var17.set("")
    var18.set("")
    var19.set("")
    var20.set("")
    date1.set('0')
    time1.set('0')
    statetax.set('0')
    subtotal.set('0')
    total.set('0')
    
    
    





#==============================================================================



label1=Label(topleft1,text='Class',font=('arial',22,'bold'),bd=8)
label1.grid(column=0,row=0,sticky=W)
chkstandard=Checkbutton(topleft1,text='Standard',font=('arial',20,'bold'),variable=var1,onvalue=1,offvalue=0)
chkstandard.grid(column=0,row=1,sticky=W)
chkeconomy=Checkbutton(topleft1,text='economy',font=('arial',20,'bold'),variable=var2,onvalue=1,offvalue=0)
chkeconomy.grid(column=0,row=2,sticky=W)
chkFirstclass=Checkbutton(topleft1,text='FirstClass',font=('arial',20,'bold'),variable=var3,onvalue=1,offvalue=0)
chkFirstclass.grid(column=0,row=3,sticky=W)

lbldestination=Label(topleft3,text='Destination Selector',font=('arial',22,'bold'),bd=8)
lbldestination.grid(column=0,row=0,sticky=W,columnspan=2)

lbldestination=Label(topleft3,text='Destination',font=('arial',20,'bold'),bd=8)
lbldestination.grid(column=0,row=1,sticky=W)

cbodestination=ttk.Combobox(topleft3,textvariable=var4,font=('arial',20,'bold'),width=8,)
cbodestination["values"]=('','Covai','Chennai','Madurai','Kerala')
cbodestination.current(0)
cbodestination.grid(column=1,row=1)

chkadult=Checkbutton(topleft3,text='Adult',font=('arial',20,'bold'),variable=var5,onvalue=1,offvalue=0)
chkadult.grid(column=0,row=2,sticky=W)
chkchild=Checkbutton(topleft3,text='Child',font=('arial',20,'bold'),variable=var6,onvalue=1,offvalue=0)
chkchild.grid(column=0,row=3,sticky=W)
#=============================ticket==================================
label1=Label(topleft2,text='Ticket Type',font=('arial',22,'bold'),bd=8)
label1.grid(column=0,row=0,sticky=W)
chksingle=Checkbutton(topleft2,text='single',font=('arial',20,'bold')
                      ,variable=var7,onvalue=1,offvalue=0,command=CheckButtonValue)
chksingle.grid(column=0,row=1,sticky=W)

ensingle=Entry(topleft2,width=8,bd=2,textvariable=var8,font=('arial',20,'bold'),state=DISABLED)
ensingle.grid(column=1,row=1)

enreturntype=Entry(topleft2,width=8,bd=2,textvariable=var9,font=('arial',20,'bold'),state=DISABLED)
enreturntype.grid(column=1,row=2)

chkreturntype=Checkbutton(topleft2,text='Returntype',font=('arial',20,'bold')
                          ,variable=var10,onvalue=1,offvalue=0,command=CheckButtonValue)
chkreturntype.grid(column=0,row=2,sticky=W)

labelcommit=Label(topleft2,text='Comment',font=('arial',20,'bold'))
labelcommit.grid(column=0,row=3,sticky=W)
encommit=Entry(topleft2,width=8,bd=2,textvariable=var11,font=('arial',20,'bold'))
encommit.grid(column=1,row=3)

#=============================calculator==================================

text_input=StringVar()



textdiplay=Entry(bottomleft2,font=("arial",16,"bold"),textvariable=text_input,bd=8,justify="right").grid(columnspan=4)

btn7=Button(bottomleft2,text="7",command=lambda:btnclick(7),padx=8,pady=20,bd=8,font=("arial",10,"bold"),fg="black",width=4).grid(row=2,column=0)
btn8=Button(bottomleft2,text="8",command=lambda:btnclick(8),padx=8,pady=20,bd=8,font=("arial",10,"bold"),width=4).grid(row=2,column=1)
btn9=Button(bottomleft2,text="9",command=lambda:btnclick(9),padx=8,pady=20,bd=8,font=("arial",10,"bold"),width=4).grid(row=2,column=2)
btnadd=Button(bottomleft2,text="+",command=lambda:btnclick('+'),padx=8,pady=20,bd=8,font=("arial",10,"bold"),width=4).grid(row=2,column=3)


btn4=Button(bottomleft2,text="4",command=lambda:btnclick(4),padx=8,pady=20,bd=8,font=("arial",10,"bold"),width=4).grid(row=3,column=0)
btn5=Button(bottomleft2,text="5",command=lambda:btnclick(5),padx=8,pady=20,bd=8,font=("arial",10,"bold"),width=4).grid(row=3,column=1)
btn6=Button(bottomleft2,text="6",command=lambda:btnclick(6),padx=8,pady=20,bd=8,font=("arial",10,"bold"),width=4).grid(row=3,column=2)
btnsub=Button(bottomleft2,text="-",command=lambda:btnclick('-'),padx=8,pady=20,bd=8,font=("arial",10,"bold"),width=4).grid(row=3,column=3)


btn1=Button(bottomleft2,text="1",command=lambda:btnclick(1),padx=8,pady=20,bd=8,font=("arial",10,"bold"),width=4).grid(row=4,column=0)
btn2=Button(bottomleft2,text="2",command=lambda:btnclick(2),padx=8,pady=20,bd=8,font=("arial",10,"bold"),width=4).grid(row=4,column=1)
btn3=Button(bottomleft2,text="3",command=lambda:btnclick(3),padx=8,pady=20,bd=8,font=("arial",10,"bold"),width=4).grid(row=4,column=2)
btnmul=Button(bottomleft2,text="*",command=lambda:btnclick('*'),padx=8,pady=20,bd=8,font=("arial",10,"bold"),width=4).grid(row=4,column=3)




btn0=Button(bottomleft2,text="0",command=lambda:btnclick(0),padx=8,pady=20,bd=8,font=("arial",10,"bold"),width=4).grid(row=5,column=0)
btnclear=Button(bottomleft2,text="c",command=btnclearDisplay,padx=8,pady=20,bd=8,font=("arial",10,"bold"),width=4).grid(row=5,column=1)
btnequals=Button(bottomleft2,text="=",command=btnequals,padx=8,pady=20,bd=8,font=("arial",10,"bold"),width=4).grid(row=5,column=2)
btndiv=Button(bottomleft2,text="/",command=lambda:btnclick('/'),padx=8,pady=20,bd=8,font=("arial",10,"bold"),width=4).grid(row=5,column=3)
#=======================widgets=============================================
labstatetax=Label(bottomleft1,text='State Tax',font=('arial',24,'bold'),anchor='w',bd=16)
labstatetax.grid(column=2,row=3)
enstatetax=Entry(bottomleft1,textvariable=statetax,bd=10,insertwidth=4,bg=('#ffffff'),width=28,font=('arial',16,'bold'),justify='right')
enstatetax.grid(column=3,row=3)

labsubtotal=Label(bottomleft1,text='Sub Total',font=('arial',24,'bold'),anchor='w',bd=16)
labsubtotal.grid(column=2,row=4)
ensubtotal=Entry(bottomleft1,textvariable=subtotal,bd=10,insertwidth=4,bg=('#ffffff'),width=28,font=('arial',16,'bold'),justify='right')
ensubtotal.grid(column=3,row=4)

labtotalcost=Label(bottomleft1,text='Total Cost',font=('arial',24,'bold'),anchor='w',bd=16)
labtotalcost.grid(column=2,row=5)
entotalcost=Entry(bottomleft1,textvariable=total,bd=10,insertwidth=4,bg=('#ffffff'),width=28,font=('arial',16,'bold'),justify='right')
entotalcost.grid(column=3,row=5)
labtotalcost1=Label(bottomleft1,text='',font=('arial',24,'bold'),anchor='w',bd=16)
labtotalcost1.grid(column=2,row=6)

labtotalcost2=Label(bottomleft1,text='',font=('arial',24,'bold'),anchor='w',bd=16)
labtotalcost2.grid(column=2,row=7)






#==========================buttons==============================================

btnconvert=Button(frbottomright,text='Total',font=('arial',12,'bold')
                  ,width=8,
    justify='center',command=Total_Cost)
btnconvert.grid(column=0,row=10)


btnclear=Button(frbottomright,text='Clear',font=('arial',12,'bold'),width=8,
    justify='center',command=reset)
btnclear.grid(column=1,row=10)
btnreset=Button(frbottomright,text='Reset',font=('arial',12,'bold'),width=8,
    justify='center',command=reset)
btnreset.grid(column=2,row=10)
btnexit=Button(frbottomright,text='Exit',font=('arial',12,'bold'),width=8,
    justify='center',command=iExit)
btnexit.grid(column=3,row=10)

labreceipt=Label(frbottomright,text='Receipt:',font=('arial',14,'bold'),width=8,
    anchor='w')
labreceipt.grid(column=0,row=11,sticky=W)

textreceipt=Text(frbottomright,width=28,height=4,font=('arial',14,'bold'),bg='white'
    ,bd=8)
textreceipt.grid(column=0,row=12,columnspan=4)

labspace=Label(frbottomright,font=('arial',12,'bold'),justify='center',width=38
               ,height=2)
labspace.grid(column=0,row=13,columnspan=4)



tk.mainloop()
