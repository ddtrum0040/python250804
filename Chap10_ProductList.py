import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path 

# DB파일이 없으면 만들고 있다면 접속한다. 
db_path = "ProductList.db"
con = sqlite3.connect(db_path)
cur = con.cursor()
if not os.path.exists(db_path):
    cur.execute(
        "CREATE TABLE Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);")
    con.commit()

# 디자인 파일을 로딩
form_class = uic.loadUiType("Chap10_ProductList.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 초기값 셋팅 
        self.id = 0 
        self.name = ""
        self.price = 0 

        # QTableWidget의 컬럼폭 셋팅하기 
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        # QTableWidget의 헤더 셋팅하기
        self.tableWidget.setHorizontalHeaderLabels(["제품ID","제품명", "가격"])
        # 탭키로 네비게이션 금지 
        self.tableWidget.setTabKeyNavigation(False)
        # 엔터키를 클릭하면 다음 컨트롤로 이동하는 경우 
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        # 더블클릭 시그널 처리
        self.tableWidget.doubleClicked.connect(self.doubleClick)
        # 초기 데이터 로딩
        self.getProduct()

    def addProduct(self):
        # 입력 파라메터 처리 
        self.name = self.prodName.text().strip()
        self.price = self.prodPrice.text().strip()
        if not self.name or not self.price.isdigit():
            QMessageBox.warning(self, "입력 오류", "제품명과 가격을 올바르게 입력하세요.")
            return
        cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", 
            (self.name, int(self.price)))
        con.commit()
        self.getProduct() 

    def updateProduct(self):
        # 업데이트 작업시 파라메터 처리 
        self.id  = self.prodID.text().strip()
        self.name = self.prodName.text().strip()
        self.price = self.prodPrice.text().strip()
        if not self.id.isdigit() or not self.name or not self.price.isdigit():
            QMessageBox.warning(self, "입력 오류", "제품ID, 제품명, 가격을 올바르게 입력하세요.")
            return
        cur.execute("UPDATE Products SET Name=?, Price=? WHERE id=?;", 
            (self.name, int(self.price), int(self.id)))
        con.commit()
        self.getProduct() 

    def removeProduct(self):
        # 삭제 파라메터 처리 
        self.id  = self.prodID.text().strip()
        if not self.id.isdigit():
            QMessageBox.warning(self, "입력 오류", "제품ID를 올바르게 입력하세요.")
            return
        cur.execute("DELETE FROM Products WHERE id=?;", (int(self.id),))
        con.commit()
        self.getProduct() 

    def getProduct(self):
        # 검색 결과를 보여주기 전에 기존 컨텐트를 삭제(헤더는 제외)
        cur.execute("SELECT * FROM Products;") 
        rows = cur.fetchall()
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.clearContents()
        for row_idx, item in enumerate(rows):
            int_as_strID = "{:10}".format(item[0])
            int_as_strPrice = "{:10}".format(item[2])
            # 각 열을 Item으로 생성해서 숫자를 오른쪽으로 정렬해서 출력한다. 
            itemID = QTableWidgetItem(int_as_strID) 
            itemID.setTextAlignment(Qt.AlignRight) 
            self.tableWidget.setItem(row_idx, 0, itemID)
            # 제품명은 그대로 출력한다. 
            self.tableWidget.setItem(row_idx, 1, QTableWidgetItem(item[1]))
            # 각 열을 Item으로 생성해서 숫자를 오른쪽으로 정렬해서 출력한다. 
            itemPrice = QTableWidgetItem(int_as_strPrice) 
            itemPrice.setTextAlignment(Qt.AlignRight) 
            self.tableWidget.setItem(row_idx, 2, itemPrice)

    def doubleClick(self):
        row = self.tableWidget.currentRow()
        self.prodID.setText(self.tableWidget.item(row, 0).text().strip())
        self.prodName.setText(self.tableWidget.item(row, 1).text())
        self.prodPrice.setText(self.tableWidget.item(row, 2).text().strip())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()




