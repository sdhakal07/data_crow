from ExcelUtility import excelutility as excel_util
file =excel_util.ExcelUtility(r"C:\Users\Leapfrog\Downloads\example_sheet.xlsx")
excel_util = file.convert_to_csv("Output\data.csv")
df = file.read_file()
print(df)

