# !/usr/bin/env bash
# Set bash to 'debug' mode, it will exit on :
# -e 'error', -u 'undefined variable', -o ... 'error in pipeline', -x 'print commands',
set -e
set -u
set -o pipefail

log() {
    local fname=${BASH_SOURCE[1]##*/}
    echo -e "$(date '+%Y-%m-%dT%H:%M:%S') (${fname}:${BASH_LINENO[0]}:${FUNCNAME[1]}) $*"
}
SECONDS=0

stage=1
stop_stage=100

datadir=downloads
hw1_root=${datadir}/


log "$0 $*"
. utils/parse_options.sh


. ./db.sh
. ./path.sh
. ./cmd.sh


if [ $# -ne 0 ]; then
    log "Error: No positional arguments are required."
    exit 2
fi

if [ -z "${hw1_task3}" ]; then
    log "Fill the value of 'hw1_task3' of db.sh"
    exit 1
fi

train_set="train_nodev"
train_dev="train_dev"
ndev_utt=200

if [ ${stage} -le 1 ] && [ ${stop_stage} -ge 1 ]; then
    log "stage 1: Data preparation"
    mkdir -p data/{train,test}

    # README exit or not
    if [ ! -f ${hw1_root}/README.txt ]; then
        echo Cannot find hw1 root! Exiting...
        exit 1
    fi

    # Prepare data in the Kaldi format, including three files:
    # text, wav.scp, utt2spk
    python3 local/data_prep.py ${hw1_root} sph2pipe

    for x in train; do
        for f in text wav.scp utt2spk; do
            sort data/${x}/${f} -o data/${x}/${f}
        done
        utils/utt2spk_to_spk2utt.pl data/${x}/utt2spk > "data/${x}/spk2utt"
    done
    for x in test; do
        for f in wav.scp utt2spk; do
            sort data/${x}/${f} -o data/${x}/${f}
        done
        utils/utt2spk_to_spk2utt.pl data/${x}/utt2spk > "data/${x}/spk2utt"
    done

    # make a dev set
    utils/subset_data_dir.sh --first data/train "${ndev_utt}" "data/${train_dev}"
    n=$(($(wc -l < data/train/text) - ndev_utt))
    utils/subset_data_dir.sh --last data/train "${n}" "data/${train_set}"
fi

log "Successfully finished. [elapsed=${SECONDS}s]"