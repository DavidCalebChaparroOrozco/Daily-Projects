# Import necessary libraries
import re
import json
import csv
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class ActivityTracker:
    def __init__(self):
        self.activity_logs = []
        self.activity_stats = defaultdict(list)
        
    # Add a new activity log and parse it for statistic
    def add_log(self, log_text):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.activity_logs.append({"timestamp": timestamp, "text": log_text})
        self._parse_log(log_text, timestamp)
        print("Activity log added successfully!")
        
    # Edit an existing activity log and update statistic
    def edit_log(self, log_index, new_text):
        if 0 <= log_index < len(self.activity_logs):
            old_text = self.activity_logs[log_index]["text"]
            timestamp = self.activity_logs[log_index]["timestamp"]
            
            self._remove_parsed_data(old_text, timestamp)
            self.activity_logs[log_index]["text"] = new_text
            self._parse_log(new_text, timestamp)
            print("Log updated successfully!")
        else:
            print("Invalid log index!")
            
    # Delete an activity log and its statistic
    def delete_log(self, log_index):
        if 0 <= log_index < len(self.activity_logs):
            log_text = self.activity_logs[log_index]["text"]
            timestamp = self.activity_logs[log_index]["timestamp"]
            
            del self.activity_logs[log_index]
            self._remove_parsed_data(log_text, timestamp)
            print("Log deleted successfully!")
        else:
            print("Invalid log index!")
            
    # Parse the log text to extract activity informatio
    def _parse_log(self, log_text, timestamp):
        exercise_patterns = [
            r'(?:did|completed|performed)\s(\d+\s*sets?\s*of\s*\d+\s*)?([\w\s]+?)(?:with|for|to|on|$)',
            r'(\d+\s*sets?\s*of\s*\d+\s*)?([\w\s]+?)(?:with|for|to|on|$)'
        ]
        
        found_exercises = set()
        
        for pattern in exercise_patterns:
            matches = re.finditer(pattern, log_text, re.IGNORECASE)
            for match in matches:
                exercise = match.group(2).strip().lower()
                # Clean up common prefixes/suffixes
                exercise = re.sub(r'^(sets?|reps?|of|the)\s+', '', exercise)
                exercise = exercise.strip()
                if exercise and len(exercise.split()) <= 4:  # Limit to reasonable length
                    found_exercises.add(exercise)
        
        # For time-based activities
        time_matches = re.findall(r'(\b\w+\b)\s(\d+)\s(minutes|min|hours|hrs|hr|seconds|sec)', log_text, re.IGNORECASE)
        for activity, amount, unit in time_matches:
            found_exercises.add(activity.lower())
        
        # Add all found exercises
        for exercise in found_exercises:
            # Standardize some common terms
            exercise = self._standardize_exercise_name(exercise)
            if exercise:
                self._add_activity(exercise, 1, timestamp)  # Using 1 as default duration

    # Clean and standardize exercise name
    def _standardize_exercise_name(self, name):
        # Remove numbers and set/rep info
        name = re.sub(r'\d+\s*(sets?|reps?|x|\*)', '', name).strip()
        # Remove common descriptors
        name = re.sub(r'\b(with|for|to|on|using|a|the)\b', '', name).strip()
        # Remove extra spaces
        name = ' '.join(name.split())
        # Specific replacements
        replacements = {
            'clap push': 'clap push-ups',
            'barbell row': 'barbell rows',
            'dumbbell shoulder press': 'shoulder press',
            'knee tuck jump': 'knee tuck jumps',
            'jump deadlift': 'jump deadlifts'
        }
        return replacements.get(name, name) if name else None
    
    # Helper method to add activity to stat
    def _add_activity(self, activity, amount, timestamp):
        if activity:
            self.activity_stats[activity].append({
                "duration": amount,
                "timestamp": timestamp
            })
    
    # Remove parsed data associated with a specific log
    def _remove_parsed_data(self, log_text, timestamp):
        # Get all activities that might be in this log
        possible_activities = set()
        
        # Check for time-based activities
        time_matches = re.findall(r'(\b\w+\b)\s(\d+)\s(minutes|min|hours|hrs|hr|seconds|sec)', log_text, re.IGNORECASE)
        possible_activities.update([m[0].lower() for m in time_matches])
        
        # Check for set/rep activities
        set_rep_matches = re.findall(r'(\d+)\s*sets?\s*(?:of\s*)?(\d+)?\s*(?:reps?)?\s*(\b\w+\b[\s\w]*)', log_text, re.IGNORECASE)
        possible_activities.update([m[2].strip().lower() for m in set_rep_matches])
        
        # Check for simple activities
        simple_matches = re.findall(r'(?:did|completed|performed)\s(\b[\w\s]+\b)', log_text, re.IGNORECASE)
        possible_activities.update([m.strip().lower() for m in simple_matches])
        
        # Remove all found activities with this timestamp
        for activity in possible_activities:
            if activity in self.activity_stats:
                self.activity_stats[activity] = [
                    entry for entry in self.activity_stats[activity] 
                    if entry["timestamp"] != timestamp
                ]
                if not self.activity_stats[activity]:
                    del self.activity_stats[activity]
    
    # Remove parsed data associated with a specific lo
    def _remove_parsed_data(self, log_text, timestamp):
        matches = re.findall(r'(\b\w+\b)\s(\d+)\s(minutes|min|hours|hrs|hr|seconds|sec)', log_text, re.IGNORECASE)
        
        for activity, amount, unit in matches:
            activity = activity.lower()
            if activity in self.activity_stats:
                self.activity_stats[activity] = [
                    entry for entry in self.activity_stats[activity] 
                    if entry["timestamp"] != timestamp
                ]
                if not self.activity_stats[activity]:
                    del self.activity_stats[activity]
    
    # Display summary statistics of all activitie
    def show_stats(self):
        print("\nActivity Statistics".center(50, '='))
        if not self.activity_stats:
            print("No activity data available.")
            return
            
        for activity, entries in self.activity_stats.items():
            total_duration = sum(entry["duration"] for entry in entries)
            avg_duration = total_duration / len(entries)
            print(f"{activity.capitalize()}:")
            print(f"  - Total: {total_duration} minutes")
            print(f"  - Average: {avg_duration:.1f} minutes per session")
            print(f"  - Sessions: {len(entries)}")
            print()
    
    # Display all activity log
    def show_logs(self):
        print("\nActivity Logs".center(50, '='))
        if not self.activity_logs:
            print("No logs available.")
            return
            
        for i, log in enumerate(self.activity_logs):
            print(f"{i}. [{log['timestamp']}] {log['text']}")

    # Export logs to a file (txt, csv, or json
    def export_logs(self, file_format='txt'):
        if not self.activity_logs:
            print("No logs to export!")
            return
            
        filename = f"activity_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{file_format}"
        
        try:
            if file_format == 'txt':
                with open(filename, 'w') as f:
                    for log in self.activity_logs:
                        f.write(f"[{log['timestamp']}] {log['text']}\n")
            elif file_format == 'csv':
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Timestamp', 'Activity Log'])
                    for log in self.activity_logs:
                        writer.writerow([log['timestamp'], log['text']])
            elif file_format == 'json':
                with open(filename, 'w') as f:
                    json.dump(self.activity_logs, f, indent=2)
            else:
                print("Invalid file format!")
                return
                
            print(f"Logs successfully exported to {filename}")
        except Exception as e:
            print(f"Error exporting logs: {e}")

    # Import logs from a file (txt, csv, or json
    def import_logs(self, filename):
        try:
            if filename.endswith('.txt'):
                with open(filename, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        parts = line.strip().split('] ')
                        if len(parts) == 2:
                            timestamp = parts[0][1:]
                            log_text = parts[1]
                            self.activity_logs.append({"timestamp": timestamp, "text": log_text})
                            self._parse_log(log_text, timestamp)
            elif filename.endswith('.csv'):
                with open(filename, 'r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        self.activity_logs.append({"timestamp": row['Timestamp'], "text": row['Activity Log']})
                        self._parse_log(row['Activity Log'], row['Timestamp'])
            elif filename.endswith('.json'):
                with open(filename, 'r') as f:
                    logs = json.load(f)
                    for log in logs:
                        self.activity_logs.append(log)
                        self._parse_log(log['text'], log['timestamp'])
            else:
                print("Unsupported file format!")
                return
                
            print(f"Logs successfully imported from {filename}")
        except Exception as e:
            print(f"Error importing logs: {e}")

    # Create visualizations of activity dat
    def visualize_activities(self):
        if not self.activity_stats:
            print("No activity data to visualize!")
            return
            
        # Prepare data for visualization
        activity_data = []
        for activity, entries in self.activity_stats.items():
            for entry in entries:
                date = entry['timestamp'].split()[0]
                activity_data.append({
                    'Activity': activity.capitalize(),
                    'Duration': entry['duration'],
                    'Date': date
                })
        
        data = pd.DataFrame(activity_data)
        
        if data.empty:
            print("No valid data for visualization!")
            return
            
        # Set up the visualization dashboard
        plt.figure(figsize=(15, 10))
        
        # Plot 1: Activity Distribution
        plt.subplot(2, 2, 1)
        sns.countplot(data=data, x='Activity', order=data['Activity'].value_counts().index)
        plt.title('Activity Frequency')
        plt.xticks(rotation=45)
        
        # Plot 2: Duration by Activity
        plt.subplot(2, 2, 2)
        sns.barplot(data=data, x='Activity', y='Duration', estimator=sum)
        plt.title('Total Duration by Activity')
        plt.xticks(rotation=45)
        
        # Plot 3: Time Series of Activities
        plt.subplot(2, 2, 3)
        data['Date'] = pd.to_datetime(data['Date'])
        time_series = data.groupby(['Date', 'Activity']).sum().unstack()
        time_series.plot(kind='area', stacked=True, ax=plt.gca())
        plt.title('Activity Over Time')
        plt.ylabel('Total Duration (minutes)')
        
        # Plot 4: Average Duration
        plt.subplot(2, 2, 4)
        sns.barplot(data=data, x='Activity', y='Duration')
        plt.title('Average Duration per Session')
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        plt.show()

    # Display a detailed dashboard for a specific activit
    def activity_dashboard(self, activity_name=None):
        if not self.activity_stats:
            print("No activity data available!")
            return
            
        if activity_name is None:
            print("\nAvailable activities:")
            for i, activity in enumerate(self.activity_stats.keys()):
                print(f"{i+1}. {activity.capitalize()}")
            try:
                choice = int(input("Select an activity number: ")) - 1
                activity_name = list(self.activity_stats.keys())[choice]
            except (ValueError, IndexError):
                print("Invalid selection!")
                return
                
        if activity_name not in self.activity_stats:
            print(f"No data found for activity: {activity_name}")
            return
            
        # Prepare data for the selected activity
        activity_data = []
        for entry in self.activity_stats[activity_name]:
            date = entry['timestamp'].split()[0]
            activity_data.append({
                'Date': date,
                'Duration': entry['duration']
            })
        
        data = pd.DataFrame(activity_data)
        data['Date'] = pd.to_datetime(data['Date'])
        
        # Set up the dashboard
        plt.figure(figsize=(15, 8))
        
        # Plot 1: Activity timeline
        plt.subplot(2, 2, 1)
        plt.plot(data['Date'], data['Duration'], 'o-')
        plt.title(f'{activity_name.capitalize()} Over Time')
        plt.ylabel('Duration (minutes)')
        plt.xticks(rotation=45)
        
        # Plot 2: Duration distribution
        plt.subplot(2, 2, 2)
        sns.histplot(data['Duration'], kde=True)
        plt.title('Duration Distribution')
        plt.xlabel('Duration (minutes)')
        
        # Plot 3: Weekly summary
        plt.subplot(2, 2, 3)
        weekly = data.resample('W', on='Date').sum()
        weekly.plot(kind='bar', ax=plt.gca())
        plt.title('Weekly Summary')
        plt.ylabel('Total Duration (minutes)')
        plt.xticks(rotation=45)
        
        # Plot 4: Statistics summary
        plt.subplot(2, 2, 4)
        stats = data['Duration'].describe().to_frame().T
        plt.table(cellText=stats.values,
                    colLabels=stats.columns,
                    rowLabels=['Statistics'],
                    loc='center')
        plt.axis('off')
        plt.title('Activity Statistics')
        
        plt.suptitle(f"{activity_name.capitalize()} Activity Dashboard", fontsize=16)
        plt.tight_layout()
        plt.show()

# Display the user menu with option
def display_menu():
    print("\nPhysical Activity Tracker Menu by David Caleb")
    print(" Select an option: ".center(50, '-'))
    print("1. Add new activity log")
    print("2. Edit existing log")
    print("3. Delete log")
    print("4. View all logs")
    print("5. View statistics")
    print("6. Export logs to file")
    print("7. Import logs from file")
    print("8. Visualize activities")
    print("9. Activity dashboard")
    print("10. Exit")
    
def main():
    tracker = ActivityTracker()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-10): ")
        
        if choice == "1":
            log_text = input("Enter your activity log (e.g., 'I walked 10 minutes and ran 5'): ")
            tracker.add_log(log_text)
            
        elif choice == "2":
            tracker.show_logs()
            try:
                log_index = int(input("Enter the log number to edit: "))
                new_text = input("Enter the new log text: ")
                tracker.edit_log(log_index, new_text)
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == "3":
            tracker.show_logs()
            try:
                log_index = int(input("Enter the log number to delete: "))
                tracker.delete_log(log_index)
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == "4":
            tracker.show_logs()
            
        elif choice == "5":
            tracker.show_stats()
            
        elif choice == "6":
            print("\nExport options:")
            print("1. Text file (.txt)")
            print("2. CSV file (.csv)")
            print("3. JSON file (.json)")
            export_choice = input("Select export format (1-3): ")
            if export_choice == "1":
                tracker.export_logs('txt')
            elif export_choice == "2":
                tracker.export_logs('csv')
            elif export_choice == "3":
                tracker.export_logs('json')
            else:
                print("Invalid choice!")
                
        elif choice == "7":
            filename = input("Enter filename to import (must be .txt, .csv, or .json): ")
            tracker.import_logs(filename)
            
        elif choice == "8":
            tracker.visualize_activities()
            
        elif choice == "9":
            tracker.activity_dashboard()
            
        elif choice == "10":
            print("Thank you for using the Physical Activity Tracker!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

if __name__ == "__main__":
    main()