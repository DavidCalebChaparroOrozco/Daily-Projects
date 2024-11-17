# Importing necessary libraries
import tkinter as tk
from tkinter import messagebox, simpledialog
import json
from datetime import datetime, timedelta

# Class to represent a task with a description and category.
class Task:
    def __init__(self, description, category):
        self.description = description
        self.category = category

    # Convert the task to a dictionary for JSON serialization.
    def to_dict(self):
        return {
            "description": self.description,
            "category": self.category
        }

class TaskPrioritizationMatrix(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Prioritization Matrix by David Caleb")
        self.geometry("400x600")
        self.configure(bg="#2e2e2e")

        # Initialize task lists for each quadrant
        self.tasks = {
            "urgent_important": [],
            "urgent_not_important": [],
            "not_urgent_important": [],
            "not_urgent_not_important": []
        }

        # Create UI components
        self.create_ui()

    def create_ui(self):
        # Create frames for each quadrant
        self.frames = {}
        quadrants = [
            ("Urgent & Important", "urgent_important"),
            ("Urgent & Not Important", "urgent_not_important"),
            ("Not Urgent & Important", "not_urgent_important"),
            ("Not Urgent & Not Important", "not_urgent_not_important")
        ]
        
        for i, (title, key) in enumerate(quadrants):
            frame = tk.Frame(self, relief=tk.RAISED, borderwidth=2)
            frame.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")
            label = tk.Label(frame, text=title)
            label.pack()
            listbox = tk.Listbox(frame, selectmode=tk.SINGLE)
            listbox.pack(expand=True, fill=tk.BOTH)
            listbox.bind("<Button-1>", self.on_click)
            listbox.bind("<B1-Motion>", self.on_drag)
            listbox.bind("<ButtonRelease-1>", self.on_drop)
            self.frames[key] = (frame, listbox)

        # Buttons
        add_task_button = tk.Button(self, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white")
        add_task_button.grid(row=2, column=0, columnspan=2)

        edit_task_button = tk.Button(self, text="Edit Task", command=self.edit_task, bg="#2196F3", fg="white")
        edit_task_button.grid(row=4, column=0, columnspan=2)

        delete_task_button = tk.Button(self, text="Delete Task", command=self.delete_task, bg="#F44336", fg="white")
        delete_task_button.grid(row=5, column=0, columnspan=2)

        report_button = tk.Button(self, text="Generate Weekly Report", command=self.generate_report, bg="#FFC107", fg="black")
        report_button.grid(row=6, column=0, columnspan=2)

    # Prompt user to enter a new task and its category.
    def add_task(self):
        description = simpledialog.askstring("New Task", "Enter task description:")
        if description:
            category = simpledialog.askstring(
                "Task Category",
                "Select category:\n1. Urgent & Important\n2. Urgent & Not Important\n3. Not Urgent & Important\n4. Not Urgent & Not Important"
            )
            category_map = {
                "1": "urgent_important",
                "2": "urgent_not_important",
                "3": "not_urgent_important",
                "4": "not_urgent_not_important"
            }
            key = category_map.get(category)
            if key:
                new_task = Task(description, key)
                self.tasks[key].append(new_task)
                self.update_listbox(key)
            else:
                messagebox.showerror("Error", "Invalid category! Please enter a number from 1 to 4.")

    # Update the ListBox with current tasks in the specified quadrant.
    def update_listbox(self, key):
        listbox = self.frames[key][1]
        listbox.delete(0, tk.END)  # Clear current tasks
        for task in self.tasks[key]:  # Add updated tasks
            listbox.insert(tk.END, task.description)

    # Store the index of the selected task for dragging or editing.
    def on_click(self, event):
        widget = event.widget
        index = widget.curselection()
        if index:
            widget.dragged_index = index[0]

    # Handle dragging of the selected task.
    def on_drag(self, event):
        pass  # No specific action needed during dragging

    # Handle dropping of the selected task into a different quadrant.
    def on_drop(self, event):
        widget = event.widget
        dragged_index = getattr(widget, 'dragged_index', None)
        
        if dragged_index is not None:  # Get the dragged task and remove it from its original list
            task_description = widget.get(dragged_index)
            
            for key in self.tasks:
                for task in self.tasks[key]:
                    if task.description == task_description:
                        self.tasks[key].remove(task)  # Remove from original quadrant
                        break
            
            # Determine which quadrant was dropped into and add the task there
            for key in self.frames:
                if widget == self.frames[key][1]:
                    new_task = Task(task_description, key)  # Create a new task instance
                    self.tasks[key].append(new_task)  # Add to new quadrant
                    break
            
            # Update all ListBoxes to reflect changes
            for key in self.frames:
                self.update_listbox(key)

    # Edit the selected task's description.
    def edit_task(self):
        selected_quadrant = None
        
        for key in self.frames:
            listbox = self.frames[key][1]
            if listbox.curselection():
                selected_quadrant = key
                break
        
        if selected_quadrant is None:
            messagebox.showwarning("Warning", "Please select a task to edit.")
            return
        
        listbox = self.frames[selected_quadrant][1]
        selected_index = listbox.curselection()[0]
        current_task_description = listbox.get(selected_index)
        
        new_description = simpledialog.askstring("Edit Task", f"Edit description for: {current_task_description}")
        
        if new_description:  # Update the task's description
            for task in self.tasks[selected_quadrant]:
                if task.description == current_task_description:
                    task.description = new_description
                    break
            
            # Refresh the ListBox display
            self.update_listbox(selected_quadrant)

    # Delete the selected task from its quadrant.
    def delete_task(self):
        selected_quadrant = None
        
        for key in self.frames:
            listbox = self.frames[key][1]
            if listbox.curselection():
                selected_quadrant = key
                break
        
        if selected_quadrant is None:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            return
        
        listbox = self.frames[selected_quadrant][1]
        selected_index = listbox.curselection()[0]
        current_task_description = listbox.get(selected_index)
        
        # Remove the selected task from the corresponding quadrant
        for task in self.tasks[selected_quadrant]:
            if task.description == current_task_description:
                self.tasks[selected_quadrant].remove(task)
                break
        
        # Refresh the ListBox display
        self.update_listbox(selected_quadrant)

    # Generate a weekly report of tasks categorized by urgency and importance.
    def generate_report(self):
        report_date = datetime.now() - timedelta(days=7)
        
        report_data = {
            "date": report_date.strftime("%Y-%m-%d"),
            "tasks": {key: [task.to_dict() for task in value] for key, value in self.tasks.items()}
        }
        
        report_filename = f"weekly_report_{report_date.strftime('%Y%m%d')}.json"
        
        with open(report_filename, 'w') as report_file:
            json.dump(report_data, report_file, indent=4)
        
        messagebox.showinfo("Report Generated", f"Weekly report saved as {report_filename}")

if __name__ == "__main__":
    app = TaskPrioritizationMatrix()
    app.mainloop()