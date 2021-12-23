import openpyxl
import os

os.chdir(r'C:\Users\ilidio\Documents\Python\Automate the boring stuff\ExcelWordPDF\READ_EXCEL')

workbook = openpyxl.load_workbook('example.xlsx')
print(type(workbook))

# To know the names of the sheets
print(workbook.get_sheet_names())

# To use a sheet that you know the name
sheet = workbook.get_sheet_by_name('Sheet1')

# Go to a exact cell at the sheet
cell = sheet['A1']

# To see the value in it
print(cell.value)

# To see a string of it
print(str(cell.value))
print(str(sheet['A1'].value))

# To make a loop over the cells
for i in range(1,8):
    print(i, sheet.cell(row=i, column = 2).value)