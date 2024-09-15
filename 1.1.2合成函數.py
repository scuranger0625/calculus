"""
合成函數的定義：
- 合成函數是將一個函數的輸出作為另一個函數的輸入。
- 設有兩個函數 f(x) 和 g(x)，則合成函數 (g ∘ f)(x) 定義為：
  (g ∘ f)(x) = g(f(x))
- 這表示我們先計算 f(x)，再將其結果作為 g(x) 的輸入進行計算。

範例：
- 若 f(x) = 2x + 3 和 g(x) = x^2，則合成函數 (g ∘ f)(x) = (2x + 3)^2
"""

# 定義第一個函數 f(x)
def f(x):
    """
    函數 f(x) 的定義：
    - 公式：f(x) = 2x + 3
    - 自變數：x 是輸入值
    - 依變數：f(x) 是輸出值
    """
    return 2 * x + 3

# 定義第二個函數 g(x)
def g(x):
    """
    函數 g(x) 的定義：
    - 公式：g(x) = x^2
    - 自變數：x 是輸入值
    - 依變數：g(x) 是輸出值
    """
    return x ** 2

# 定義合成函數 g(f(x))
def composite_function(x):
    """
    合成函數的定義：
    - 公式：g(f(x)) = (2x + 3)^2
    - 自變數：x 是輸入值
    - 運算過程：先計算 f(x)，再將 f(x) 作為 g 的輸入進行運算
    """
    return g(f(x))

# 測試合成函數
x_value = 5
result = composite_function(x_value)

# 輸出結果
print(f"自變數 x = {x_value}")
print(f"f(x) = 2x + 3，當 x = {x_value} 時，f({x_value}) = {f(x_value)}")
print(f"g(x) = x^2，當 f(x) = {f(x_value)} 時，g(f(x)) = {result}")
print(f"因此，合成函數 g(f(x)) 在 x = {x_value} 的時候，結果為：{result}")
