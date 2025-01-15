# Importing necessary libraries
import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Global variable to hold shooting data
shooting_data = {
    'Free Throws': 85,
    'Two-Point Shots': 50,
    'Three-Point Shots': 40
}

# Load shooting data from a JSON file.
def load_data_from_file(filename='shooting_data.json'):
    global shooting_data
    try:
        with open(filename, 'r') as f:
            shooting_data = json.load(f)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No previous data found. Starting with default values.")

# Save shooting data to a JSON file.
def save_data_to_file(filename='shooting_data.json'):
    with open(filename, 'w') as f:
        json.dump(shooting_data, f)
    print("Data saved successfully.")

# Import shooting data from a JSON or CSV file.
def import_data_from_file(filename='shooting_data.json'):
    global shooting_data
    try:
        if filename.endswith('.json'):
            with open(filename, 'r') as f:
                shooting_data = json.load(f)
            print("Data imported successfully from JSON.")
        elif filename.endswith('.csv'):
            df = pd.read_csv(filename)
            shooting_data = df.set_index('Shot Type')['Efficiency'].to_dict()
            print("Data imported successfully from CSV.")
        else:
            print("Unsupported file format. Please use .json or .csv.")
    except Exception as e:
        print(f"Error importing data: {e}")

# Display the main menu options.
def display_menu():
    print("\nWelcome to the Shooting Efficiency Application")
    print("1. View all shooting efficiencies")
    print("2. Add new shooting data")
    print("3. Modify existing shooting data")
    print("4. Visualize shooting efficiencies")
    print("5. Save data")
    print("6. Import data")
    print("7. Exit")
    print("=".center(50, "="))

# Display current shooting efficiencies.
def view_shooting_data():
    print("\nCurrent Shooting Efficiencies:")
    for shot_type, efficiency in shooting_data.items():
        print(f"{shot_type}: {efficiency}%")

# Add new shooting data.
def add_shooting_data():
    print("\nSelect the type of shot to add:")
    shot_types = list(shooting_data.keys())
    
    for index, shot_type in enumerate(shot_types, start=1):
        print(f"{index}. {shot_type}")
    
    choice = input("Enter the number of the shot type you want to add: ")
    
    try:
        choice = int(choice)
        if 1 <= choice <= len(shot_types):
            shot_type = shot_types[choice - 1]
            efficiency = input(f"Enter the shooting efficiency percentage for {shot_type}: ")
            
            efficiency = int(efficiency)
            if 0 <= efficiency <= 100:
                shooting_data[shot_type] = efficiency
                print(f"Added {shot_type} with {efficiency}% efficiency.")
            else:
                print("Please enter a valid percentage between 0 and 100.")
        else:
            print("Invalid choice! Please select a valid option.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Modify existing shooting data.
def modify_shooting_data():
    print("\nSelect the type of shot to modify:")
    shot_types = list(shooting_data.keys())
    
    for index, shot_type in enumerate(shot_types, start=1):
        print(f"{index}. {shot_type}")
        
    choice = input("Enter the number of the shot type you want to modify: ")
    
    try:
        choice = int(choice)
        if 1 <= choice <= len(shot_types):
            shot_type = shot_types[choice - 1]
            new_efficiency = input(f"Enter the new shooting efficiency for {shot_type}: ")
            
            new_efficiency = int(new_efficiency)
            if 0 <= new_efficiency <= 100:
                shooting_data[shot_type] = new_efficiency
                print(f"Updated {shot_type} to {new_efficiency}%.")
            else:
                print("Please enter a valid percentage between 0 and 100.")
        else:
            print("Invalid choice! Please select a valid option.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Visualize shooting efficiencies using a bar plot or other types.
def visualize_shooting_data():
    
    # Ask user for visualization type
    print("\nSelect visualization type:")
    print("1. Bar Plot")
    print("2. Line Chart")
    print("3. Pie Chart")
    
    choice = input("Enter your choice (1-3): ")
    
    shots = list(shooting_data.keys())
    percentages = list(shooting_data.values())

    if choice == '1':
        plt.figure(figsize=(10, 6))
        sns.barplot(x=shots, y=percentages, palette='viridis')
        plt.title('Shooting Efficiency by Shot Type', fontsize=16)
        plt.xlabel('Type of Shot', fontsize=14)
        plt.ylabel('Shooting Efficiency (%)', fontsize=14)
        plt.ylim(0, 100)
        
        for i in range(len(percentages)):
            plt.text(i, percentages[i] + 2, f'{percentages[i]}%', ha='center', fontsize=12)

        plt.tight_layout()
        plt.show()
        
    elif choice == '2':
        plt.figure(figsize=(10, 6))
        plt.plot(shots, percentages, marker='o')
        plt.title('Shooting Efficiency Over Time', fontsize=16)
        plt.xlabel('Type of Shot', fontsize=14)
        plt.ylabel('Shooting Efficiency (%)', fontsize=14)
        plt.ylim(0, 100)
        
        for i in range(len(percentages)):
            plt.text(i, percentages[i] + 2, f'{percentages[i]}%', ha='center', fontsize=12)

        plt.tight_layout()
        plt.show()

    elif choice == '3':
        plt.figure(figsize=(8, 8))
        plt.pie(percentages, labels=shots, autopct='%1.1f%%', startangle=140)
        plt.title('Shooting Efficiency Distribution', fontsize=16)
        
        plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
        plt.show()

# Calculate and display performance metrics.
def calculate_statistics():
    
    efficiencies = list(shooting_data.values())
    
    average_efficiency = sum(efficiencies) / len(efficiencies)
    
    best_performance = max(efficiencies)
    worst_performance = min(efficiencies)

    best_shot_type = [k for k, v in shooting_data.items() if v == best_performance]
    
    worst_shot_type = [k for k, v in shooting_data.items() if v == worst_performance]

    print("\nPerformance Metrics:")
    print(f"Average Shooting Efficiency: {average_efficiency:.2f}%")
    print(f"Best Performance: {best_performance}% ({', '.join(best_shot_type)})")
    print(f"Worst Performance: {worst_performance}% ({', '.join(worst_shot_type)})")

# Main function to run the application.
def main():
    
    load_data_from_file()
    
    while True:
        display_menu()
        
        choice = input("Select an option (1-7): ")
        
        if choice == '1':
            view_shooting_data()
            calculate_statistics()
        elif choice == '2':
            add_shooting_data()
        elif choice == '3':
            modify_shooting_data()
        elif choice == '4':
            visualize_shooting_data()
        elif choice == '5':
            save_data_to_file()
        elif choice == '6':
            filename = input("Enter the filename to import data from (e.g., shooting_data.json or data.csv): ")
            import_data_from_file(filename)
        elif choice == '7':
            save_data_to_file()  # Save before exiting
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
