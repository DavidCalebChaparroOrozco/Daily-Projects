# Import necessary libraries
import re
from collections import defaultdict

# Extracts day titles from a README.md file and saves them to a .txt file.
# Handles complex formats with emojis and detects duplicate days.    
def extract_day_titles(readme_path, output_file):
    day_titles = []
    day_counts = defaultdict(int)
    # Improved pattern that accepts emojis and different formats
    pattern = r'^[\*️⃣]*\s*[^\w]*(?:Day|Día)\s+\d+:.*$'
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if re.match(pattern, line, re.UNICODE | re.IGNORECASE):
                    # Extract day number
                    day_match = re.search(r'(?:Day|Día)\s+(\d+):', line, re.IGNORECASE)
                    if day_match:
                        day_num = int(day_match.group(1))
                        day_counts[day_num] += 1
                    
                    # Advanced title cleanup

                    # Remove asterisk
                    clean_title = re.sub(r'^\*\s*', '', line)  
                    # Normalize spaces
                    clean_title = re.sub(r'\s+', ' ', clean_title)  
                    day_titles.append(clean_title)
        
        # Detectar días repetidos
        repeated_days = [day for day, count in day_counts.items() if count > 1]
        if repeated_days:
            print("\n⚠️ Repeated days found:")
            for day in sorted(repeated_days):
                print(f"Day {day} appears {day_counts[day]} times")
        
        # Save the titles
        with open(output_file, 'w', encoding='utf-8') as out_file:
            for title in day_titles:
                out_file.write(title + '\n')
                
        print(f"\n{len(day_titles)} titles have been saved to {output_file}")
        return True
    
    except FileNotFoundError:
        print(f"Error: File {readme_path} not found")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

# Find missing and duplicate days in titles.
# Handles all formats with emojis.
def find_missing_days(input_file="DayTitles.txt", max_day=500):
    existing_days = defaultdict(int)
    day_entries = defaultdict(list)

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                # Match lines with "Day" followed by a number
                match = re.search(r'(?:.*?)(?:Day|Día)\s+(\d+):', line, re.IGNORECASE)
                if match:
                    day_num = int(match.group(1))
                    existing_days[day_num] += 1
                    day_entries[day_num].append((line_num, line))
        
        # Detect repeated days (recheck just in case)
        repeated_days = {day: count for day, count in existing_days.items() if count > 1}
        if repeated_days:
            print("\n🔍 Repeating days found in DayTitles.txt:")
            for day, count in sorted(repeated_days.items()):
                print(f"\nDay {day} (appears {count} times):")
                for entry in day_entries[day]:
                    print(f"Line {entry[0]}: {entry[1]}".center(50))
        
        # Find missing days
        missing_days = sorted(set(range(1, max_day + 1)) - set(existing_days.keys()))
        
        if missing_days:
            print(f"\n❌ Missing days from 1 to {max_day}:")
            # Group consecutive days
            grouped = []
            if missing_days:
                start = missing_days[0]
                prev = start
                for day in missing_days[1:]:
                    if day != prev + 1:
                        grouped.append(f"{start}-{prev}" if start != prev else str(start))
                        start = day
                    prev = day
                grouped.append(f"{start}-{prev}" if start != prev else str(start))
            
            print(", ".join(grouped))
            print(f"\nTotal missing days: {len(missing_days)}")
        else:
            print(f"\n✅ There are no missing days in the sequence from 1 to {max_day}.")
        
        return missing_days, repeated_days
    
    except FileNotFoundError:
        print(f"Error: File {input_file} not found")
        return [], {}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return [], {}

def main():
    readme_file = "../README.md"
    output_file = "DayTitles.txt"
    
    print("🔍 Processing README.md file...")
    if extract_day_titles(readme_file, output_file):
        print("\n🔎 Searching for missing and repeating days...")
        missing_days, repeated_days = find_missing_days(output_file)
        
        # Save report
        with open("DayAnalysisReport.txt", 'w', encoding='utf-8') as report:
            report.write("Day Analysis\n\n")
            
            if missing_days:
                report.write(f"MISSING DAYS (Total: {len(missing_days)}):\n")
                report.write(", ".join(map(str, missing_days)) + "\n\n")
            else:
                report.write("✅ There are no missing days\n\n")
            
            if repeated_days:
                report.write("REPEATING DAYS:\n")
                for day, count in sorted(repeated_days.items()):
                    report.write(f"- Day {day} (appears {count} times)\n")
            else:
                report.write("✅ There are no repeated days\n")
        
        print("\n📝 The full report has been saved to DayAnalysisReport.txt")

if __name__ == "__main__":
    main()