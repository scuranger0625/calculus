"""
一對一函數的定義：
- 一對一函數是指，對於函數 f(x)，如果 f(x1) = f(x2)，則必須有 x1 = x2。
  換句話說，函數不會將不同的輸入值映射為相同的輸出值。
- 視覺化上來看，如果用水平線穿過函數的圖形，水平線最多只能與函數圖形相交一次（這稱為水平線測試）。

舉例：
- 函數 f(x) = 2x + 1 是一對一的，因為不同的 x 值對應不同的 f(x)。
- 函數 f(x) = x^2 不是一對一的，因為 f(1) = f(-1) = 1，不同的 x 值對應相同的 f(x)。
"""

# 定義我們要檢查的一個函數 f(x)
def f(x):
    """
    這是我們要檢查的一對一函數的範例:
    函數 f(x) = 2x + 1 是一對一的。
    如果你想測試非一對一的函數，可以嘗試 f(x) = x**2
    """
    return 2 * x + 1  # 你可以將此處替換為 x**2 來測試非一對一的情況

# 檢查函數是否是一對一的
def is_one_to_one(start, end):
    """
    檢查給定範圍內的函數是否為一對一的。
    這裡我們使用字典來存儲函數的輸出值，並檢查是否有重複的輸出。
    
    :param start: 範圍的開始 (例如: -10)
    :param end: 範圍的結束 (例如: 10)
    :return: 如果函數是一對一的，則返回 True；否則返回 False
    """
    
    # 用來存放每個輸出的值
    output_map = {}

    # 遍歷從 start 到 end 的所有 x 值
    for x in range(start, end + 1):
        result = f(x)  # 計算 f(x) 的輸出
        # 如果這個輸出值已經在字典中存在，則說明它不是一對一
        if result in output_map:
            print(f"函數 f(x) 不是一對一的，因為 f({output_map[result]}) = f({x}) = {result}")
            return False
        else:
            # 否則，將輸出值存入字典
            output_map[result] = x

    print(f"在範圍 {start} 到 {end} 內，函數 f(x) 是一對一的")
    return True

# 測試範例
start_range = -10  # 開始範圍
end_range = 10     # 結束範圍

# 檢查我們的函數 f(x) 是否是一對一的
is_one_to_one(start_range, end_range)
