
# Dataset Description

1. 注意訓練檔案有1.5GB
2. 訓練音檔：train目錄（請忽略._*.wav，這是mac電腦的隱藏暫存檔）
3. 測試音檔：test目錄（請忽略._*.wav，這是mac電腦的隱藏暫存檔）
4. 字典：lexicon.txt（教育部部定台羅拼音，子音，母音），檢查用，訓練時用不到
5. 訓練資料列表：train.csv（id, text）
6. 答案範例檔：sample.csv（id, text）

## Sox
注意用sox轉音檔格式，轉成 16 kHz sampling, signed-integer, 16 bits
```
sox in.wav -r 16000 -e signed-integer -b 16 out.wav
```

## Data Augmentation
注意測試音檔使用 ，有人工加上變形與背景雜訊。但人聽得懂的，電腦也要能聽得懂。
這些音檔都已被用 audiomentations & nlpaug 套件（https://github.com/iver56/audiomentations & https://github.com/makcedward/nlpaug）進行修改過。基本上使用了下列functions跟參數：

## Augmentation links
### short_noises
(https://github.com/iver56/audiomentations/tree/main/demo/short_noises)
### AddBackgroundNoise
(https://github.com/karolpiczak/ESC-50?tab=readme-ov-file#download)
### ApplyImpulseResponse
(http://www.echothief.com/downloads/)

## Note
我是先做Data Augmentation再做Sox
