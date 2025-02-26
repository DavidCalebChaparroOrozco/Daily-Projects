from controller.controller import ReportController

if __name__ == "__main__":
    report_controller = ReportController("data/Work_Hours_Report.xlsx", "report.docx")
    report_controller.generate_report()