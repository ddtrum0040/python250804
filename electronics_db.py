import sqlite3
import random

class ElectronicsDB:
    def __init__(self, db_name="electronics.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_product(self, product_id, name, price):
        query = "INSERT INTO products (product_id, name, price) VALUES (?, ?, ?)"
        self.conn.execute(query, (product_id, name, price))
        self.conn.commit()

    def update_product(self, product_id, name=None, price=None):
        if name is not None and price is not None:
            query = "UPDATE products SET name=?, price=? WHERE product_id=?"
            self.conn.execute(query, (name, price, product_id))
        elif name is not None:
            query = "UPDATE products SET name=? WHERE product_id=?"
            self.conn.execute(query, (name, product_id))
        elif price is not None:
            query = "UPDATE products SET price=? WHERE product_id=?"
            self.conn.execute(query, (price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        query = "DELETE FROM products WHERE product_id=?"
        self.conn.execute(query, (product_id,))
        self.conn.commit()

    def select_products(self):
        query = "SELECT * FROM products"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def close(self):
        self.conn.close()

# 샘플 데이터 100개 생성 및 삽입
if __name__ == "__main__":
    db = ElectronicsDB()
    for i in range(1, 101):
        name = f"전자제품_{i}"
        price = round(random.uniform(10000, 1000000), 2)
        db.insert_product(i, name, price)
    print("샘플 데이터 100개가 삽입되었습니다.")
    # 예시: 전체 데이터 조회
    products = db.select_products()
    for p in products[:5]:  # 일부만 출력
        print(p)