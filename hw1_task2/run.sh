# !/usr/bin/env bash
# Set bash to 'debug' mode, it will exit on :
# -e 'error', -u 'undefined variable', -o ... 'error in pipeline', -x 'print commands',
set -e
set -u
set -o pipefail

# train_set=train
# valid_set=dev
# test_sets="dev test"

asr_config=conf/train_asr_conformer_xlsr.yaml
inference_config=conf/decode_asr.yaml
lm_config=conf/train_lm_transformer.yaml
use_lm=false
use_wordlm=false
# speed perturbation related
# (train_set will be "${train_set}_sp" if speed_perturb_factors is specified)
speed_perturb_factors="0.9 1.0 1.1"
# --feats_normalize ""
#    --token_type bpe for wav2vec bpe5000

./asr.sh \
    --stage 1 \
    --stop_stage 13 \
    --nj 8 \
    --ngpu 2 \
    --nbpe 150 \
    --gpu_inference true \
    --inference_nj 1 \
    --use_lm ${use_lm} \
    --use_word_lm ${use_wordlm} \
    --lang zh \
    --token_type bpe \
    --audio_format "flac.ark" \
    --feats_type raw \
    --asr_config "${asr_config}" \
    --lm_config "${lm_config}" \
    --inference_config "${inference_config}" \
    --cleaner whisper_basic \
    --train_set train_nodev \
    --valid_set train_dev \
    --test_sets "train_dev test" \
    --bpe_train_text "data/train_nodev/text" \
    --speed_perturb_factors "${speed_perturb_factors}" \
    --asr_speech_fold_length 512 \
    --asr_text_fold_length 150 \
    --lm_fold_length 150 \
    --lm_train_text "data/train_nodev/text" \
    --feats_normalize uttmvn "$@"

