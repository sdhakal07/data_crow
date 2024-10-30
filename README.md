# ExcelUtility Module
This module provides utility functions for handling Excel files, including converting them to CSV, removing rows, and reading data into a pandas DataFrame.

# Features
Convert Excel files to CSV format
Remove specified rows from an Excel file
Read Excel data into a DataFrame for further processing


# Class & Methods
## ExcelUtility
Methods:

convert_to_csv(output_path): Converts the Excel file to CSV and saves it to the specified location.

remove_rows(rows, output_path=None): Removes specified rows from the Excel file and saves it. If no output path is specified, it overwrites the original file.

read_file(): Reads the Excel file into a pandas DataFrame.


# Usage Example
python
from excel_utility import ExcelUtility

## Initialize ExcelUtility with the path to your Excel file
excel_util = ExcelUtility("data.xlsx")

## Convert Excel file to CSV
excel_util.convert_to_csv("data.csv")

## Remove specific rows (e.g., first 3 rows) and save to a new file
excel_util.remove_rows([0, 1, 2], "modified_data.xlsx")

## Read the Excel file into a DataFrame
df = excel_util.read_file()
print(df.head())

