# Importing necessary libraries
import flet as ft

def main(page: ft.Page):
    # Set the background color of the page and title
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "TO DO List in Flet by David Caleb"
    
    # Center the content horizontally on the page
    page.horizontal_align = ft.CrossAxisAlignment.CENTER

    # Create the title for the to-do list
    title = ft.Text(
        "My to-do list with Flet",
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    # Function to add a new task to the list when the button is clicked
    def add_task(e):
        # Check if the task field has a value
        if task_field.value:
            # Create a new task as a ListTile with a checkbox
            task = ft.ListTile(
                title=ft.Text(task_field.value),
                leading=ft.Checkbox(on_change=select_task)
            )
            # Append the new task to the tasks list
            tasks.append(task)
            # Clear the task input field
            task_field.value = ""
            # Update the list to reflect the new task
            update_list()
    
    # Function to select a task and update the selected tasks list
    def select_task(e):
        # Get the selected tasks (checked checkboxes) and update the selected_tasks text
        selected = [task.title.value for task in tasks if task.leading.value]
        selected_tasks.value = "Selected Tasks: " + ", ".join(selected)
        # Update the page to show the changes
        page.update()

    # Function to refresh the task list display on the page
    def update_list():
        # Clear the current list of tasks and repopulate with updated tasks
        list_task.controls.clear()
        list_task.controls.extend(tasks)
        # Update the page to reflect changes
        page.update()

    # TextField for user input to write new tasks
    task_field = ft.TextField(hint_text="Write a new task")
    
    # Button to trigger the add_task function when clicked
    btn_add = ft.FilledButton(
        text="Add task", 
        on_click=add_task
    )

    # ListView to display the list of tasks, with spacing between them
    list_task = ft.ListView(expand=1, spacing=3)

    # List to hold all tasks added by the user
    tasks = []
    
    # Text field to display the selected tasks (tasks that are checked)
    selected_tasks = ft.Text("", size=20, weight=ft.FontWeight.BOLD)

    # Add the title, task field, and add button to the page, aligning them to the center
    page.add(
        ft.Column(
            [
                title,
                task_field,
                btn_add,
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Vertically align to the center
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Horizontally align to the center
        ),
        # Add the list of tasks and the selected tasks display to the page
        list_task,
        selected_tasks
    )

# Run the Flet application with the main function as the target
ft.app(target=main)
