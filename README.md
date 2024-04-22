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



## 我的結果


*This text will be italic*  
_This will also be italic_

**This text will be bold**  
__This will also be bold__

_You **can** combine them_

### Unordered

* Item 1
* Item 2
* Item 2a
* Item 2b

### Ordered

1. Item 1
2. Item 2
3. Item 3
    1. Item 3a
    2. Item 3b
