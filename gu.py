from tkinter import *
class myentry:
    def _init_(self,root):
        self.f= Frame(root,height=350,width=500)
        self.f.propagate(0)
        self.f.pack()
        self.l1=Label(text="enter your user name:")
        self.l2=Label(text="enter password:")
        self.e1=Entry(self.f,width=25,fg="blue",bg="yellow",font=('arial',14))
        self.e2=Entry(self.f,width=25,fg="blue",bg="yellow",show="*")
        self.e2.blind("<return>",self.display)
        self.l1.place(x=50,y=100)
        self.e1.place(x=200,y=100)
        self.l1.place(x=50,y=150)
        self.e2.place(x=200,y=150)
        def display(self,event):
                    str1=self.e1.get()
                    str2=self.e2.get()
                    lbl1=Label(text="your name is:"+str1).place(x=50,y=200)
                    lbl2=Label(text="your password:"+str2).place(x=50,y=220)
                    root=Tk()
                    mb=myentry(root)
                    root.mainloop()