'''
Created on May 18, 2018

@author: aranjan
'''
import xlrd
ExcelFileName= 'Data.xlsx'
workbook = xlrd.open_workbook(ExcelFileName)
worksheet = workbook.sheet_by_name("Sheet1") # We need to read the data 
#from the Excel sheet named "Sheet1"

num_rows = worksheet.nrows  #Number of Rows
num_cols = worksheet.ncols  #Number of Columns

 # read a row
print (worksheet.row_values(0))

# read a cell
cell = worksheet.cell(0,0)
print (cell)
print (cell.value)
 # read a row slice
print (worksheet.row_slice(rowx=0,start_colx=0,end_colx=2))


result_data =[]
for curr_row in range(0, num_rows, 1):
        row_data = []

        for curr_col in range(0, num_cols, 1):
            data = worksheet.cell_value(curr_row, curr_col) # Read the data in the current cell
            #print(data)
            row_data.append(data)

        result_data.append(row_data)

