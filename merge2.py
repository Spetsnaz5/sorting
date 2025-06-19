"""
合併排序演算法的運作如下：
    1.把資料「一分為二」拆到最小（只剩一個元素）
    2.再「一層層」回來，每次合併都排序好
"""
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 原始資料
data = [random.randint(10, 100) for _ in range(20)]
steps = []

# 初始化 global_data，確保排序時不影響原始 data
global_data = data.copy()

# 合併排序 + 步驟記錄
def merge_sort(arr, l=0):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], l)
    right = merge_sort(arr[mid:], l + mid)

    return merge(left, right, l)

def merge(left, right, start_index):
    global global_data
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        # 比較時紀錄整體狀態與比較 index
        steps.append((global_data.copy(), start_index + i, start_index + j + len(left)))

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    # 更新 global_data 並紀錄每一步合併後狀態
    for idx, val in enumerate(merged):
        global_data[start_index + idx] = val
        steps.append((global_data.copy(), start_index + idx, start_index + idx))

    return merged

# 執行合併排序
merge_sort(data.copy())

# 畫布初始化
fig, ax = plt.subplots()
sc = ax.scatter(range(len(data)), data, c='skyblue', s=100)
ax.set_title("Merge Sort - Full Array View")
ax.set_xlim(-1, len(data))
ax.set_ylim(0, max(data) + 10)

# 動畫更新函式
def update(frame):
    current, i, j = frame
    colors = ['red' if k == i or k == j else 'skyblue' for k in range(len(current))]
    sc.set_offsets([[x, y] for x, y in zip(range(len(current)), current)])
    sc.set_color(colors)
    ax.set_title(f"Comparing / Merging: index {i} and {j}")

# 建立動畫
ani = animation.FuncAnimation(fig, update, frames=steps, interval=300, repeat=False)
plt.show()