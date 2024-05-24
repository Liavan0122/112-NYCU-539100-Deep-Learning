import pandas as pd
import json

def convert_excel_to_json(excel_file, output_json_file):
    # 讀取Excel文件
    df = pd.read_excel(excel_file)

    # 定義空列表存放結果
    results = []

    # 遍歷DataFrame的每一行
    for index, row in df.iterrows():
        # 構建instruction字符串
        instruction = "".join([
            f"接下來的訊息中，將會提供「文章」、「題目」，以及四個「選項」。請在仔細地閱讀並理解文章後，針對題目所述，從四個選項中選出最適當的答案。直接回答選項編號。\n\n",
                f"文章:{str(row['文章'])} \n",
                f"題目:{str(row['問題'])} \n",
                f"選項1:{str(row['選項1'])} \n",
                f"選項2:{str(row['選項2'])} \n",
                f"選項3:{str(row['選項3'])} \n",
                f"選項4:{str(row['選項4'])}。\n",
                f"假如此題的答案為選項1，回答「1」即可，依此類推"
                ])
        output = f"{str(row['正確答案'])}"

        # 構建每個字典
        result = {
            "instruction": instruction,
            "input": "",
            "output": output
        }

        # 添加到結果列表
        results.append(result)

    # 將結果保存到JSON文件
    with open(output_json_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print("結果已成功保存到:", output_json_file)

# 輸入您的Excel文件名和要保存的JSON文件名
excel_file = "/content/drive/MyDrive/AI.xlsx"
output_json_file = "/content/drive/MyDrive/output.json"

# 調用函數轉換Excel為JSON格式並保存到文件
convert_excel_to_json(excel_file, output_json_file)
