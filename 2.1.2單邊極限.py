import numpy as np
import matplotlib.pyplot as plt

# 單邊極限的定義：
# 單邊極限描述的是函數在某個點從一側趨近該點時的行為。
# 左極限是當 x 從該點的左側趨近時的函數極限值，記作 lim_{x -> a^-} f(x)。
# 右極限是當 x 從該點的右側趨近時的函數極限值，記作 lim_{x -> a^+} f(x)。
# 若左極限和右極限相等，則該點的雙邊極限存在，否則雙邊極限不存在。

# 定義分段函數
def piecewise_function(x):
    if x < 1:
        return 2 * x + 1  # 當 x 小於 1 時，函數為 2x + 1
    else:
        return x ** 2  # 當 x 大於或等於 1 時，函數為 x^2

# 將分段函數應用到 NumPy 陣列上（用 np.vectorize 讓它能處理陣列）
vectorized_function = np.vectorize(piecewise_function)

# 設定 x 的範圍，分別生成 x 在左側與右側的數據點
x_left = np.linspace(0, 1, 500, endpoint=False)  # 小於 1 的值（左極限）
x_right = np.linspace(1, 2, 500)  # 大於或等於 1 的值（右極限）

# 計算函數值
y_left = vectorized_function(x_left)
y_right = vectorized_function(x_right)

# 繪製圖形來視覺化單邊極限
plt.figure(figsize=(8, 6))

# 繪製左側（小於 1 的部分）
plt.plot(x_left, y_left, label=r'$f(x) = 2x + 1, \ x < 1$', color='blue')

# 繪製右側（大於或等於 1 的部分）
plt.plot(x_right, y_right, label=r'$f(x) = x^2, \ x \geq 1$', color='red')

# 在 x = 1 處用圓圈標記左極限和右極限
plt.scatter(1, 3, color='blue', edgecolor='black', zorder=5, label=r'左極限 $\lim_{x \to 1^-} f(x) = 3$')
plt.scatter(1, 1, color='red', edgecolor='black', zorder=5, label=r'右極限 $\lim_{x \to 1^+} f(x) = 1$')

# 添加圖形標題和坐標軸標籤
plt.title("單邊極限示例")
plt.xlabel("x")
plt.ylabel("f(x)")

# 顯示圖例
plt.legend()

# 顯示網格
plt.grid(True)

# 顯示圖表
plt.show()

