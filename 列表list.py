# 創建一個包含數字的列表
numbers = [1, 2, 3, 4, 5]

# 創建一個包含字符串的列表
fruits = ["apple", "banana", "cherry"]

# 創建一個混合類型的列表
mixed_list = [1, "apple", 3.14, True]

# 訪問列表中的元素
first_fruit = fruits[0]  # 訪問第一個元素，結果為 "apple"

# 修改列表中的元素
fruits[1] = "blueberry"  # 將第二個元素改為 "blueberry"

# 添加元素到列表末尾
fruits.append("orange")  # fruits 現在是 ["apple", "blueberry", "cherry", "orange"]

# 刪除列表中的元素
del fruits[2]  # 刪除索引為 2 的元素，結果為 ["apple", "blueberry", "orange"]

# 列表長度
length = len(fruits)  # 返回 3

# 列表切片
sublist = numbers[1:4]  # 返回 [2, 3, 4]

# 檢查元素是否在列表中
is_in_list = "apple" in fruits  # 返回 True

# 迭代列表
for fruit in fruits:
    print(fruit)
