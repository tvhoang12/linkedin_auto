import pandas as pd
from visa import solve  # Import hàm solve từ file visa.py

# Đọc file Excel
file_path = "D:\\sourceCode\\Python\\linkedin\\NTQ.xlsx"  # Đường dẫn file
xls = pd.ExcelFile(file_path)

# Đọc sheet đầu tiên
df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])

# Chuyển dữ liệu từ cột 'Key' và 'Value' thành dictionary
data_dict = dict(zip(df["Key"], df["Value"]))

# Giải nén dictionary thành các biến động và truyền vào hàm solve
solve(**data_dict)