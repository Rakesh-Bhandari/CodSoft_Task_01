import customtkinter
from tkinter import*
from tkinter import messagebox
import sys

app=customtkinter.CTk()
app.title('To-Do List')
app.geometry('750x450')
app.config(bg='#5c8ab6')
app.resizable(width='false',height='false')


font1=('Arial',35,'bold')
font2=('Arial',18,'bold')
font3=('Consoles',30,'bold')

def add_task():
 task=task_entry.get()
 if task:
  tasks_list.insert(0,task)
  task_entry.delete(0,END)
  save_tasks()
 else:
  messagebox.showerror('Error!','Enter a task.')
  
def remove_task():
 selected=tasks_list.curselection()
 if selected:
  tasks_list.delete(selected[0])
  save_tasks()
 else:
  messagebox.showerror('Error!','Choose a task to delete.')
  
def update_task():
 selected=tasks_list.curselection()
 task=task_entry.get()
 if selected:
  if task:
   tasks_list.delete(selected[0])
   tasks_list.insert(selected[0],task)
   task_entry.delete(0,END)
   save_tasks()
  else:
   messagebox.showerror('Error!','Enter a task to update.')
 else:
  messagebox.showerror('Error!','Choose a task to update.')
 
def save_tasks():
 with open("tasks.txt","w")as f:
  tasks=tasks_list.get(0,END)
  for task in tasks:
   f.write(task+"\n")
              
def load_tasks():
 try:
  with open("tasks.txt","r")as f:
   tasks=f.readlines()
   for task in tasks:
    tasks_list.insert(0,task.strip())
 except FileNotFoundError:
  pass          
  
 def exit():
  sys.exit(0)

grid=customtkinter.CTkLabel(app,bg_color='#09112e',width=250,height=450,text='')
grid.place(x=0,y=0)
title_label=customtkinter.CTkLabel(app,font=font1,text='To-Do List',text_color='#fff',bg_color='#09112e')
title_label.place(x=40,y=40)

add_button=customtkinter.CTkButton(app,command=add_task,font=font2,text='Add Task',text_color='#fff',fg_color='#00f',hover_color='#06911f',bg_color='#09112e',cursor='hand2',corner_radius=5,width=120)
add_button.place(x=60,y=100)

del_button=customtkinter.CTkButton(app,command=remove_task,font=font2,text='DeleteTask',text_color='#fff',fg_color='#00f',hover_color='#96061f',bg_color='#09112e',cursor='hand2',corner_radius=5,width=120)
del_button.place(x=60,y=160)

update_button=customtkinter.CTkButton(app,command=update_task,font=font2,text='Update Task',text_color='#fff',fg_color='#0331ff',hover_color='#03319f',bg_color='#09112e',cursor='hand2',corner_radius=5,width=120)
update_button.place(x=60,y=220)

exit_button=customtkinter.CTkButton(app,command=exit,font=font2,text='Exit',text_color='#fff',fg_color='#0331ff',hover_color='#000',bg_color='#09112e',cursor='hand2',corner_radius=5,width=120)
exit_button.place(x=60,y=280)

task_entry=customtkinter.CTkEntry(app,font=font2,text_color='#000',fg_color='#fff',border_color='#fff',width=440,bg_color='#5c8ab6',height=50)
task_entry.place(x=280,y=20)

tasks_list=Listbox(app,width=25,height=9,font=font3)
tasks_list.place(x=350,y=95)

load_tasks()
app.mainloop()