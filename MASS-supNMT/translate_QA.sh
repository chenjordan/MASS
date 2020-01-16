MODEL=./checkpoints/mass/fine-tune/checkpoint14887.pt

fairseq-generate ./QA_test_data/processed \
	-s Q -t A \
	--user-dir mass \
	--langs A,Q \
	--source-langs Q --target-langs A\
	--mt_steps Q-A \
	--gen-subset valid \
	--task xmasked_seq2seq \
	--path $MODEL \
	--beam 1 \
	--remove-bpe \
    --results-path ./result \
    --print-alignment \
    --memory-efficient-fp16 \
    --max-sentences 50 \
    --max-len-a 100 \
    --max-len-b 200 \
    --unkpen 100 \
    --lenpen 5 \
    --beam 15 \
    --remove-bpe \
    --max-tokens 160
