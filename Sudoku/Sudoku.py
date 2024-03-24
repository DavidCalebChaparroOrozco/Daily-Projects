# Importing necessary libraries
from collections import deque
import tkinter
from tkinter import PhotoImage

# Creating the main window
root = tkinter.Tk()
root.title("Sudoku Solver")
root.tk.call("wm", "iconphoto", root._w, PhotoImage(file="Sudoku.png"))

# Class to handle the Sudoku Solver functionality
class Solver:
    def __init__(self, master):
        # Initializing objects
        self.cells = {}
        self.entries = []
        
        # Generating Sudoku grid
        for row in range(1, 10):
            for column in range(1, 10):
                # Setting grid cell color
                if ((row in (1,2,3,7,8,9) and column in (4,5,6)) 
                    or (row in (4,5,6) and column in (1,2,3,7,8,9))):
                    color='#e0e0e0'
                else:
                    color='#f2f2f2'
                
                # Creating grid cells
                cell = tkinter.Frame(master, highlightbackground=color, highlightcolor=color, highlightthickness=2, width=50, height=50, padx=3,  pady=3, background='black')
                cell.grid(row=row, column=column)
                self.cells[(row, column)] = cell
                validate_num = master.register(self.validate_input)

                # Creating entry widgets for user input
                e = tkinter.Entry(self.cells[row, column], justify='center', validate="key", validatecommand=(validate_num, "%P"))
                e.place(height=40, width=40)
                self.entries.append(e)
                
        # Creating buttons 
        topFrame = tkinter.Frame(master)
        topFrame2 = tkinter.Frame(master)
        topFrame3 = tkinter.Frame(master)

        solveButton = tkinter.Button(topFrame, text="SOLVE", command=self.solve, bg='#4a90e2', fg='white')
        solveButton.pack()

        visualButton = tkinter.Button(topFrame2, text="VISUAL", command=self.visualbacktrack, bg='#4a90e2', fg='white')
        visualButton.pack()

        resetButton = tkinter.Button(topFrame3, text="CLEAR", command=self.reset, bg='#77dd77', fg='white')
        resetButton.pack()

        topFrame.grid(column=5, row=0)
        topFrame2.grid(column=4, row=0)
        topFrame3.grid(column=6, row=0)

    # Converts user input into an array/python list
    def turnToList(self):
        outputList = []

        for row in range(9):
            nestedList = []

            for column in range(9):
                if self.entries[column + (row * 9)].get() == "":
                    nestedList.append(0)
                else:
                    nestedList.append(int(self.entries[column + (row * 9)].get()))

            outputList.append(nestedList)

        return outputList

    # Backtracking method to solve Sudoku
    def pickEmpty(self, inputBoard, vis):
        self.stack = deque()
        rowIndex = 0
        columnIndex = 0

        while rowIndex < 9:
            columnIndex = 0

            while columnIndex < 9:
                if inputBoard[rowIndex][columnIndex] == 0:
                    # Tries to input num from 1-9
                    index = self.trynum([rowIndex, columnIndex], 1, inputBoard, vis)
                    rowIndex = index[0]
                    columnIndex = index[1]

                columnIndex += 1
            rowIndex += 1

    # Checks if a number is valid in its row, column, or square
    def validInput(self, number, boardInput, indexes):
        if (not self.inColumn(number, boardInput, indexes) and not self.inRow(number, boardInput, indexes) and not self.inSquare(number, boardInput, indexes)):
            return True
        return False

    # Helper function: checks if number exists in its row
    def inRow(self, number, boardInput, indexes):
        for num in boardInput[indexes[0]]:
            if number == num:
                return True
        return False

    # Helper function: checks if number exists in its column
    def inColumn(self, number, boardInput, indexes):
        for row in boardInput:
            if row[indexes[1]] == number:
                return True
        return False

    # Helper function: checks if number exists in its square
    def inSquare(self, number, boardInput, indexes):
        botX = (indexes[0] // 3) * 3
        topX = ((indexes[0] // 3) * 3) + 3
        botY = (indexes[1] // 3) * 3
        topY = ((indexes[1] // 3) * 3) + 3

        for x in range(botX, topX):
            for y in range(botY, topY):
                if boardInput[x][y] == number:
                    return True
        return False

    # Tries a number in a cell
    def trynum(self, indexes, start, boardInput, visual):
        for number in range(start, 10):
            if self.validInput(number, boardInput, indexes):
                boardInput[indexes[0]][indexes[1]] = number

                # Updates color change if visual
                if visual:
                    self.entries[(indexes[0] * 9 + indexes[1])].configure(foreground="red", highlightbackground="green")
                    self.entries[(indexes[0] * 9 + indexes[1])].insert(0, number)
                    root.update()
                    self.entries[(indexes[0] * 9 + indexes[1])].configure(foreground="red", highlightbackground="white")
                else:
                    self.entries[(indexes[0] * 9 + indexes[1])].configure(foreground="red")
                    self.entries[(indexes[0] * 9 + indexes[1])].insert(0, number)

                self.stack.append(indexes)
                return indexes

        return self.backtrack(boardInput, visual)

    # Backtracks to previous state if no solution found
    def backtrack(self, boardinp, vis):
        lastWrong = self.stack.pop()
        # Stores previous wrong value
        prevVal = boardinp[lastWrong[0]][lastWrong[1]]
        # Resets last wrong to 0 and deletes from GUI
        boardinp[lastWrong[0]][lastWrong[1]] = 0
        self.entries[lastWrong[0] * 9 + lastWrong[1]].delete(0, tkinter.END)
        return self.trynum(lastWrong, prevVal + 1, boardinp, vis)

    # Checks if the current board configuration is valid
    def isBoardValid(self, userBoard):
        return True

    # Normal Solve
    def solve(self):
        if self.isBoardValid("Not Finished"):
            self.pickEmpty(self.turnToList(), False)

    # Visual Solve
    def visualbacktrack(self):
        if self.isBoardValid("Not Finished"):
            self.pickEmpty(self.turnToList(), True)

    # Resets the Sudoku board
    def reset(self):
        for value in self.entries:
            value.delete(0, tkinter.END)
            value.configure(foreground="black")

    # Validate input to allow only numbers and one character
    def validate_input(self, new_text):
        if new_text.isdigit() and len(new_text) <= 1 or new_text == "":
            return True
        else:
            return False

# Creating an instance of the Solver class
ye = Solver(root)

# Running the main loop
root.mainloop()
