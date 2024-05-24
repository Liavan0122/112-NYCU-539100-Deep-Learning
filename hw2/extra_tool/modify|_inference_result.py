import pandas as pd
import re

# 讀取inference 後 CSV文件
df = pd.read_csv('/content/drive/MyDrive/inference_output.csv')

# 定義一個函數，用于提取第一個數字部分
def extract_numbers(text):
    match = re.search(r'\d+', str(text))
    return match.group(0) if match else ''

# 應用函數到'Answer'列
df['Answer'] = df['Answer'].apply(extract_numbers)

# 保存结果到新的CSV文件
df.to_csv('/content/drive/MyDrive/inference_output_number.csv', index=False)
