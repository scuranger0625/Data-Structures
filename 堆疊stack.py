#堆疊（Stack）是一種遵循後進先出（LIFO, Last In First Out）原則的資料結構。
#以下是使用 Python 中的列表（list）來實現堆疊的範例：
#堆疊的主要特性是元素的添加和移除都是在頂部進行的。
#使用列表來實現堆疊在 Python 中是一種常見且簡單的方法，但在實際應用中，也可以使用 collections.deque 來實現更高效的堆疊操作。


# 使用列表來實現堆疊
stack = []

# 推入元素到堆疊（Push operation）
stack.append(10)
stack.append(20)
stack.append(30)

# 現在 stack 是 [10, 20, 30]

# 彈出元素從堆疊（Pop operation）
last_element = stack.pop()  # 返回 30，stack 現在是 [10, 20]

# 檢查堆疊的頂部元素（Peek operation），不移除元素
top_element = stack[-1]  # 返回 20，stack 保持不變

# 檢查堆疊是否為空
is_empty = len(stack) == 0  # 返回 False

# 獲取堆疊的大小
size = len(stack)  # 返回 2

# 打印堆疊的所有元素
print("Stack elements:", stack)  # 輸出 Stack elements: [10, 20]
