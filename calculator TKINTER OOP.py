#april 19th 6:34pm 2 numbers only dont rush LEEMINZW
from tkinter import *

class numbers:
#number buttons in grid system
#will be displayed on the "entry" when pressed

    def __init__(self,number,row,col,which_calculator):
        self.number = number
        self.row = row
        self.col = col
        self.w_c = which_calculator
        self.thenum = Button(self.w_c.master,text=self.number,\
                        command = self.enterit)
        self.thenum.grid(row=self.row,column=self.col)
        
    def enterit(self):
        nxtnum = len(self.w_c.equation.get())
        self.w_c.equation.insert(nxtnum,self.number)
        

class operations:
#to add any new operations, creates new button
#automates the storing pf "f1"(first integer)
#to perform the operation chosen with "f2"(second integer)
    def __init__(self,operations,row,col,which_calculator):
        self.operations = operations
        self.row = row
        self.col = col
        self.w_c = which_calculator
        

        theopr = Button(self.w_c.master,text=self.operations,\
                    command = self.takein )
        
        theopr.grid(row=self.row,column=self.col)
        
    #will store the number b4 and operate with second by using equal
    def takein(self):
        self.w_c.f1 = self.w_c.equation.get()
        self.w_c.equation.delete(0,END)
        self.w_c.oper = self.operations
        
  

   
class calculator:
#inserts the operations and numbers
#has delete, clear, equal

    def __init__(self,master):
        self.master = master
        self.equation = Entry(self.master)
        self.equation.grid(row=0, column =0, columnspan = 30)
        self.f1 = 0
        self.f2 = 0
        self.oper = ''
        one=numbers(1,1,0,self)
        two=numbers(2,1,1,self)
        three=numbers(3,1,2,self)
        four=numbers(4,2,0,self)
        five=numbers(5,2,1,self)
        six=numbers(6,2,2,self)
        seven=numbers(7,3,0,self)
        eight=numbers(8,3,1,self)
        nine=numbers(9,3,2,self)
        zero=numbers(0,4,1,self)
        add=operations("+",1,4,self)
        sub=operations("-",2,4,self)
        mul=operations("x",1,5,self)
        div=operations("/",2,5,self)
        
        equal =Button(self.master,text='=',\
                    command = self.equal )
        
        delete =Button(self.master,text='DEL',\
                    command = self.DEL )
        
        clear =Button(self.master,text='CE',\
                    command = self.clear )
        equal.grid(row=3,column=4)
        clear.grid(row=4,column=4)
        delete.grid(row=3,column=5)
        
    #judges what operation to use based on inputs
    def equal(self):
        self.f2 = self.equation.get()
        result = "ERROR"
        
        if self.oper == '+': 
            result = int(self.f1) + int(self.f2) 
        elif self.oper == "-":
            result = int(self.f1) - int(self.f2)
        elif self.oper == "x":
            result = int(self.f1) * int(self.f2)
        elif self.oper == "/":
            result = int(self.f1) / int(self.f2)
        
        self.equation.delete(0,END)    
        self.equation.insert(0,result)
        
    #deletes the last digit
    def DEL(self):
        deleted = self.equation.delete(len(self.equation.get())-1)    
        
    #clears any presaved integers/operations
    def clear(self):
        self.equation.delete(0,END)
        self.f1 = 0
        self.f2 = 0
        self.oper = ''    
        
root = Tk()
root.geometry("300x500")
a = calculator(root)

root.mainloop()
