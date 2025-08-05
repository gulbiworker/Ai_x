from predict import loaded_model, predict_apt_price
import xlwings as xw
def main():
    file_path = "../data/ex3_xlwing.xlsx"
    wb = xw.Book(file_path)
    ws = wb.sheets.active
    for line in range(2,5):
        year = ws.range('B2').value
        square = ws.range('C2').value
        floor = ws.range('D2').value
        pred = predict_apt_price(year, square, floor)
        ws.range('E'+str(line)).value = pred
    wb.save(file_path)
    wb.close


    if __name__=="__main__"