import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QLabel,
    QMessageBox
)
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

class ProductManager(QWidget):
    def __init__(self):
        super().__init__()
        self.init_db()
        self.init_ui()
        self.load_data()

    def init_db(self):
        self.conn = sqlite3.connect('products.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS MyProducts (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME TEXT NOT NULL,
                PRICE INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def init_ui(self):
        self.setWindowTitle('전자제품 관리 시스템')
        
        # 전체 배경색 설정
        self.setStyleSheet("""
            QWidget {
                background-color: #F8F6F4;
            }
            QLineEdit {
                background-color: #FFFFFF;
                border: 1px solid #D3D3D3;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton {
                background-color: #E8D9FF;
                border: none;
                border-radius: 5px;
                padding: 6px 12px;
                color: #444444;
            }
            QPushButton:hover {
                background-color: #D0B8FF;
            }
            QTableWidget {
                background-color: #FFFFFF;
                alternate-background-color: #F5F5F5;
                border: 1px solid #D3D3D3;
            }
            QHeaderView::section {
                background-color: #FFE4E1;
                padding: 4px;
                border: none;
                font-weight: bold;
            }
            QLabel {
                color: #555555;
            }
        """)

        layout = QVBoxLayout()

        # 입력 폼
        form_layout = QHBoxLayout()
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText('제품명')
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText('가격')
        
        form_layout.addWidget(QLabel('제품명:'))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel('가격:'))
        form_layout.addWidget(self.price_input)
        
        layout.addLayout(form_layout)

        # 버튼들
        btn_layout = QHBoxLayout()
        
        self.add_btn = QPushButton('추가')
        self.add_btn.clicked.connect(self.add_product)
        
        self.update_btn = QPushButton('수정')
        self.update_btn.clicked.connect(self.update_product)
        
        self.delete_btn = QPushButton('삭제')
        self.delete_btn.clicked.connect(self.delete_product)
        
        self.search_btn = QPushButton('검색')
        self.search_btn.clicked.connect(self.search_product)
        
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.update_btn)
        btn_layout.addWidget(self.delete_btn)
        btn_layout.addWidget(self.search_btn)
        
        layout.addLayout(btn_layout)

        # 테이블 위젯
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['ID', '제품명', '가격'])
        self.table.cellClicked.connect(self.cell_clicked)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def load_data(self, query="SELECT * FROM MyProducts"):
        self.table.clearContents()
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        
        self.table.setRowCount(len(results))
        for i, row in enumerate(results):
            for j, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                self.table.setItem(i, j, item)

    def add_product(self):
        name = self.name_input.text()
        price = self.price_input.text()
        
        if name and price:
            try:
                price = int(price)
                self.cursor.execute(
                    "INSERT INTO MyProducts (NAME, PRICE) VALUES (?, ?)",
                    (name, price)
                )
                self.conn.commit()
                self.load_data()
                self.clear_inputs()
                QMessageBox.information(self, '성공', '제품이 추가되었습니다.')
            except ValueError:
                QMessageBox.warning(self, '오류', '가격은 숫자로 입력해주세요.')
        else:
            QMessageBox.warning(self, '오류', '모든 필드를 입력해주세요.')

    def update_product(self):
        selected = self.table.currentRow()
        if selected >= 0:
            product_id = self.table.item(selected, 0).text()
            name = self.name_input.text()
            price = self.price_input.text()
            
            if name and price:
                try:
                    price = int(price)
                    self.cursor.execute(
                        "UPDATE MyProducts SET NAME=?, PRICE=? WHERE ID=?",
                        (name, price, product_id)
                    )
                    self.conn.commit()
                    self.load_data()
                    self.clear_inputs()
                    QMessageBox.information(self, '성공', '제품이 수정되었습니다.')
                except ValueError:
                    QMessageBox.warning(self, '오류', '가격은 숫자로 입력해주세요.')
            else:
                QMessageBox.warning(self, '오류', '모든 필드를 입력해주세요.')
        else:
            QMessageBox.warning(self, '오류', '수정할 제품을 선택해주세요.')

    def delete_product(self):
        selected = self.table.currentRow()
        if selected >= 0:
            product_id = self.table.item(selected, 0).text()
            reply = QMessageBox.question(self, '확인', 
                '정말 삭제하시겠습니까?',
                QMessageBox.Yes | QMessageBox.No)
                
            if reply == QMessageBox.Yes:
                self.cursor.execute("DELETE FROM MyProducts WHERE ID=?", (product_id,))
                self.conn.commit()
                self.load_data()
                self.clear_inputs()
                QMessageBox.information(self, '성공', '제품이 삭제되었습니다.')
        else:
            QMessageBox.warning(self, '오류', '삭제할 제품을 선택해주세요.')

    def search_product(self):
        search_text = self.name_input.text()
        if search_text:
            query = f"SELECT * FROM MyProducts WHERE NAME LIKE '%{search_text}%'"
            self.load_data(query)
        else:
            self.load_data()

    def cell_clicked(self, row, column):
        self.name_input.setText(self.table.item(row, 1).text())
        self.price_input.setText(self.table.item(row, 2).text())

    def clear_inputs(self):
        self.name_input.clear()
        self.price_input.clear()

    def closeEvent(self, event):
        self.conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProductManager()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec_())