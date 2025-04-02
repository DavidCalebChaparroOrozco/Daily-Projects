import csv
import json
from datetime import datetime
from typing import List, Dict, Optional
from model.model import SleepRecord, SleepAnalyzerModel
from view.view import SleepAnalyzerView

# Controller class coordinating model and view for SleepAnalyzer
class SleepAnalyzerController:
    
    # Initialize controller with model and view
    def __init__(self):
        self.model = SleepAnalyzerModel()
        self.view = SleepAnalyzerView()
    
    # Main application loop
    def run(self) -> None:
        while True:
            choice = self.view.display_main_menu()
            
            if choice == 1:
                self.add_record()
            elif choice == 2:
                self.view_all_records()
            elif choice == 3:
                self.view_statistics()
            elif choice == 4:
                self.search_records()
            elif choice == 5:
                self.delete_record()
            elif choice == 6:
                self.export_data()
            elif choice == 0:
                print("\nThank you for using SleepAnalyzer. Goodbye!")
                break
    
    # Add a new sleep record
    def add_record(self) -> None:
        record_data = self.view.get_sleep_record_input()
        
        # Check if record already exists for this date
        if self.model.get_record_by_date(record_data["date"]):
            self.view.display_message(
                "A record already exists for this date. Use edit instead.",
                is_error=True
            )
            return
        
        record = SleepRecord(
            record_data["date"],
            record_data["bedtime"],
            record_data["wakeup_time"],
            record_data["quality"],
            record_data["dreams"],
            record_data["notes"]
        )
        
        self.model.add_record(record)
        self.view.display_message("Sleep record added successfully!")
    
    # Display all sleep records
    def view_all_records(self) -> None:
        records = self.model.get_all_records()
        self.view.display_records(records)
    
    # Display sleep statistics
    def view_statistics(self) -> None:
        stats = self.model.get_statistics()
        self.view.display_statistics(stats)
    
    # Search and optionally edit records
    def search_records(self) -> None:
        criteria = self.view.get_search_criteria()
        
        if criteria["option"] == 0:
            return
        
        records = self._filter_records(criteria)
        
        if not records:
            self.view.display_message("No records found matching criteria.")
            return
        
        self.view.display_records(records)
        
        # Allow viewing/editing a specific record
        while True:
            date = input("\nEnter date to view details (or 'back' to return): ").strip()
            if date.lower() == "back":
                break
            
            record = next((r for r in records if r.date == date), None)
            if not record:
                self.view.display_message("No record found for that date.", is_error=True)
                continue
            
            self._handle_record_details(record)
    
    # Filter records based on search criteria
    def _filter_records(self, criteria: Dict) -> List[SleepRecord]:
        all_records = self.model.get_all_records()
        
        if criteria["option"] == 1:  # Date range
            return [
                r for r in all_records
                if criteria["start_date"] <= r.date <= criteria["end_date"]
            ]
        elif criteria["option"] == 2:  # Min duration
            return [r for r in all_records if r.sleep_duration >= criteria["min_duration"]]
        elif criteria["option"] == 3:  # Min quality
            return [r for r in all_records if r.quality >= criteria["min_quality"]]
        elif criteria["option"] == 4:  # Dreams only
            return [r for r in all_records if r.dreams]
        
        return []
    
    # Handle viewing and editing a specific record
    def _handle_record_details(self, record: SleepRecord) -> None:
        while True:
            self.view.display_record_details(record)
            
            action = input("\nEdit this record? (y/n): ").strip().lower()
            if action != "y":
                break
            
            updates = self.view.prompt_edit_record(record)
            if not updates:
                self.view.display_message("No changes made.")
                break
            
            # Create updated record
            new_record = SleepRecord(
                updates.get("date", record.date),
                updates.get("bedtime", record.bedtime),
                updates.get("wakeup_time", record.wakeup_time),
                updates.get("quality", record.quality),
                updates.get("dreams", record.dreams),
                updates.get("notes", record.notes)
            )
            
            # Delete old record and add updated one
            self.model.delete_record(record.date)
            self.model.add_record(new_record)
            
            self.view.display_message("Record updated successfully!")
            record = new_record  # Update reference for next iteration
    
    # Delete a sleep record
    def delete_record(self) -> None:
        date = self.view.get_record_date_to_delete()
        record = self.model.get_record_by_date(date)
        
        if not record:
            self.view.display_message("No record found for that date.", is_error=True)
            return
        
        self.view.display_record_details(record)
        confirm = input("\nAre you sure you want to delete this record? (y/n): ").strip().lower()
        
        if confirm == "y":
            if self.model.delete_record(date):
                self.view.display_message("Record deleted successfully!")
            else:
                self.view.display_message("Failed to delete record.", is_error=True)
        else:
            self.view.display_message("Deletion canceled.")
    
    # Export sleep data to file
    def export_data(self) -> None:
        format_choice = self.view.get_export_format()
        
        if format_choice == 0:
            return
        
        records = self.model.get_all_records()
        if not records:
            self.view.display_message("No records to export.", is_error=True)
            return
        
        default_name = f"sleep_data_{datetime.now().strftime('%Y%m%d')}"
        
        if format_choice == 1:  # CSV
            filename = self.view.get_filename(f"{default_name}.csv")
            self._export_to_csv(records, filename)
        elif format_choice == 2:  # JSON
            filename = self.view.get_filename(f"{default_name}.json")
            self._export_to_json(records, filename)
        elif format_choice == 3:  # Text
            filename = self.view.get_filename(f"{default_name}.txt")
            self._export_to_text(records, filename)
        
        self.view.display_export_success(filename)
    
    # Export records to CSV file
    def _export_to_csv(self, records: List[SleepRecord], filename: str) -> None:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Date", "Bedtime", "Wakeup Time", "Duration (h)", 
                "Quality", "Dreams", "Notes"
            ])
            
            for record in records:
                writer.writerow([
                    record.date,
                    record.bedtime,
                    record.wakeup_time,
                    f"{record.sleep_duration:.2f}",
                    record.quality,
                    "Yes" if record.dreams else "No",
                    record.notes
                ])
    
    # Export records to JSON file
    def _export_to_json(self, records: List[SleepRecord], filename: str) -> None:
        with open(filename, "w") as file:
            json.dump([record.to_dict() for record in records], file, indent=4)
    
    # Export records to formatted text file
    def _export_to_text(self, records: List[SleepRecord], filename: str) -> None:
        with open(filename, "w") as file:
            file.write("SLEEP RECORDS REPORT\n")
            file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            file.write(f"Total records: {len(records)}\n\n")
            file.write("=" * 80 + "\n")
            
            stats = self.model.get_statistics()
            if stats:
                file.write("\nSTATISTICS:\n")
                file.write(f"Average sleep duration: {stats['avg_duration']} hours\n")
                file.write(f"Average quality: {stats['avg_quality']}/5\n")
                file.write(f"Dream recall: {stats['dream_percentage']}%\n")
                file.write(f"Recommended bedtime: {stats['recommended_bedtime']}\n")
                file.write(f"Sleep consistency: {stats['sleep_consistency']}/100\n")
                file.write("\n" + "=" * 80 + "\n")
            
            file.write("\nINDIVIDUAL RECORDS:\n\n")
            for record in records:
                file.write(f"Date: {record.date}\n")
                file.write(f"Bedtime: {record.bedtime} | Wakeup: {record.wakeup_time}\n")
                file.write(f"Duration: {record.sleep_duration:.2f} hours\n")
                file.write(f"Quality: {'★' * record.quality + '☆' * (5 - record.quality)}\n")
                file.write(f"Dreams: {'Remembered' if record.dreams else 'None'}\n")
                file.write(f"Notes: {record.notes}\n")
                file.write("-" * 60 + "\n")