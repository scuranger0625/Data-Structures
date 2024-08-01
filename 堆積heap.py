import heapq

# 創建一個空的最小堆（Min Heap）
min_heap = []

# 插入元素到堆中（Push operation）
# 使用 heappush() 方法將元素添加到堆中，同時維護堆的性質。
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 1)

# 現在 min_heap 是 [1, 3, 8, 5]
# 堆的性質：每個節點的值小於或等於其子節點的值

# 移除並返回最小元素（Pop operation）
# 使用 heappop() 方法從堆中移除並返回最小元素。
min_element = heapq.heappop(min_heap)  # 返回 1，min_heap 現在是 [3, 5, 8]

# 查看堆中的最小元素（Peek operation）
# 直接訪問堆中的第一個元素來查看最小值。
smallest = min_heap[0]  # 返回 3，min_heap 保持不變

# 將列表轉換為堆
# 使用 heapify() 方法可以將一個無序列表轉換為堆。
unsorted_list = [9, 6, 2, 7, 4]
heapq.heapify(unsorted_list)  # unsorted_list 現在是 [2, 4, 9, 7, 6]

# 重要事項：
# - 堆是一種特殊的樹形資料結構，最常見的是最小堆和最大堆。
# - 最小堆的特性是每個節點的值都小於或等於其子節點的值，
#   這使得根節點總是最小的。
# - 最大堆則是每個節點的值都大於或等於其子節點的值。
# - 使用 heapq 模組時，Python 默認提供最小堆。
# - 堆的主要操作（插入和移除最小元素）均能在 O(log n) 時間內完成，
#   這使其非常適合用於實現優先級佇列。
