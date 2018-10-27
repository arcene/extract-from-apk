#!/bin/bash

#INPUT_PATH='./data/train_data/0-normal'
#OUTPUT_PATH='./data/train_data/dex_0-normal'

INPUT_PATH='./data/train_data/1-malware'
OUTPUT_PATH='./data/train_data/dex_1-malware'

for f in $(ls $INPUT_PATH)
do
    mkdir -p $OUTPUT_PATH/$f
    unzip $INPUT_PATH/$f -d $OUTPUT_PATH/$f
    mv $OUTPUT_PATH/$f/*.dex $OUTPUT_PATH/$f.dex
    find $OUTPUT_PATH/$f -not -name '*.dex' -delete
    rm -rf $OUTPUT_PATH/$f
    sleep 0.1
done

