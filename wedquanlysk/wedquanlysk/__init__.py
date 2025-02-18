import pymssql
import pyodbc

# Kiểm tra xem có thể kết nối với SQL Server hay không
try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=tin-loc;'
        'DATABASE=wedquanylsk;'
    )
    print("Kết nối SQL Server thành công!")
    conn.close()
except Exception as e:
    print(f"Lỗi kết nối SQL Server: {e}")

