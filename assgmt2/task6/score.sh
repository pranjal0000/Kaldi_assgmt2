#!/bin/bash
# create new directories for both data
# create relevent files for the new data directories
# split datasets by using python script
# run decoders on them
# report wers for them, dont store for all of them, report results iteratively
# figure out if anything was missed from the big picture

# assuming calls are from working directory ie recipe
# g, m, n, l

test_nj=1
cmd="run.pl"
test_dir=$3
graph_dir=$4
output_dir=$5

rm -r -f $test_dir'g'
rm -r -f $test_dir'm'
rm -r -f $test_dir'n'
rm -r -f $test_dir'l'

mkdir $test_dir'g'
mkdir $test_dir'm'
mkdir $test_dir'n'
mkdir $test_dir'l'

mkdir $test_dir'g/.backup'
mkdir $test_dir'm/.backup'
mkdir $test_dir'n/.backup'
mkdir $test_dir'l/.backup'
mkdir $test_dir'g/conf'
mkdir $test_dir'm/conf'
mkdir $test_dir'n/conf'
mkdir $test_dir'l/conf'

python task6/split_quality.py $test_dir

steps/decode.sh --nj $test_nj --cmd $cmd $graph_dir $test_dir'g' $output_dir > temp.txt

cd $output_dir
cd ..
wait;
echo -n '(g)'
for x in decode_test; do [ -d $x ] && grep WER $x/wer_* | ../../utils/best_wer.sh; done 
cd ../..

steps/decode.sh --nj $test_nj --cmd $cmd $graph_dir $test_dir'm' $output_dir > temp.txt

cd $output_dir
cd ..
wait;
echo -n '(m)'
for x in decode_test; do [ -d $x ] && grep WER $x/wer_* | ../../utils/best_wer.sh; done
cd ../..



steps/decode.sh --nj $test_nj --cmd $cmd $graph_dir $test_dir'n' $output_dir > /dev/null 2>&1

cd $output_dir
cd ..
wait;
echo -n '(n)'
for x in decode_test; do [ -d $x ] && grep WER $x/wer_* | ../../utils/best_wer.sh; done
cd ../..



steps/decode.sh --nj $test_nj --cmd $cmd $graph_dir $test_dir'l' $output_dir > temp.txt

cd $output_dir
cd ..
wait;
echo -n '(l)'
for x in decode_test; do [ -d $x ] && grep WER $x/wer_* | ../../utils/best_wer.sh; done
cd ../..

# steps/decode.sh --nj $test_nj --cmd $cmd $graph_dir $test_dir $output_dir > temp.txt

# cd $output_dir
# cd ..
# wait;
# echo -n '(t)'
# for x in decode_test; do [ -d $x ] && grep WER $x/wer_* | ../../utils/best_wer.sh; done
# cd ../..

