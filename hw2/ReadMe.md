
# DL LLM Finetune Homework2

# LLaMA-Factory

## Environmental Requirements & Hardware Requirement
參照[官網](https://github.com/hiyouga/LLaMA-Factory?tab=readme-ov-file#requirement)

## Installation LLaMA-Factory

```
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e .[torch,metrics]
```
Extra dependencies available: torch, metrics, deepspeed, bitsandbytes, vllm, galore, badam, gptq, awq, aqlm, qwen, modelscope, quality

For example if you need to install **bitsandbytes**
```
pip install -e .[bitsandbytes]
```

## Directory structure of inner folder

```
.github/
assets/
data/

    -many folders/
    -README.md
    -README_zh.md
    -AI_train.json
    -AI_train_prompt.json
    -dataset_info.json
    -many dataset format.json

evaluation/
examples/

    -inference/
          --llama3_lora_sft.yaml
    -merge_lora/
          --llama3_lora_sft.yaml
    -qlora_single_gpu/
          --llama3_lora_sft_bitsandbytes.yaml
    -README.md
    -README_zh.md

scripts/
src/

    -llmtuner/
    -api.py
    -train.py
    -webui

tests/
Makefile
README.md
README_zh.md
docker-compose.yml
pyproject.toml
requirements.txt
setup.py
```

## Getting Started

### Data Preparation
Please refer to [data/README.md](https://github.com/hiyouga/LLaMA-Factory/blob/main/data/README.md) for checking the details about the format of dataset files. You can either use datasets on HuggingFace / ModelScope hub or load the dataset in local disk.

> If you add any customized dataset.json into data/  
> Please update `data/dataset_info.json` to use your custom dataset.


### Quickstart Training 
There are three ways that are able to run **fine-tuning**, **inference** and **merging** of the Llama3-8B-Instruct model, respectively.

1.
> Command line 

```
CUDA_VISIBLE_DEVICES=0 llamafactory-cli train examples/lora_single_gpu/llama3_lora_sft.yaml
CUDA_VISIBLE_DEVICES=0 llamafactory-cli chat examples/inference/llama3_lora_sft.yaml
CUDA_VISIBLE_DEVICES=0 llamafactory-cli export examples/merge_lora/llama3_lora_sft.yaml
```

* CUDA_VISIBLE_DEVICES=0,1  => 表示選擇GPU
* train                     => 訓練階段
* chat                      => inference階段
* export                    => 輸出模型

See [examples/README.md](https://github.com/hiyouga/LLaMA-Factory/blob/main/examples/README.md) for advanced usage (including distributed training).

---
2.
***
3.
- - -
