from tkinter import *
import string
import random
import pyperclip
def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation
    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())
    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))
    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))
    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))
def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)
root=Tk()
root.config(bg='cyan')
choice=IntVar()
Font=('arial',13,'bold')
passwordLabel=Label(root,text='PASSWORD GENERATOR',font=('times new roman',20,'bold'),bg='cyan',fg='red')
passwordLabel.grid(pady=10)
name=Label(root,text="ENTER USER NAME:", font=('times new roman',20,'bold'),bg='cyan',fg='red')
name.grid(pady=10)
nameField=Entry(root,width=25,bd=2,font=Font)
nameField.grid()
weakradioButton=Radiobutton(root,text='WEAK',value=1,variable=choice,font=Font,fg='green')
weakradioButton.grid(pady=5)
mediumradioButton=Radiobutton(root,text='MEDIUM',value=2,variable=choice,font=Font,fg='green')
mediumradioButton.grid(pady=5)
strongradioButton=Radiobutton(root,text='STRONG',value=3,variable=choice,font=Font,fg='green')
strongradioButton.grid(pady=5)
lengthLabel=Label(root,text='PASSWORD LENGTH',font=Font,bg='cyan',fg='red')
lengthLabel.grid(pady=5)
length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font,fg='green')
length_Box.grid(pady=5)
generateButton=Button(root,text='GENERATE',font=Font,command=generator,fg='green')
generateButton.grid(pady=5)
passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid()
root.mainloop()
