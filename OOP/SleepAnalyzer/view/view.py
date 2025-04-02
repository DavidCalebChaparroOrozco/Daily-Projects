from typing import List, Dict
from datetime import datetime
from model.model import SleepRecord

# View class handling all user interface for SleepAnalyzer
class SleepAnalyzerView:
    
    # Display main menu and get user choice
    def display_main_menu(self) -> int:
        print("=".center(50, "="))
        print(" SLEEP ANALYZER - MAIN MENU ".center(50, "="))
        print("=" * 50)
        print("1. Add New Sleep Record")
        print("2. View All Sleep Records")
        print("3. View Sleep Statistics")
        print("4. Search/Edit Records")
        print("5. Delete a Record")
        print("6. Export Data")
        print("0. Exit")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (0-6): "))
                if 0 <= choice <= 6:
                    return choice
                print("Please enter a number between 0 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    # Get input for a new sleep record
    def get_sleep_record_input(self) -> Dict:
        print("=".center(50, "="))
        print(" ADD NEW SLEEP RECORD ".center(50, "-"))
        print("=".center(50, "="))
        
        while True:
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        
        while True:
            bedtime = input("Enter bedtime (HH:MM): ")
            try:
                datetime.strptime(bedtime, "%H:%M")
                break
            except ValueError:
                print("Invalid time format. Please use HH:MM.")
        
        while True:
            wakeup_time = input("Enter wakeup time (HH:MM): ")
            try:
                datetime.strptime(wakeup_time, "%H:%M")
                break
            except ValueError:
                print("Invalid time format. Please use HH:MM.")
        
        while True:
            try:
                quality = int(input("Rate sleep quality (1-5, 5=best): "))
                if 1 <= quality <= 5:
                    break
                print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        dreams = input("Did you remember any dreams? (y/n): ").lower() == "y"
        notes = input("Additional notes (optional): ")
        
        return {
            "date": date,
            "bedtime": bedtime,
            "wakeup_time": wakeup_time,
            "quality": quality,
            "dreams": dreams,
            "notes": notes
        }
    
    # Display all sleep records in a table
    def display_records(self, records: List[SleepRecord]) -> None:
        if not records:
            print("\nNo sleep records found.")
            return
            
        print("=".center(50, "="))
        print(" SLEEP RECORDS ".center(100, "="))
        print("=".center(50, "="))
        print(f"{'Date':<12} {'Bedtime':<10} {'Wakeup':<10} {'Duration':<10} {'Quality':<8} {'Dreams':<8} {'Notes':<40}")
        print("=".center(50, "="))
        
        for record in records:
            duration = f"{record.sleep_duration:.2f}h"
            quality = "★" * record.quality + "☆" * (5 - record.quality)
            dreams = "✓" if record.dreams else "✗"
            notes = record.notes[:37] + "..." if len(record.notes) > 40 else record.notes
            
            print(f"{record.date:<12} {record.bedtime:<10} {record.wakeup_time:<10} "
                f"{duration:<10} {quality:<8} {dreams:<8} {notes:<40}")
        
        print("=" * 100)
    
    # Display sleep statistics
    def display_statistics(self, stats: Dict) -> None:
        if not stats:
            print("\nNo statistics available. Add some records first.")
            return
            
        print("=".center(50, "="))
        print(" SLEEP STATISTICS ".center(50, "="))
        print("=" * 50)
        
        print(f"\nTotal Records: {stats['total_records']}")
        print(f"\nAverage Sleep Duration: {stats['avg_duration']} hours")
        print(f"Shortest Sleep: {stats['min_duration']} hours")
        print(f"Longest Sleep: {stats['max_duration']} hours")
        print(f"\nAverage Sleep Quality: {stats['avg_quality']}/5")
        print(f"Dream Recall: {stats['dream_percentage']}% of nights")
        print(f"\nRecommended Bedtime: {stats['recommended_bedtime']}")
        print(f"Sleep Consistency Score: {stats['sleep_consistency']}/100")
        
        # Additional interpretation
        print("=".center(50, "="))
        print(" INTERPRETATION ".center(50, "-"))
        if stats['avg_duration'] < 7:
            print("⚠️ You might be sleep deprived (average < 7 hours)")
        elif stats['avg_duration'] > 9:
            print("⚠️ You might be oversleeping (average > 9 hours)")
        else:
            print("✅ Your average sleep duration is in the healthy range")
        
        if stats['sleep_consistency'] < 60:
            print("⚠️ Your sleep schedule is inconsistent (score < 60)")
        else:
            print("✅ Your sleep schedule is consistent")
        
        if stats['avg_quality'] < 3:
            print("⚠️ Your sleep quality could be improved")
        
        print("=" * 50)
    
    # Get search criteria for records
    def get_search_criteria(self) -> Dict:
        print("=".center(50, "="))
        print(" SEARCH RECORDS ".center(50, "-"))
        print("=".center(50, "="))
        
        print("\nSearch options:")
        print("1. By date range")
        print("2. By minimum sleep duration")
        print("3. By sleep quality")
        print("4. By dream recall")
        print("0. Cancel")
        
        while True:
            try:
                choice = int(input("\nEnter search option (0-4): "))
                if 0 <= choice <= 4:
                    break
                print("Please enter a number between 0 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        criteria = {"option": choice}
        
        if choice == 1:
            while True:
                start_date = input("Enter start date (YYYY-MM-DD): ")
                try:
                    datetime.strptime(start_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
            
            while True:
                end_date = input("Enter end date (YYYY-MM-DD): ")
                try:
                    datetime.strptime(end_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
            
            criteria["start_date"] = start_date
            criteria["end_date"] = end_date
        
        elif choice == 2:
            while True:
                try:
                    min_duration = float(input("Enter minimum sleep duration in hours: "))
                    if min_duration > 0:
                        criteria["min_duration"] = min_duration
                        break
                    print("Duration must be positive.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        elif choice == 3:
            while True:
                try:
                    min_quality = int(input("Enter minimum sleep quality (1-5): "))
                    if 1 <= min_quality <= 5:
                        criteria["min_quality"] = min_quality
                        break
                    print("Quality must be between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        elif choice == 4:
            criteria["dreams_only"] = True
        
        return criteria
    
    # Get date of record to delete
    def get_record_date_to_delete(self) -> str:
        print("=".center(50, "="))
        print(" DELETE RECORD ".center(50, "-"))
        print("=".center(50, "="))
        
        while True:
            date = input("Enter date of record to delete (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
                return date
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
    
    # Display a message to the user
    def display_message(self, message: str, is_error: bool = False) -> None:
        if is_error:
            print(f"\n❌ ERROR: {message}")
        else:
            print(f"\n✅ {message}")
    
    # Get export format choice from user
    def get_export_format(self) -> int:
        print("=".center(50, "="))
        print(" EXPORT DATA ".center(50, "-"))
        print("=".center(50, "="))
        
        print("\nExport options:")
        print("1. CSV format")
        print("2. JSON format")
        print("3. Text summary")
        print("0. Cancel")
        
        while True:
            try:
                choice = int(input("\nEnter export option (0-3): "))
                if 0 <= choice <= 3:
                    return choice
                print("Please enter a number between 0 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    # Get filename for export from user
    def get_filename(self, default: str) -> str:
        filename = input(f"\nEnter filename (default: {default}): ").strip()
        return filename if filename else default
    
    # Notify user of successful export
    def display_export_success(self, filename: str) -> None:
        print(f"\n✅ Data successfully exported to {filename}")
    
    # Display detailed view of a single record
    def display_record_details(self, record: SleepRecord) -> None:
        if not record:
            print("\nRecord not found.")
            return
            
        print("\n" + "=" * 50)
        print(" RECORD DETAILS ".center(50, "="))
        print("=" * 50)
        
        print(f"\nDate: {record.date}")
        print(f"Bedtime: {record.bedtime}")
        print(f"Wakeup Time: {record.wakeup_time}")
        print(f"Duration: {record.sleep_duration:.2f} hours")
        print(f"Quality: {'★' * record.quality + '☆' * (5 - record.quality)}")
        print(f"Dreams Remembered: {'Yes' if record.dreams else 'No'}")
        print(f"\nNotes:\n{record.notes}")
        
        print("=" * 50)
    
    # Prompt user to edit a record
    def prompt_edit_record(self, record: SleepRecord) -> Dict:
        print("\nLeave field blank to keep current value.")
        
        new_date = input(f"Date [{record.date}]: ").strip()
        new_bedtime = input(f"Bedtime [{record.bedtime}]: ").strip()
        new_wakeup = input(f"Wakeup time [{record.wakeup_time}]: ").strip()
        new_quality = input(f"Quality (1-5) [{record.quality}]: ").strip()
        new_dreams = input(f"Remember dreams? (y/n) [{'y' if record.dreams else 'n'}]: ").strip().lower()
        new_notes = input(f"Notes [{record.notes}]: ").strip()
        
        updates = {}
        
        if new_date:
            try:
                datetime.strptime(new_date, "%Y-%m-%d")
                updates["date"] = new_date
            except ValueError:
                print("Invalid date format. Keeping original.")
        
        if new_bedtime:
            try:
                datetime.strptime(new_bedtime, "%H:%M")
                updates["bedtime"] = new_bedtime
            except ValueError:
                print("Invalid time format. Keeping original.")
        
        if new_wakeup:
            try:
                datetime.strptime(new_wakeup, "%H:%M")
                updates["wakeup_time"] = new_wakeup
            except ValueError:
                print("Invalid time format. Keeping original.")
        
        if new_quality:
            try:
                quality = int(new_quality)
                if 1 <= quality <= 5:
                    updates["quality"] = quality
                else:
                    print("Quality must be 1-5. Keeping original.")
            except ValueError:
                print("Invalid quality. Keeping original.")
        
        if new_dreams in ("y", "n"):
            updates["dreams"] = new_dreams == "y"
        elif new_dreams:
            print("Invalid input for dreams. Keeping original.")
        
        if new_notes is not None:
            updates["notes"] = new_notes
        
        return updates