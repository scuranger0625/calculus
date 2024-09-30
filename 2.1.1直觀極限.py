import numpy as np
import matplotlib.pyplot as plt

# 直觀極限的定義：
# 直觀極限是通過觀察函數的趨勢和行為來推測其極限值的一種方法，
# 而不依賴於嚴格的數學定義（例如 ε-δ 定義）。通過直觀地理解函數
# 隨著變數的變化趨勢，我們可以預測在某些極限情況下，函數值會趨向何處。
# 例如，當 x 趨向於無限大時，f(x) 可能會趨於某個常數、無限大或 0。
# 當 x 趨近於 0 時，類似地可以觀察到函數的極限行為。

# 設定 x 的範圍
# np.linspace 用於生成一個從 0.01 到 10 的等間距數列（避免分母為 0 的情況）
x = np.linspace(0.01, 10, 1000)

# 定義 f(x) = 1/x 的函數
# 這個函數在 x 趨於無限大時會趨近 0，在 x 趨近於 0^+ 時會趨向無限大
def reciprocal_function(x):
    return 1 / x

# 定義 f(x) = x^2 的函數
# 這個函數隨著 x 的增加會無限增長，因此當 x 趨向無限大時，f(x) 趨向無限大
def square_function(x):
    return x**2

# 繪製兩個函數的圖形
plt.figure(figsize=(12, 6))  # 設定圖表大小

# 繪製 f(x) = 1/x 的圖形
plt.subplot(1, 2, 1)  # 繪製第一個子圖（兩行一列中的第一張）
plt.plot(x, reciprocal_function(x), label=r'$f(x) = \frac{1}{x}$', color='blue')  # 繪圖
plt.axhline(0, color='black',linewidth=0.5)  # 加上 x 軸
plt.axvline(0, color='black',linewidth=0.5)  # 加上 y 軸
plt.title(r'極限當 $x \to \infty$ 和 $x \to 0^+$')  # 圖片標題
plt.xlabel(r'$x$')  # x 軸標籤
plt.ylabel(r'$f(x)$')  # y 軸標籤
plt.legend()  # 顯示圖例
plt.grid(True)  # 顯示網格線

# 繪製 f(x) = x^2 的圖形
plt.subplot(1, 2, 2)  # 繪製第二個子圖（兩行一列中的第二張）
plt.plot(x, square_function(x), label=r'$f(x) = x^2$', color='red')  # 繪圖
plt.axhline(0, color='black',linewidth=0.5)  # 加上 x 軸
plt.axvline(0, color='black',linewidth=0.5)  # 加上 y 軸
plt.title(r'極限當 $x \to \infty$')  # 圖片標題
plt.xlabel(r'$x$')  # x 軸標籤
plt.ylabel(r'$f(x)$')  # y 軸標籤
plt.legend()  # 顯示圖例
plt.grid(True)  # 顯示網格線

# 顯示圖表
plt.tight_layout()  # 調整圖表佈局，避免重疊
plt.show()
