# Import necessary modules
from tkinter import *
from tkinter import ttk
import datetime as dt
from mydb import *
from tkinter import messagebox, PhotoImage
import matplotlib.pyplot as plt
from collections import defaultdict

# Initialize database object
data = Database(db='test.db')

# Global variables
count = 0
selected_rowid = 0

# Function to save a record
def saveRecord():
    global data
    name = item_name.get()
    price_str = item_amt.get()
    date = transaction_date.get()
    
    if not date:
        messagebox.showerror("Error", "You must enter a date.")
        return
    if name.strip() == "":
        messagebox.showerror("Error", "The item name cannot be empty.")
        return
    try:
        price = float(price_str)
        if price <= 0:
            messagebox.showerror("Error", "The price of the item must be greater than 0.")
            return
    except ValueError:
        messagebox.showerror("Error", "The price of the item must be a float number.")
    data.insertRecord(item_name=name, item_price=price, purchase_date=date)

# Function to set current date
def setDate():
    date = dt.datetime.now()
    dopvar.set(f'{date:%d %B %Y}')

# Function to clear entry fields
def clearEntries():
    item_name.delete(0, 'end')
    item_amt.delete(0, 'end')
    transaction_date.delete(0, 'end')

# Function to fetch records from database
def fetch_records():
    f = data.fetchRecord('select rowid, * from expense_record')
    global count
    for rec in f:
        tv.insert(parent='', index='0', iid=count, values=(rec[0], rec[1], rec[2], rec[3]))
        count += 1
    tv.after(400, refreshData)

# Function to select a record from the table
def select_record(event):
    global selected_rowid
    selected = tv.focus()    
    val = tv.item(selected, 'values')
    try:
        selected_rowid = val[0]
        d = val[3]
        namevar.set(val[1])
        amtvar.set(val[2])
        dopvar.set(str(d))
    except Exception as ep:
        pass

# Function to update a record
def update_record():
    global selected_rowid
    selected = tv.focus()
    # Update record
    try:
        name = namevar.get()
        price = amtvar.get()
        date = dopvar.get()
        if name.strip() == "":
            messagebox.showerror("Error", "The item name cannot be empty.")
            return
        if price <= 0:
            messagebox.showerror("Error", "The price of the item must be greater than 0.")
            return

        data.updateRecord(name, price, date, selected_rowid)
        tv.item(selected, text="", values=(name, price, date))
    except Exception as ep:
        messagebox.showerror('Error',  ep)

    # Clear entry boxes
    clearEntries()
    tv.after(400, refreshData)


# Function to calculate total balance
def totalBalance():
    f = data.fetchRecord(query="Select sum(item_price) from expense_record")
    for i in f:
        for j in i:
            messagebox.showinfo('Current Balance: ', f"Total Expense: ' {j} \nBalance Remaining: {5000 - j}")

# Function to refresh data displayed in the table
def refreshData():
    for item in tv.get_children():
        tv.delete(item)
    fetch_records()
    
# Function to delete a record
def deleteRow():
    global selected_rowid
    data.removeRecord(selected_rowid)
    refreshData()

# Define a function to show the pie chart
def show_pie_chart():
    total_spent = data.fetchRecord(query="SELECT SUM(item_price) FROM expense_record")[0][0]
    balance_remaining = 5000 - total_spent

    labels = ['Spent', 'Balance']
    sizes = [total_spent, balance_remaining]
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)  # explode 1st slice (i.e. 'Spent')

    plt.figure(figsize=(8, 4))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Percentage of spending relative to balance')
    plt.show()

# Define a function to show the daily spending chart
def show_daily_spending_chart():
    # Get daily spending records
    records = data.fetchRecord(query="SELECT item_price, purchase_date FROM expense_record")
    daily_spending = defaultdict(float)

    for price, date in records:
        daily_spending[date] += price

    # Extract dates and daily spending
    dates = list(daily_spending.keys())
    amounts = list(daily_spending.values())

    plt.figure(figsize=(10, 6))
    plt.bar(dates, amounts, color='skyblue')
    plt.xlabel('Date')
    plt.ylabel('Spending')
    plt.title('Daily Spending')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# create tkinter object
root = Tk()
root.title('Daily Expenses')
root.tk.call("wm", "iconphoto", root._w, PhotoImage(file="expensetracking.png"))

# Define variables
f = ('Times new roman', 14)
namevar = StringVar()
amtvar = IntVar()
dopvar = StringVar()

