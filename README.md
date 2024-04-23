# ESPNET DL

## 環境建設要求

### Software Requirements

* Python 3.6.1+
* gcc 4.9+ for PyTorch1.0.0+
* Cuda 8.0, 9.0, 9.1, 10.0 depending on each DNN library
* Cudnn 6+, 7+
* NCCL 2.0+ (for the use of multi-GPUs)

### 我的建置
```
Python = 3.12.2;
gcc = 11.4;
Cudatoolkit = 12.1
Cudnn = 8.9.2.6
NCCL = 2.21.5.1
```

## 安裝教學

參考 [Espnet 官方文件](https://espnet.github.io/espnet/installation.html#step-2-installation-espnet).

或是github上的Tutorial at CMU Usage of ESPnet (ASR as an example) [Material](https://colab.research.google.com/github/espnet/notebook/blob/master/espnet2_recipe_tutorial_CMU_11751_18781_Fall2022.ipynb)

[Espnet Github](https://github.com/espnet/espnet)
 

## 資料目錄
If you create a new directory in egs2/ for the new dataset. This will automatically create several other files and directories.
```
asr.sh    cmd.sh    conf  db.sh  local  path.sh  pyscripts    scripts  steps    utils
```
Besides, you can also see the following different files in the different folders: 
```
%/conf/*.yaml               ## For the model configurations
```
```
%/local/data_prep.py        ##
%/local/data.sh
```
```
%/downloads/*.              ##
```
```
%run.sh                     ##
```

## 執行方式

**環境建置在anaconda虛擬環境**  
```
!conda activate espnet
```
```
%cd /content/espnet/egs2/${your_task_name}/asr1
!./run.sh
```

*For example*  
```
%cd /content/espnet/egs2/an4/asr1
!./run.sh
```

## 可能有啥



## 作業結果
### Data Discription
單人女聲聲音（高雄腔）
輸入：台語語音音檔（格式：wav檔, 22 kHz, mono, 32 bits）
輸出：台羅拼音（依教育部標準）

### Evaluation 評分標準
* 只看'台羅拼音'，而且'不管音調'，辨認輸出範例如下：
"li be e mih kiann lan lan san san long be tsiau tsng"
* 評分標準使用 word error rate (WER）
* 'Word-Error Rate (WER)'. WER= (D + S + I) / N × 100% （整個詞的字元都要正確，才算對）。

### WER Talbe
| Model  | Snt | Wrd  | Corr | Sub | Del  | Ins | Err | S.Err  |
| ------------- |:-------------:| ------------- |:-------------:|:-------------:| ------------- |:-------------:| ------------- |:-------------:|
| asr_train_asr_whisper_small_lora_finetune_**v2**_raw_zh_whisper_multilingual_sp   | 200     | 3374      | 84.9     | 14.1      | 1.0     | 1.5      | 16.5     | 69.5      |
| asr_train_asr_whisper_small_lora_finetune_**v3**_raw_zh_whisper_multilingual_sp   | 200     | 3374      | 83.7     | 15.2      | 1.1     | 1.5      | 17.8     | 72.5      |
| asr_train_asr_conformer_xlsr_raw_zh_bpe150_sp    | 200     | 3374      | 70.2     | 26.4      | 3.4     | 2.3      | 32.1     | 89.0      |

### Final rank in class

![NYCU-IAlS-DL2024-Taiwanese-ASR Submission](https://github.com/Deep-Learning-NYCU/taiwanese-speech-recognition-using-espnet-toolkit-A122130/assets/166596141/84ebe12f-b6fb-4f74-8a98-82ae1f93ce47)
![Classroom Competition](https://github.com/Deep-Learning-NYCU/taiwanese-speech-recognition-using-espnet-toolkit-A122130/assets/166596141/92fa6c84-42d1-4207-b1c9-46db94c8570d)
(Kaggle information)

