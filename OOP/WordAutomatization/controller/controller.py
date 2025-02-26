from model.model import DataModel
from view.view import DocumentView, GraphView

class ReportController:
    def __init__(self, data_path, report_name):
        self.model = DataModel(data_path)
        self.view = DocumentView(report_name)

    # Generate a comprehensive report with tables and visualizations.
    def generate_report(self):
        data = self.model.get_data()

        # Add title and table
        self.view.add_paragraph("Work Hours Report", size=14, bold=True)
        self.view.add_table(data)

        # Add visualizations
        self.view.add_paragraph("Hours Worked Over Time", size=12, bold=True)
        image_stream = GraphView.plot_hours_worked_over_time(data)
        self.view.add_image(image_stream)

        self.view.add_paragraph("Total Hours Worked by Employee", size=12, bold=True)
        image_stream = GraphView.plot_total_hours_by_employee(data)
        self.view.add_image(image_stream)

        self.view.add_paragraph("Hours Worked by Client", size=12, bold=True)
        image_stream = GraphView.plot_hours_distribution_by_client(data)
        self.view.add_image(image_stream)

        self.view.add_paragraph("Distribution of Hours Worked", size=12, bold=True)
        image_stream = GraphView.plot_hours_histogram(data)
        self.view.add_image(image_stream)

        self.view.add_paragraph("Hours Worked vs Date", size=12, bold=True)
        image_stream = GraphView.plot_scatter_hours_vs_date(data)
        self.view.add_image(image_stream)

        # Save the document
        self.view.save()