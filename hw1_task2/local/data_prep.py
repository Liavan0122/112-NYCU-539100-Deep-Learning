import os
import glob
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python data_prep.py [hw1_root] [sph2pipe]")
        sys.exit(1)
    hw1_root = sys.argv[1]
    sph2pipe = sys.argv[2]


    for x in ["train"]:
        # all_audio_list = glob.glob(
        #     os.path.join(hw1_root, "train", "train","*.wav")
        # )
        train_path = glob.glob(os.path.join(hw1_root, "train", "train","*.wav"))
        transcription_path = glob.glob(os.path.join(hw1_root, "train", "train-toneless.csv"))
        transcription_path = transcription_path[0]

        with open(transcription_path) as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            transcription = list(csv_reader)

        transcription.sort(key=lambda x: int(x[0]))

        with open(os.path.join("data", x, "text"), "w") as text_f, open(
            os.path.join("data", x, "wav.scp"), "w"
        ) as wav_scp_f, open(
            os.path.join("data", x, "utt2spk"), "w"
        ) as utt2spk_f:


            for audio_path in train_path:
                filename = os.path.basename(audio_path)     # "o73a.wav" etc
                #speaker = os.path.basename(os.path.dirname(audio_path))     # "lc", "sk", etc
                speaker = "dummy"

                idx = int(filename[:-4]) - 1

                #transcript = " ".join(list(filename[:-4]))  # "o73" -> "o 7 3"
                #train_id = transcription[idx][0]
                train_text = transcription[idx][1]

                #uttid = f"{speaker}-{filename[:-4]}"    # "sk-o73a"
                uttid = f"{filename[:-4]}"    # "sk-o73a"

                # wav_scp_f.write(
                #    f"{uttid} {sph2pipe} -f wav -p -c 1 {audio_path} |\n"
                # )
                wav_scp_f.write(
                    f"{uttid} {audio_path}\n"
                )


                # Write text file
                text_f.write(f"{uttid} {train_text}\n")

                # Write utt2spk file
                utt2spk_f.write(f"{uttid} {speaker}\n")

    for x in ["test"]:
        test_path = glob.glob(os.path.join(hw1_root, "test","*.wav"))

        with open(os.path.join("data", x, "wav.scp"), "w") as wav_scp_f, open(
            os.path.join("data", x, "utt2spk"), "w"
        ) as utt2spk_f:

            for audio_path_test in test_path:
                filename = os.path.basename(audio_path_test)     # "o73a.wav" etc
                #speaker = os.path.basename(os.path.dirname(audio_path))     # "lc", "sk", etc
                speaker = "dummy"

                transcript = " ".join(list(filename[:-4]))  # "o73" -> "o 7 3"
                #uttid = f"{speaker}-{filename[:-4]}"    # "sk-o73a"
                uttid = f"{filename[:-4]}"    # "sk-o73a"

                # wav_scp_f.write(
                #    f"{uttid} {sph2pipe} -f wav -p -c 1 {audio_path} |\n"
                # )
                wav_scp_f.write(
                    f"{uttid} {audio_path_test}\n"
                )

                # Write utt2spk file
                utt2spk_f.write(f"{uttid} {speaker}\n")



