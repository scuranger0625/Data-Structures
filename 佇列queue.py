from collections import deque

# 創建一個佇列
queue = deque()

# 插入元素到佇列的尾部（Enqueue operation）
# 使用 append() 方法將元素添加到佇列的尾部。
queue.append('a')
queue.append('b')
queue.append('c')

# 現在 queue 是 deque(['a', 'b', 'c'])

# 從佇列的頭部移除元素（Dequeue operation）
# 使用 popleft() 方法從佇列的頭部移除元素並返回該元素。
first_element = queue.popleft()  # 返回 'a'，queue 現在是 deque(['b', 'c'])

# 檢查佇列的頭部元素（Peek operation），不移除元素
# 通過 queue[0] 來查看佇列的頭部元素而不移除它。
front_element = queue[0]  # 返回 'b'，queue 保持不變

# 檢查佇列是否為空
# 通過檢查佇列的長度是否為零來判斷佇列是否為空。
is_empty = len(queue) == 0  # 返回 False

# 獲取佇列的大小
# 使用 len(queue) 來獲取佇列中元素的數量。
size = len(queue)  # 返回 2

# 打印佇列的所有元素
print("Queue elements:", list(queue))  # 輸出 Queue elements: ['b', 'c']

# 重要事項：
# - 佇列的主要特性是先進先出（FIFO, First In First Out），
#   即最先進入佇列的元素最先被移除。
# - collections.deque 是實現佇列的高效工具，
#   它支援 O(1) 複雜度的頭部和尾部插入和刪除操作。
