# Import necessary libraries
import pandas as pd

# Extracts data from a CSV file.
def extract_data(file_path):
    """    
    Args:
        file_path: The path to the input CSV file.
    Returns:
        DataFrame: A pandas DataFrame containing the extracted data.
    """
    try:
        data = pd.read_csv(file_path)
        print("Data extracted successfully.")
        return data
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

# Transforms the DataFrame by filtering and adding a new column.
def transform_data(df):
    """    
    Args:
        df: The input DataFrame to transform.
        
    Returns:
        DataFrame: A transformed pandas DataFrame.
    """
    # Filter out employees with salary less than 60000
    filtered_df = df[df['salary'] >= 60000].copy()
    
    # Add a new column 'tax' which is 20% of salary
    filtered_df.loc[:, 'tax'] = filtered_df['salary'] * 0.20
    
    print("Data transformed successfully.")
    return filtered_df

# Loads the transformed DataFrame into a new CSV file.
def load_data(df, output_file_path):
    """    
    Args:
        df: The DataFrame to save.
        output_file_path: The path to save the output CSV file.
    """
    try:
        df.to_csv(output_file_path, index=False)
        print(f"Data loaded successfully into {output_file_path}.")
    except Exception as e:
        print(f"Error loading data: {e}")

def main():
    # Define file paths
    input_file_path = 'data/data.csv'
    output_file_path = 'output/processed_data.csv'
    
    # Execute the ETL pipeline
    data = extract_data(input_file_path)
    
    if data is not None:
        transformed_data = transform_data(data)
        load_data(transformed_data, output_file_path)

if __name__ == "__main__":
    main()