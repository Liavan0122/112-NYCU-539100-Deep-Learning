## Directory structure of inner folder
```
espnet/
utils/
test/
test_utils/
egs/
	hw1_task2/
		asr1/
			-conf/			# Configuration files for training, inference, etc.
			-downloads/		# Train / test dataset
			-local/			
				-data.sh	# Prepare the dataset in the Kaldi format
				-data_prep.py	#
			-scripts/
			-pyscripts/
			-steps/
			-utils/
			-asr.sh			#invoked by run.sh
			-cmd.sh
			-db.sh			# Specify the absolute path to the dataset and the directory path of each corpora
			-path.sh		# Setup script for environment variables
			-run.sh			# Entry point
		tts1/
```
