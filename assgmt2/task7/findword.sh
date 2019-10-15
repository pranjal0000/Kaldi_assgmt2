#!/bin/bash

word=$1
./steps/get_train_ctm.sh data/train data/lang exp/mono_ali > temp.txt

grep -w $word exp/mono_ali/ctm > task7/filew.txt

rm -r -f task7/output

mkdir task7/output

python3 task7/wav.py task7/filew.txt