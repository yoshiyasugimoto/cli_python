from openpyxl import Workbook, workbook

wb = workbook()

ws = wb.active

ws = wb.create_sheet("Mysheet")
wb.save("Mysheet.xlsx")