import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

app=ctk.CTk()
app.title("TO-DO List")
app.geometry("350x450")
app.config(bg='#09112e')
app.resizable(0,0)
font1=('Arial',30,'bold')
font2=('Arial',18,'bold')
font3=('Arial',10,'bold')

def addTask():
    task=task_entry.get()
    if task:
        tasks_list.insert(0,task)
        task_entry.delete(0,END)
        save()
    else:
        messagebox.showerror('Error','Enter a task.')

def removeTask():
    selected=tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        save()
    else:
        messagebox.showerror('Error','Choose a task to delete.')

def save():
    with open('tasks.txt','w') as f:
        tasks=tasks_list.get(0,END)
        for i in tasks:
            f.write(i+'\n')

def load():
    try:
        with open('tasks.txt','r') as f:
            tasks=f.readlines()
            for i in tasks:
                tasks_list.insert(0,i.strip())
    except FileNotFoundError:
        messagebox.showerror('Error','Cannot load tasks.')

titleLabel=ctk.CTkLabel(app,font=font1,text='TO-DO List',text_color='#fff',bg_color='#09112e')
titleLabel.place(x=100,y=20)

addBtn=ctk.CTkButton(app,font=font2,text_color='#fff',text='Add Task',fg_color='#06911f',hover_color='#06911f',bg_color='#09112e',cursor='hand2',corner_radius=5,width=120,command=addTask)
addBtn.place(x=40,y=80)

removeBtn=ctk.CTkButton(app,font=font2,text_color='#fff',text='Remove Task',fg_color='#96061c',hover_color='#96061c',bg_color='#09112e',cursor='hand2',corner_radius=5,width=120,command=removeTask)
removeBtn.place(x=180,y=80)

task_entry=ctk.CTkEntry(app,font=font2,text_color='#000',fg_color='#fff',border_color='#fff',width=280)
task_entry.place(x=40,y=120)
tasks_list=Listbox(app,width=59,height=22,font=font3)
tasks_list.place(x=60,y=280)

load()
app.mainloop()