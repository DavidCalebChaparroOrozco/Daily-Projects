# Importing necessary libraries
import pandas as pd

class DataModel:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_excel(file_path)

    def get_data(self):
        return self.data