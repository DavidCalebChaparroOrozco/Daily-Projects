# Import necessary libraries
import os
import json
import statistics
from datetime import datetime, timedelta
from typing import List, Dict, Optional

# Class to represent a single sleep record

# Initialize a sleep record
class SleepRecord:
    def __init__(self, date: str, bedtime: str, wakeup_time: str, quality: int, 
                    dreams: bool, notes: str = ""):
        self.date = date
        self.bedtime = bedtime
        self.wakeup_time = wakeup_time
        self.quality = quality
        self.dreams = dreams
        self.notes = notes
        
    # Calculate sleep duration in hours
    @property
    def sleep_duration(self) -> float:
        bed_time = datetime.strptime(f"{self.date} {self.bedtime}", "%Y-%m-%d %H:%M")
        wake_time = datetime.strptime(f"{self.date} {self.wakeup_time}", "%Y-%m-%d %H:%M")
        
        # Handle case where bedtime is after midnight
        if wake_time < bed_time:
            wake_time += timedelta(days=1)
            
        return (wake_time - bed_time).total_seconds() / 3600
    
    # Convert record to dictionary for JSON storage
    def to_dict(self) -> Dict:
        return {
            "date": self.date,
            "bedtime": self.bedtime,
            "wakeup_time": self.wakeup_time,
            "quality": self.quality,
            "dreams": self.dreams,
            "notes": self.notes
        }

# Model class handling data operations for SleepAnalyzer
# Initialize the model with data file
class SleepAnalyzerModel:
    def __init__(self, data_file: str = "data/sleep_data.json"):
        self.data_file = data_file
        
        # Create data directory if it doesn't exist
        os.makedirs(os.path.dirname(data_file), exist_ok=True)
        
        # Create empty JSON file if it doesn't exist
        if not os.path.exists(data_file):
            with open(data_file, 'w') as f:
                json.dump([], f)
                
        self.records: List[SleepRecord] = []
        self.load_data()
    
    # Load sleep records from JSON file
    def load_data(self) -> None:
        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)
                self.records = [
                    SleepRecord(
                        record["date"],
                        record["bedtime"],
                        record["wakeup_time"],
                        record["quality"],
                        record["dreams"],
                        record.get("notes", "")
                    ) for record in data
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            self.records = []
    
    # Save sleep records to JSON file
    def save_data(self) -> None:
        with open(self.data_file, "w") as file:
            json.dump([record.to_dict() for record in self.records], file, indent=4)
    
    # Add a new sleep record
    def add_record(self, record: SleepRecord) -> None:
        self.records.append(record)
        self.save_data()
    
    # Get all sleep records
    def get_all_records(self) -> List[SleepRecord]:
        return sorted(self.records, key=lambda x: x.date, reverse=True)
    
    # Get sleep record by date
    def get_record_by_date(self, date: str) -> Optional[SleepRecord]:
        for record in self.records:
            if record.date == date:
                return record
        return None
    
    # Delete sleep record by date
    def delete_record(self, date: str) -> bool:
        for i, record in enumerate(self.records):
            if record.date == date:
                del self.records[i]
                self.save_data()
                return True
        return False
    
    # Calculate sleep statistics
    def get_statistics(self) -> Dict:
        if not self.records:
            return {}
        
        durations = [record.sleep_duration for record in self.records]
        qualities = [record.quality for record in self.records]
        dream_records = sum(1 for record in self.records if record.dreams)
        
        return {
            "total_records": len(self.records),
            "avg_duration": round(statistics.mean(durations), 2),
            "min_duration": round(min(durations), 2),
            "max_duration": round(max(durations), 2),
            "avg_quality": round(statistics.mean(qualities), 2),
            "dream_percentage": round((dream_records / len(self.records)) * 100, 2),
            "recommended_bedtime": self._calculate_recommended_bedtime(),
            "sleep_consistency": self._calculate_sleep_consistency()
        }
    
    # Calculate recommended bedtime based on average wakeup time and duration
    def _calculate_recommended_bedtime(self) -> Optional[str]:
        if not self.records:
            return None
            
        # Calculate average wakeup time
        wakeup_times = []
        for record in self.records:
            time_obj = datetime.strptime(record.wakeup_time, "%H:%M").time()
            wakeup_times.append(time_obj.hour * 60 + time_obj.minute)
        
        avg_wakeup = statistics.mean(wakeup_times)
        avg_duration = statistics.mean([record.sleep_duration for record in self.records])
        
        # Calculate recommended bedtime
        bedtime_minutes = avg_wakeup - (avg_duration * 60)
        if bedtime_minutes < 0:
            bedtime_minutes += 24 * 60
            
        hours = int(bedtime_minutes // 60)
        minutes = int(bedtime_minutes % 60)
        
        return f"{hours:02d}:{minutes:02d}"
    
    # Calculate sleep consistency score (0-100)
    def _calculate_sleep_consistency(self) -> float:
        if len(self.records) < 2:
            return 0.0
            
        durations = [record.sleep_duration for record in self.records]
        avg_duration = statistics.mean(durations)
        std_dev = statistics.stdev(durations)
        
        # Higher score for more consistent sleep durations
        consistency = 100 * (1 - (std_dev / avg_duration))
        return max(0.0, min(100.0, round(consistency, 2)))
    
    # Get records within a date range
    def get_records_in_range(self, start_date: str, end_date: str) -> List[SleepRecord]:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        return [
            record for record in self.records
            if start <= datetime.strptime(record.date, "%Y-%m-%d") <= end
        ]