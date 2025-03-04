import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("450x550")

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task ✅", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.remove_button = tk.Button(root, text="Remove Selected ❌", command=self.remove_task)
        self.remove_button.pack()

        self.clear_button = tk.Button(root, text="Clear All 🗑", command=self.clear_tasks)
        self.clear_button.pack()

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected)
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

    def clear_tasks(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
            self.task_listbox.delete(0, tk.END)
            self.save_tasks()

    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        with open(TASKS_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                for task in file.readlines():
                    self.task_listbox.insert(tk.END, task.strip())

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
