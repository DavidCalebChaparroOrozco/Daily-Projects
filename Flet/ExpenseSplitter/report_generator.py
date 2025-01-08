import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_excel_report(expenses, filename='report.xlsx'):
    data = {
        'Description': [],
        'Amount': [],
        'Participants': []
    }
    
    for expense in expenses:
        data['Description'].append(expense.description)
        data['Amount'].append(expense.amount)
        data['Participants'].append(', '.join(expense.participants))

    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

def generate_pdf_report(expenses, filename='report.pdf'):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    c.drawString(100, height - 50, "Expense Report")
    
    y_position = height - 100
    for expense in expenses:
        c.drawString(100, y_position, f"{expense.description}: ${expense.amount} - Participants: {', '.join(expense.participants)}")
        y_position -= 20
    
    c.save()
