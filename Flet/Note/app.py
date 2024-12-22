import flet as ft

# This function will be called when the user clicks the "Add Note" button
def add_note(e, page):
    # Get the note text from the input field
    note_text = note_input.value.strip()
    
    # Only add the note if it's not empty
    if note_text:
        # Create a new Text control for the note
        note_item = ft.Row(
            controls=[
                # Display the note text
                ft.Text(note_text, size=20),  
                # Delete button
                ft.IconButton(ft.icons.DELETE, on_click=lambda e: remove_note(note_item, page))  
            ],
            # Align items in the row
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN  
        )
        
        # Add the new note item to the notes list
        notes_list.controls.append(note_item)
        
        # Clear the input field after adding the note
        note_input.value = ""
        
        # Update the page to reflect changes
        page.update()

# This function will remove a note when the delete button is clicked
def remove_note(note_item, page):
    # Remove the specified note item
    notes_list.controls.remove(note_item)  
    # Update the page to reflect changes
    page.update()  

# Main function that initializes the app
def main(page: ft.Page):
    # Set the title of the page
    page.title = "Note-taking App by David Caleb"  

    # Input field for new notes
    # Declare as global to access in other functions
    
    global note_input  
    note_input = ft.TextField(label="Enter your note", width=300)

    # Button to add notes
    add_button = ft.ElevatedButton(text="Add Note", on_click=lambda e: add_note(e, page))

    # Container for displaying notes

    # Declare as global to access in other functions
    global notes_list  
    notes_list = ft.Column()

    # Add controls to the page
    page.add(
        # Row for input and button
        ft.Row(controls=[note_input, add_button]),  
        # Column for notes list
        notes_list  
    )

# Run the Flet app with main function as target
ft.app(target=main)
