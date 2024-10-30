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

    def remove_rows(self, rows, output_path=None):
        """
        Removes specified rows from the Excel file.

        Parameters:
            rows (list): List of row indices to remove.
            output_path (str): Path to save the modified file.
                               If None, overwrites the original file.
        """
        try:
            df = pd.read_excel(self.file_path)
            df = df.drop(rows)
            save_path = output_path if output_path else self.file_path
            df.to_excel(save_path, index=False)
            print(f"Rows {rows} removed. File saved at {save_path}.")
        except Exception as e:
            print(f"Error removing rows: {e}")

    def read_file(self):
        """
        Reads the Excel file into a DataFrame.

        Returns:
            pd.DataFrame: DataFrame containing the Excel file data.
        """
        try:
            df = pd.read_excel(self.file_path)
            return df
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return None

    def export_distinct_values(self, output_path):
        """
        Exports the distinct values of each column in the Excel file to a CSV file.

        Parameters:
            output_path (str): Path to save the output CSV file with distinct values.
        """
        try:
            df = pd.read_excel(self.file_path)
            distinct_values = {column: df[column].dropna().unique().tolist() for column in df.columns}
            distinct_df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in distinct_values.items()]))
            distinct_df.to_csv(output_path, index=False)
            print(f"Distinct values for each column exported to {output_path}.")
        except Exception as e:
            print(f"Error exporting distinct values: {e}")
