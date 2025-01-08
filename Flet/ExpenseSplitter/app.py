import flet as ft
from expenses import ExpenseManager
from report_generator import generate_excel_report, generate_pdf_report

def main(page: ft.Page):
    page.title = "Expense Splitter"
    
    expense_manager = ExpenseManager()
    
    # UI Elements
    description_input = ft.TextField(label="Expense Description")
    amount_input = ft.TextField(label="Amount")  # Removed type specification
    participants_input = ft.TextField(label="Participants (comma-separated)")
    
    output_area = ft.Column()

    def add_expense(e):
        description = description_input.value
        amount = float(amount_input.value)
        participants = [p.strip() for p in participants_input.value.split(',')]
        
        expense_manager.add_expense(description, amount, participants)
        
        output_area.controls.append(ft.Text(f"Added: {description} - ${amount} shared by {', '.join(participants)}"))
        
        description_input.value = ""
        amount_input.value = ""
        participants_input.value = ""
        
        page.update()

    def show_report(e):
        owed_summary = expense_manager.calculate_owed()
        
        output_area.controls.append(ft.Text("Owed Summary:"))
        
        for person, amount in owed_summary.items():
            output_area.controls.append(ft.Text(f"{person}: ${amount:.2f}"))
        
        page.update()

    def export_excel(e):
        generate_excel_report(expense_manager.get_expenses())
    
    def export_pdf(e):
        generate_pdf_report(expense_manager.get_expenses())
    
    page.add(
        description_input,
        amount_input,
        participants_input,
        ft.ElevatedButton("Add Expense", on_click=add_expense),
        ft.ElevatedButton("Show Owed Summary", on_click=show_report),
        ft.ElevatedButton("Export to Excel", on_click=export_excel),
        ft.ElevatedButton("Export to PDF", on_click=export_pdf),
        output_area,
    )

ft.app(target=main)
