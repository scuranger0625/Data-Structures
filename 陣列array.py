#在 Python 中，雖然內建的資料結構 list 可以用來實現類似於其他語言中的陣列，但如果想要使用真正的陣列結構，
#可以使用 array 模組或 numpy 套件。這裡，我將展示如何使用 array 模組來創建和操作陣列。


import array

# 創建一個包含整數的陣列
int_array = array.array('i', [1, 2, 3, 4, 5])

# 創建一個包含浮點數的陣列
float_array = array.array('f', [1.1, 2.2, 3.3, 4.4])

# 訪問陣列中的元素
first_element = int_array[0]  # 訪問第一個元素，結果為 1

# 修改陣列中的元素
int_array[1] = 20  # 將第二個元素改為 20

# 添加元素到陣列末尾
int_array.append(6)  # int_array 現在是 array('i', [1, 20, 3, 4, 5, 6])

# 刪除陣列中的元素
int_array.remove(20)  # 移除值為 20 的元素，結果為 array('i', [1, 3, 4, 5, 6])

# 陣列長度
length = len(int_array)  # 返回 5

# 陣列切片
subarray = int_array[1:3]  # 返回 array('i', [3, 4])

# 檢查元素是否在陣列中
is_in_array = 3 in int_array  # 返回 True

# 迭代陣列
for number in int_array:
    print(number)
