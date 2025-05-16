import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TodoListApp:
    def _init_(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        # Create GUI elements
        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.priority_var = tk.StringVar()
        self.priority_var.set("Low")
        self.priority_menu = tk.OptionMenu(master, self.priority_var, "Low", "Medium", "High")
        self.priority_menu.grid(row=0, column=1, padx=5, pady=10)

        self.due_date_entry = tk.Entry(master, width=15)
        self.due_date_entry.grid(row=0, column=2, padx=5, pady=10)
        self.due_date_entry.insert(tk.END, self.get_today_date())

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=3, padx=5, pady=10)

        self.task_listbox = tk.Listbox(master, width=70, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=5, pady=10)

        self.complete_button = tk.Button(master, text="Mark Complete", command=self.mark_complete)
        self.complete_button.grid(row=2, column=1, padx=5, pady=10)

        # Add some default tasks
        self.add_default_tasks()

    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_var.get()
        due_date = self.due_date_entry.get()

        if task:
            self.tasks.append({"task": task, "priority": priority, "due_date": due_date, "completed": False})
            self.task_listbox.insert(tk.END, self.format_task_display(task, priority, due_date))
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

    def mark_complete(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = True
            self.task_listbox.itemconfig(selected_index, {'bg': 'lightgrey', 'fg': 'grey'})
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

    def add_default_tasks(self):
        default_tasks = [
            {"task": "Task 1", "priority": "High", "due_date": self.get_today_date(), "completed": False},
            {"task": "Task 2", "priority": "Medium", "due_date": self.get_today_date(), "completed": False},
            {"task": "Task 3", "priority": "Low", "due_date": self.get_today_date(), "completed": True}
        ]
        for task_data in default_tasks:
            self.tasks.append(task_data)
            self.task_listbox.insert(tk.END, self.format_task_display(task_data["task"], task_data["priority"], task_data["due_date"], task_data["completed"]))

    def get_today_date(self):
        return datetime.today().strftime("%Y-%m-%d")

    def format_task_display(self, task, priority, due_date, completed=False):
        if completed:
            return f"[COMPLETED] {task} - Priority: {priority} - Due Date: {due_date}"
        else:
            return f"{task} - Priority: {priority} - Due Date: {due_date}"

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if _name_ == "_main_":
    main()