import tkinter as tk
from tkinter import filedialog
class TodoListApp(tk.Tk):
    def __init__(self):
        super(). __init__()
        self.geometry("600x600")
        self.title("TO DO LIST")
        #self['background']='red'
        self.create_widgets()
    def create_widgets(self):
        self.task_input=tk.Entry(self, width=100)
        self.task_input.pack(pady=15)
        self.add_task_button=tk.Button(self, text="ADD TASK",font=('arial',12), borderwidth=10, fg='red',  command=self.add_task)
        self.add_task_button.pack(pady=10)
        self.tasks_Listbox=tk.Listbox(self, selectmode=tk.SINGLE, bg='white', fg='red', font=('arial',20))
        self.tasks_Listbox.winfo_geometry()
        self.tasks_Listbox.pack(pady=10)
        self.button_frame=tk.Frame(self)
        self.button_frame.pack(pady=10)
        self.edit_task_button=tk.Button(self.button_frame, text="EDIT TEXT",font=('arial',12), borderwidth=10,fg='red', command=self.edit_task)
        self.edit_task_button.grid(row=0, column=0, padx=10, pady=10)
        self.delete_task_button=tk.Button(self.button_frame, text="DELETE TASK",font=('arial',12), fg='red', borderwidth=10,  command=self.delete_task)
        self.delete_task_button.grid(row=0, column=1, padx=50, pady=50)
        self.save_button=tk.Button(self, text="SAVE",font=('arial',12), borderwidth=10, command=self.save_tasks)
        self.button_frame.pack(pady=10)
        self.load_button=tk.Button(self, text="LOAD", command=self.load_tasks)
        self.button_frame.pack(pady=10)
    def add_task(self):
        task=self.task_input.get()
        if task:
            self.tasks_Listbox.insert(tk.END, task)
            self.task_input.delete(0, tk.END)
    def edit_task(self):
        task_index=self.tasks_Listbox.curselection()
        if task_index:
            new_task=self.task_input.get()
            if new_task:
                self.tasks_Listbox.delete(task_index)
                self.tasks_Listbox.insert(task_index, new_task)
                self.task_input.delete(0, tk.END)
    def delete_task(self):
        task_index=self.tasks_Listbox.curselection()
        if task_index:
            self.tasks_Listbox.delete(task_index)
    def save_tasks(self):
        tasks=self.tasks_Listbox.get(0, tk.END)
        file_path=filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w')as file:
                for task in tasks:
                    file.write(task + '\n')
    def load_tasks(self):
        file_path=filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r')as file:
                tasks=[Line.strip() for Line in file.readlines()]
            self.tasks_Listbox.delete(0, tk.END)
            for task in tasks:
                self.tasks_Listbox.insert(tk.END, task)        