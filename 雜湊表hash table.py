# 創建一個雜湊表（字典）
hash_table = {}

# 向雜湊表中添加鍵-值對（Insert operation）
# 使用鍵（key）來映射到值（value）。
hash_table['name'] = 'Alice'
hash_table['age'] = 30
hash_table['occupation'] = 'Engineer'

# 現在 hash_table 是 {'name': 'Alice', 'age': 30, 'occupation': 'Engineer'}

# 訪問雜湊表中的值（Access operation）
# 通過鍵來訪問對應的值。
name = hash_table['name']  # 返回 'Alice'
age = hash_table['age']    # 返回 30

# 更新雜湊表中的值
# 可以通過重新賦值來更新某個鍵對應的值。
hash_table['age'] = 31  # hash_table 現在是 {'name': 'Alice', 'age': 31, 'occupation': 'Engineer'}

# 刪除雜湊表中的鍵-值對（Delete operation）
# 使用 del 關鍵字刪除某個鍵及其對應的值。
del hash_table['occupation']  # hash_table 現在是 {'name': 'Alice', 'age': 31}

# 檢查鍵是否存在於雜湊表中
# 使用 in 關鍵字來檢查某個鍵是否存在。
has_name = 'name' in hash_table  # 返回 True
has_salary = 'salary' in hash_table  # 返回 False

# 獲取雜湊表的大小
# 使用 len() 函數來獲取雜湊表中鍵-值對的數量。
size = len(hash_table)  # 返回 2

# 迭代雜湊表
# 可以通過迭代來獲取所有的鍵和值。
for key, value in hash_table.items():
    print(f"{key}: {value}")

# 重要事項：
# - 雜湊表（字典）是一種以鍵-值對形式存儲數據的資料結構，
#   使用雜湊函數將鍵映射到存儲位置，以實現快速的查找。
# - 鍵必須是不可變的（例如，字符串、數字、元組），
#   而值可以是任何類型的數據。
# - 雜湊表的查找、插入和刪除操作平均時間複雜度為 O(1)，
#   這使其非常高效。
