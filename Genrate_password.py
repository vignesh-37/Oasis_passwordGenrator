import os
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import random
import string

def random_password(length=12,uppercase=True,lowercase=True,digit=True,punctuation=True):                       
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    number = string.digits
    special_char = string.punctuation
   
    #the variable was ceeated of storing password requirements from the user
    requires = ''
    if uppercase:
        requires += upper
    if lowercase:
        requires += lower
    if digit:
        requires += number
    if punctuation:
        requires += special_char
    
    password = ''    #the variable stores the password of randomly genrated
    #at least one char in every selected category
    if uppercase:
        password += (random.choice(upper))
    if lowercase:
        password += (random.choice(lower))
    if digit:
        password += (random.choice(number))
    if punctuation:
        password += (random.choice(special_char))

    while len(password) < length:
        password += random.choice(requires)
        
    password.join("")
    #random.shuffle(password)   
    return password

#getting values from check boxes
def genrate():
    try:
        #get the values from user
        check_upper_value = check_upper.get()
        check_lower_value = check_lower.get()
        check_digit_value = check_digit.get()
        length_value = length.get()
        if length_value != '':
            length_value = int(length_value)
        else:
            length_value = 0 
        check_punctuation_value = check_punctuation.get()
    
        if length_value > 0 and check_upper_value == False and check_lower_value == False and check_digit_value == False and check_punctuation_value == False:
            password = random_password(length=length_value)
        
        elif check_upper_value == False and check_lower_value == False and check_digit_value == False and check_punctuation_value == False:
            password=random_password()
        
        elif length_value == 0 and (check_upper_value == True or check_lower_value == True or check_digit_value == True or check_punctuation_value == True):
            password = random_password(length=12,uppercase=check_upper_value,lowercase=check_lower_value,digit=check_digit_value,punctuation=check_punctuation_value)
        
        elif length_value > 0  and check_upper_value == True or check_lower_value == True or check_digit_value == True or check_punctuation_value == True:
            password = random_password(length=length_value,uppercase=check_upper_value,lowercase=check_lower_value,digit=check_digit_value,punctuation=check_punctuation_value)

        output.config(text=password,bg="#fff")
    except Exception :
        mb.showerror("Error","Unkwon Error")
    
#copy password in clipboard
def copyPass():
    try:
        text = output.cget("text")
        main.clipboard_clear()
        main.clipboard_append(text)
        main.update()
    except AttributeError:
        mb.showerror("Error","Gentrate Password")
    

main =tk.Tk()
main.title("PASSWORD GENRATOR")
main.geometry("600x300")
main.resizable(0,0)
main.config(bg="#ccff66")
Bg= main.cget("bg")
icon = PhotoImage(file='download.png')
main.iconphoto(False,icon)

check_upper = BooleanVar()
check_lower = BooleanVar()
check_digit = BooleanVar()
check_punctuation = BooleanVar()

lenght_label = Label(main,text="Length",fg="#000",bg=Bg)
lenght_label.place(x=60,y=30)
length = Entry(main,background="#999", width=15, fg="#000")
length.place(x=130,y=30)
Button1 = Checkbutton(main,text="UPPER CASE",variable = check_upper,offvalue=False,onvalue=True,height=2,width=10,bg=Bg,fg="#000")
Button1.place(x=60,y=60)
Button2 = Checkbutton(main,text="LOWER CASE",variable =check_lower,offvalue=False,onvalue=True,height=2,width=10,bg=Bg,fg="#000")
Button2.place(x=180,y=60)
Button3 = Checkbutton(main,text="DIGIT",variable = check_digit,offvalue=False,onvalue=True,height=2,width=10,bg=Bg,fg="#000")
Button3.place(x=320,y=60)
Button4 = Checkbutton(main,text="SPECIAL CHAR",variable = check_punctuation,offvalue=False,onvalue=True,height=2,width=10,bg=Bg,fg="#000")
Button4.place(x=440,y=60)
genrate_button = Button(main,text = "Genrate" ,command=genrate)
genrate_button.place(x=250,y=100)

output = Label(main,text="", fg="#000",bg=Bg)
output.place(x=30,y=150)

Image = PhotoImage(file="duplicate.png")
copy_button = Button(main,text="Copy",command=copyPass)
copy_button.place(x=30,y=200)

main.mainloop()
    
      