# Frame widget
f2 = Frame(root)
f2.pack() 

f1 = Frame(
    root,
    padx=10,
    pady=10,
)
f1.pack(expand=True, fill=BOTH)


# Label widget
Label(f1, text='ITEM NAME', font=f).grid(row=0, column=0, sticky=W)
Label(f1, text='ITEM PRICE', font=f).grid(row=1, column=0, sticky=W)
Label(f1, text='PURCHASE DATE', font=f).grid(row=2, column=0, sticky=W)

# Entry widgets 
item_name = Entry(f1, font=f, textvariable=namevar)
item_amt = Entry(f1, font=f, textvariable=amtvar)
transaction_date = Entry(f1, font=f, textvariable=dopvar)

# Entry grid placement
item_name.grid(row=0, column=1, sticky=EW, padx=(10, 0))
item_amt.grid(row=1, column=1, sticky=EW, padx=(10, 0))
transaction_date.grid(row=2, column=1, sticky=EW, padx=(10, 0))


# Action buttons
cur_date = Button(
    f1, 
    text='Current Date', 
    font=f, 
    bg='#04C4D9', 
    command=setDate,
    width=15
    )

submit_btn = Button(
    f1, 
    text='Save Record', 
    font=f, 
    command=saveRecord, 
    bg='#42602D', 
    fg='white'
    )

clr_btn = Button(
    f1, 
    text='Clear Entry', 
    font=f, 
    command=clearEntries, 
    bg='#D9B036', 
    fg='white'
    )

quit_btn = Button(
    f1, 
    text='Exit', 
    font=f, 
    command=lambda:root.destroy(), 
    bg='#D33532', 
    fg='white'
    )

total_bal = Button(
    f1,
    text='Total Balance',
    font=f,
    bg='#486966',
    command=totalBalance
)

total_spent = Button(
    f1,
    text='Total Spent',
    font=f,
    command=lambda:data.fetchRecord('select sum(ite)')
)

update_btn = Button(
    f1, 
    text='Update',
    bg='#C2BB00',
    command=update_record,
    font=f
)

del_btn = Button(
    f1, 
    text='Delete',
    bg='#BD2A2E',
    command=deleteRow,
    font=f
)

pie_chart_btn = Button(
    f1, 
    text='Pie Chart', 
    font=f, 
    command=show_pie_chart,
    bg='#C9D7DD',
    fg='white'
)

daily_spending_btn = Button(
    f1, 
    text='Daily Spending', 
    font=f, 
    command=show_daily_spending_chart,
    bg='#637A9F',
    fg='white'
)

# Grid placement
cur_date.grid(row=3, column=1, sticky=EW, padx=(10, 0))
daily_spending_btn.grid(row=3, column=3, sticky=EW, padx=(10, 0))
submit_btn.grid(row=0, column=2, sticky=EW, padx=(10, 0))
clr_btn.grid(row=1, column=2, sticky=EW, padx=(10, 0))
quit_btn.grid(row=3, column=2, sticky=EW, padx=(10, 0))
total_bal.grid(row=0, column=3, sticky=EW, padx=(10, 0))
update_btn.grid(row=1, column=3, sticky=EW, padx=(10, 0))
del_btn.grid(row=2, column=3, sticky=EW, padx=(10, 0))
pie_chart_btn.grid(row=2, column=2, sticky=EW, padx=(10, 0))

# Treeview widget
tv = ttk.Treeview(f2, columns=(1, 2, 3, 4), show='headings', height=8)
tv.pack(side="left")

# Add heading to treeview
tv.column(1, anchor=CENTER, stretch=NO, width=70)
tv.column(2, anchor=CENTER)
tv.column(3, anchor=CENTER)
tv.column(4, anchor=CENTER)
tv.heading(1, text="Serial no")
tv.heading(2, text="Item Name", )
tv.heading(3, text="Item Price")
tv.heading(4, text="Purchase Date")

# Binding treeview
tv.bind("<ButtonRelease-1>", select_record)

# Style for treeview
style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

# Vertical scrollbar
scrollbar = Scrollbar(f2, orient='vertical')
scrollbar.configure(command=tv.yview)
scrollbar.pack(side="right", fill="y")
tv.config(yscrollcommand=scrollbar.set)

# Call function to fetch records
fetch_records()

# Run tkinter main loop
root.mainloop()