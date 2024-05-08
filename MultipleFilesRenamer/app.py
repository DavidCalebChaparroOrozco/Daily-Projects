# Importing necessary libraries
import os
import glob
from tkinter import *
from threading import *
from PIL import ImageTk, Image
from tkinter import messagebox, ttk, filedialog

# File Extensions
file_types = [".jpg", ".jpeg",".png", ".mp3", ".mp4", '.pdf']

# Class FileRenamer
class FileRenamer:
    def __init__(self, root):
        # Setting the Tkinter main window
        self.window = root
        self.window.geometry("800x500")
        self.window.title("File Renamer by David Caleb")
        self.window.resizable(width = False, height = False)
        self.window.configure(bg='black')

        # Declaring variables
        self.Selected_Folder = ""
        self.SaveTo_Loc = ""
        self.File_List = list()
        self.File_Dict = dict()

        # Frame (Logo)
        self.frame_1 = Frame(self.window, bg="gray90", width=300, height=70)
        self.frame_1.pack()
        self.frame_1.place(x=20,y=20)
        # Call the function to display the logo
        self.Logo()

        # Button (About)
        About_btn = Button(self.window, text="About", font=("Arial", 12, "bold"), fg="white", width=5, command=self.About_Window)
        About_btn.place(x=600, y=20)

        # Button (Exit)
        Exit_btn = Button(self.window, text="Exit", font=("Arial", 12, "bold"), fg="white", width=5, command=self.Exit_Window)
        Exit_btn.place(x=600, y=60)

        # Frame (Main Window Widgets)
        self.frame_2 = Frame(self.window, bg="white", width=720, height=480)
        # self.frame_2.pack()
        self.frame_2.place(x=0,y=110)
        # Call the function to display main window widgets
        self.Main_Window()

    # Display the Logo
    def Logo(self):
        image = Image.open("Images/logo.png")
        # Resizing the image
        resized_image = image.resize((280,70))
        self.img_1 = ImageTk.PhotoImage(resized_image)
        # Create a Label Widget to display the text or Image
        label_image = Label(self.frame_1, bg="gray90", image=self.img_1)
        label_image.pack()

    # Add Widgets to the Main Window
    def Main_Window(self):
        Filetype_Label = Label(self.frame_2, text="File Type: ", font=("Arial", 12, "bold"), bg="white")
        Filetype_Label.place(x=50, y=30)
        self.f_type = StringVar()
        # Combo Box for showing the file extensions
        self.file_type = ttk.Combobox(self.frame_2, textvariable=self.f_type, font=("Time New Roman", 12), width=8)
        self.file_type["values"] = file_types
        self.file_type.current(0)
        self.file_type.place(x=150, y=30)

        # Button for selecting the directory
        Folder_Button = Button(self.frame_2, text="Select Folder", font=("Arial", 12, "bold"), bg="gold", width=10, command=self.Select_Directory)
        Folder_Button.place(x=20, y=70)

        # Select Folder
        self.Folder_Entry = Entry(self.frame_2, font=("Helvetica",12), width=30)
        self.Folder_Entry.place(x=150, y=75)

        # Save To
        SaveTo_btn = Button(self.frame_2, text="Save To", font=("Arial", 12, "bold"), bg="green", fg="white", width=10, command=self.SaveTo_Directory)
        SaveTo_btn.place(x=20, y=125)
        self.SaveTo_Entry = Entry(self.frame_2, font=("Arial", 12), width=30)
        self.SaveTo_Entry.place(x=150, y=130)

        # ResultFile
        ResultFile_Label = Label(self.frame_2, text="Result File: ", font=("Arial", 12, 'bold'), bg='white')
        ResultFile_Label.place(x=35, y=175)
        self.ResultFile_Entry = Entry(self.frame_2, font=("Arial", 12))
        self.ResultFile_Entry.place(x=150, y=175)

        # Status
        Status = Label(self.frame_2, text="Status: ", font=("Arial", 12, 'bold'), bg='white')
        Status.place(x=70, y=215)
        self.Status_Label = Label(self.frame_2, text="Not Started Yet", font=("Arial", 12), bg="white", fg="red")
        self.Status_Label.place(x=150, y=215)

        # ListBox Label
        Listbox_Label = Label(self.frame_2, text="Selected Files", font=("Times New Roman", 14, 'bold'), bg='white')
        Listbox_Label.place(x=515, y=30)

        # Listbox for showing the selected files for renaming
        self.File_ListBox = Listbox(self.frame_2,width=30, height=14)
        self.File_ListBox.place(x=450, y=60)

        # Add button
        Add_Button = Button(self.frame_2, text='Add',font=("Arial", 9, 'bold'), width=6, command=self.Add_File)
        Add_Button.place(x=450, y=322)

        # Delete button
        Delete_Button = Button(self.frame_2, text='Delete', font=("Arial", 9, 'bold'), width=6, command=self.Delete_File)
        Delete_Button.place(x=530, y=322)

        Start_Button = Button(self.frame_2, text="Start", font=("Arial", 13, 'bold'), bg="dodger blue", fg="white", width=8, command=self.Threading)
        Start_Button.place(x=120, y=260)


    # Select the Folder
    def Select_Directory(self):
        self.Clear_Listbox()
        self.Selected_Folder = filedialog.askdirectory(title = "Select a location")
        self.Folder_Entry.insert(0, self.Selected_Folder)
        # If the user selects a directory
        if self.Selected_Folder != '':
            self.Files_in_Listbox()

    # Choose the Save To Location
    def SaveTo_Directory(self):
        self.SaveTo_Loc = filedialog.askdirectory(title = "Select a location")
        self.SaveTo_Entry.insert(0, self.SaveTo_Loc)

    # Insert the File Names to the Listbox
    def Files_in_Listbox(self):
        self.File_List = \
        glob.glob(f"{self.Selected_Folder}/*{self.file_type.get()}")
        for path in self.File_List:
            self.File_Dict[os.path.basename(path)] = path
            self.File_ListBox.insert(END, os.path.basename(path))
    
    # Add Files to the Listbox
    def Add_File(self):
        File_Path = filedialog.askopenfilenames(initialdir = "/", \
        title = "Select PDF Files", filetypes = \
        ((f"{self.file_type.get()} files",f"*{self.file_type.get()}*"),))

        for Path in File_Path:
            # Adding the file path to the 'self.File_List'
            self.File_List.append(Path)
            self.File_Dict[os.path.basename(Path)] = Path
            self.File_ListBox.insert(END, os.path.basename(Path))

    # Delete Files from Listbox
    def Delete_File(self):
        try:
            if len(self.File_List) < 1:
                messagebox.showwarning('Warning!', \
                'There are no more files to delete')
            else:
                for item in self.File_ListBox.curselection():
                    self.File_List.remove(\
                    self.File_Dict[self.File_ListBox.get(item)])
                    self.File_Dict.pop(self.File_ListBox.get(item))

                    self.File_ListBox.delete(item)
        except Exception:
            messagebox.showwarning('Warning!', "Please select PDFs first")

    # Create a Thread and Perform Renaming Operation
    def Threading(self):
        self.x = Thread(target=self.Rename_Files, daemon=True)
        self.x.start()

    def Rename_Files(self):
        # If no files are presented in the 'self.File_List'
        # a Tkinter MessageBox will pop up
        if len(self.File_List) == 0:
            messagebox.showerror('Error!', "There are no files to rename")
        else:
            # If the user doesn't select the Saving Location a warning message will display
            if self.SaveTo_Entry.get() == '':
                messagebox.showwarning('Warning!', \
                "Please Select a Save Location")
            else:
                # If the user doesn't enter the Base File Name
                if self.ResultFile_Entry.get() == '':
                    self.Status_Message(status = 'Renaming...')
                    for file in self.File_List:
                        source = file

                        Part1 = self.SaveTo_Entry.get()
                        Part2 = self.File_List.index(file)
                        Part3 = self.file_type.get()

                        destination = f"{Part1}/{Part2}{Part3}"
                        # Calling the os.rename function
                        os.rename(source, destination)
                    self.Clear_Listbox()
                    self.Status_Message(status = 'Renaming Completed.')
                    self.Done_Message()
                else:
                    # If the user entered the Base File Name
                    self.Status_Message(status = 'Renaming...')
                    for file in self.File_List:
                        source = file

                        Part1 = self.SaveTo_Entry.get()
                        Part2 = self.ResultFile_Entry.get()
                        Part3 = self.File_List.index(file)
                        Part4 = self.file_type.get()

                        destination = f"{Part1}/{Part2}_{Part3}{Part4}"
                        # Calling the os.rename function
                        os.rename(source, destination)
                    self.Clear_Listbox()
                    self.Status_Message(status = 'Renaming Completed.')
                    self.Done_Message()

    # Display the Status
    def Status_Message(self, **Status):
        for key, value in Status.items():
            self.Status_Label.config(text=value)
    
    # Clear the Listbox
    def Clear_Listbox(self):
        self.File_List.clear()
        self.File_Dict.clear()
        self.Selected_Folder = ''
        self.SaveTo_Loc = ''
        self.Status_Label.config(text="Not Started Yet")
        self.Folder_Entry.delete(0, END)
        self.SaveTo_Entry.delete(0, END)
        self.ResultFile_Entry.delete(0, END)
        self.File_ListBox.delete(0, END)

    def Done_Message(self):
        messagebox.showinfo('Done!', "The files are renamed successfully")

    def About_Window(self):
        messagebox.showinfo("File Renamer", \
                            "Developed by David Caleb")

    def Exit_Window(self):
        self.window.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = FileRenamer(root)
    root.mainloop()