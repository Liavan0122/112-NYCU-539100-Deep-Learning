# DL ESPnet Homework1

## Environmental requirements
### Software Requirements

* Python 3.6.1+
* gcc 4.9+ for PyTorch1.0.0+
* Cuda 8.0, 9.0, 9.1, 10.0 depending on each DNN library
* Cudnn 6+, 7+
* NCCL 2.0+ (for the use of multi-GPUs)

### My Environmental
```
Python = 3.12.2;
gcc = 11.4;
Cudatoolkit = 12.1
Cudnn = 8.9.2.6
NCCL = 2.21.5.1
```


## Installation ESPnet

I mainly refer to the tutorial in these website
[Espnet official document](https://espnet.github.io/espnet/installation.html#step-2-installation-espnet).

CMU Usage of ESPnet (ASR as an example) [Material](https://colab.research.google.com/github/espnet/notebook/blob/master/espnet2_recipe_tutorial_CMU_11751_18781_Fall2022.ipynb)

[Espnet Github](https://github.com/espnet/espnet)
 


## Run a Recipe

**The environment is built in anaconda and ESPnet virtual environment**  
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



## Homework Result
### Data Discription
Single female voice (Kaohsiung accent)
Input: Taiwanese voice file (format: wav file, 22 kHz, mono, 32 bits)
Output: Tailuo Pinyin (according to the standards of the Ministry of Education)

### Evaluation 
* Only compare the context 'TaiLuo Pinyin', and 'regardless of tone', the recognition output example is as follows:
"li be e mih kiann lan lan san san long be tsiau tsng"
* The scoring criteria uses word error rate (WER)
* 'Word-Error Rate (WER)'. WER= (D + S + I) / N × 100% (the characters of the entire word must be correct to be considered correct).

### WER Talbe
| Model  | Snt | Wrd  | Corr | Sub | Del  | Ins | Err | S.Err  |
| ------------- |:-------------:| ------------- |:-------------:|:-------------:| ------------- |:-------------:| ------------- |:-------------:|
| asr_train_asr_whisper_small_lora_finetune_**v2**_raw_zh_whisper_multilingual_sp   | 200     | 3374      | 84.9     | 14.1      | 1.0     | 1.5      | 16.5     | 69.5      |
| asr_train_asr_whisper_small_lora_finetune_**v3**_raw_zh_whisper_multilingual_sp   | 200     | 3374      | 83.7     | 15.2      | 1.1     | 1.5      | 17.8     | 72.5      |
| asr_train_asr_conformer_xlsr_raw_zh_bpe150_sp    | 200     | 3374      | 70.2     | 26.4      | 3.4     | 2.3      | 32.1     | 89.0      |

### Final rank in class

![image](https://github.com/Liavan0122/112-NYCU-539100-Deep-Learning/assets/167183282/7aeaa4c9-2cf9-42dd-bde1-7f7c6e62a29b)
![image](https://github.com/Liavan0122/112-NYCU-539100-Deep-Learning/assets/167183282/facd874c-351b-4e0a-aee1-067b8bf1cbb2)

(Kaggle information)

