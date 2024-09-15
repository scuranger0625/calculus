# 定義函數 f(x) = 2x + 3
def f(x):
    """
    函數 f(x) 的定義：
    - 自變數 (Independent Variable)：x 是函數的輸入。
    - 依變數 (Dependent Variable)：f(x) 是函數的輸出，取決於 x 的值。
    - 定義域 (Domain)：所有實數 R，因為任何實數都可以代入 f(x) = 2x + 3 計算。
    - 值域 (Range)：所有實數 R，因為 2x + 3 是線性函數，輸出的值可以是任何實數。
    """
    return 2 * x + 3

# 定義用來測試的自變數列表
x_values = [-10, -1, 0, 1, 10]  # 測試的自變數值，包括負數、零和正數

# 遍歷每一個自變數 x，並計算對應的依變數 f(x)
for x in x_values:
    # 輸出自變數、依變數、定義域與值域的關係
    print(f"自變數: {x}, 依變數 f({x}) = {f(x)}")
    
# 定義域與值域的說明
print("\n定義域 (Domain)：所有實數 R (無限制)")
print("值域 (Range)：所有實數 R (因為 2x + 3 是線性函數)")

