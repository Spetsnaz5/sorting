"""
插入排序演算法的運作如下：
    1.從第一個元素開始，該元素可以認為已經被排序
    2.取出下一個元素，在已經排序的元素序列中從後向前掃描
    3.如果該元素（已排序）大於新元素，將該元素移到下一位置
    4.重複步驟3，直到找到已排序的元素小於或者等於新元素的位置
    5.將新元素插入到該位置後
    6.重複步驟2~5
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

data = [random.randint(10, 100) for _ in range(20)]

print(data)

def sort_steps(data):
    arr = data.copy()
    steps = []
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            steps.append((arr.copy(), j, i))  # 記錄狀態
            j -= 1
        
        arr[j + 1] = key
        steps.append((arr.copy(), j + 1, i))  # 插入完成後記錄狀態
        
    print(arr)
    return steps

# 預先執行排序並記錄所有動畫步驟
steps = sort_steps(data)

# 畫布初始化
fig, ax = plt.subplots()
sc = ax.scatter(range(len(data)), data, c='skyblue', s=100)
ax.set_title("Insertion Sort - Scatter Plot Animation")
ax.set_xlim(-1, len(data))
ax.set_ylim(0, max(data) + 20)

# 動畫更新函式
def update(frame):
    current, i, j = frame
    colors = ['red' if k == i or k == j else 'skyblue' for k in range(len(current))]
    sc.set_offsets([[x, y] for x, y in zip(range(len(current)), current)])
    sc.set_color(colors)
    ax.set_title(f"Comparing: index {i} and {j}")

ani = animation.FuncAnimation(fig, update, frames=steps, interval=1000, repeat=False)
plt.show()