import xlrd

filename = "E:\\PythonMaster\\Day101-150\\userID.xls"
'''获取单元格的数据'''
def readExcel(rowValue,colValue):
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_name("Sheet1")
    # cell = sheet.row_slice(1,0,3)  #获取指定行的某几列的cell对象
    # cell = sheet.col_slice(0,0,3) #获取指定列的某几行的cell对象。
    # print(cell)
    return sheet.cell_value(rowValue,colValue)

'''
获取sheel所有数据
sheet.nrows,sheet.ncols:获取行数，列数
sheet.row_values:获取整行的值
sheet.col_values:获取整列的值
'''
def readAll():
    rows = []
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_name("Sheet1")
    for row in range(1,sheet.nrows):
        rows.append(list(sheet.row_values(row,0,sheet.ncols)))
    return rows

if __name__ == '__main__':
    print(readExcel(1,0))
