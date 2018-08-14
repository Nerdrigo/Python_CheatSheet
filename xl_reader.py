import xlrd

def read_xl(xl_file):
	'''
    This function has no purpose, it it only intended to remind me of how
    to read values from an excell sheet 
    '''

    #Opening xl file
    workbook = xlrd.open_workbook(xl_file)

    #Selecting sheet
    sheet = workbook.sheet_by_name('CLIENTES')

    #Getting number of rows
    num_rows = sheet.nrows

    #Getting cell value, 0-indexed: (row,col)
	value = sheet.cell_value(4,2) 