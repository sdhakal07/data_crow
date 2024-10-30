import pandas as pd


class ExcelUtility:
    def __init__(self, file_path):
        """
        Initializes the ExcelUtility class with a file path.
        """
        self.file_path = file_path

    def convert_to_csv(self, output_path):
        """
        Converts the Excel file to CSV format.

        Parameters:
            output_path (str): Path to save the output CSV file.
        """
        try:
            df = pd.read_excel(self.file_path)
            df.to_csv(output_path, index=False)
            print(f"Excel file converted to CSV and saved at {output_path}.")
        except Exception as e:
            print(f"Error converting Excel to CSV: {e}")

