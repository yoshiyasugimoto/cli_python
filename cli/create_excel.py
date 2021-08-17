from openpyxl import Workbook

def create_excel():
    wb = Workbook()
    
    wb.save("Mysheet.xlsx")

if __name__== "__main__":
    create_excel()