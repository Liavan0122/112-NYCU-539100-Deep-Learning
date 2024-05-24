import pandas as pd
import requests
import json
import csv

df = pd.read_excel('/content/drive/MyDrive/AI1000.xlsx')

# 讀取 CSV 檔案並傳遞問題進行推論
def inference_from_dataframe(df, url, output_csv):
  with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Answer'])  # 寫入文件的標題列
    for index, row in df.iterrows():
        question_ID = row['題號']
        question = "".join([
            f"接下來的訊息中，將會提供「文章」、「題目」，以及四個「選項」。請在仔細地閱讀並理解文章後，針對題目所述，從四個選項中選出最適當的答案。直接回答選項編號。\n\n",
                f"文章:{str(row['文章'])} \n",
                f"題目:{str(row['問題'])} \n",
                f"選項1:{str(row['選項1'])} \n",
                f"選項2:{str(row['選項2'])} \n",
                f"選項3:{str(row['選項3'])} \n",
                f"選項4:{str(row['選項4'])}。\n",
                f"假如此題的答案為選項1，回答「1」即可，依此類推"
                ])
        data = {
              "model": "unsloth/llama-3-8b-Instruct-bnb-4bit",
              "messages": [
                {
                  "role": "user",
                  "content": question,
                }
              ],
              "do_sample": True,
              "temperature": 0,
              "max_tokens": 300,
              "stream": False
            }  # 將問題組織成字典或 JSON 格式

        # 發送 POST 請求到指定的 URL 並傳遞問題資訊
        resp = requests.post(url, headers={"Content-Type": "application/json", "Authorization": "Bearer "}, json=data)
        if resp.status_code == 200:
            inference_result = resp.json()  # 解析服務器返回的推論結果
            inference_result_content = inference_result['choices'][0]['message']['content']
            # print("Question:", question)
            # print("")
            # print("Inference result:", inference_result_content)
            print(f"finished {index}")
            writer.writerow([question_ID, inference_result_content])  # 将结果写入CSV文件

        else:
            print("Failed to perform inference for question:", question)

# 示例使用
inference_url = 'http://140.114.78.39:8000/v1/chat/completions'  # 推論 URL
output_csv = '/content/drive/MyDrive/inference_output.csv'
inference_from_dataframe(df, inference_url, output_csv)
