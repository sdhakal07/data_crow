from ExcelUtility import excelutility as excel_util
file =excel_util.ExcelUtility(r"C:\Users\example.xlsx")
excel_util = file.convert_to_csv("Output\data.csv")
