# Audio to Text Conversion

This repository can be used to convert audio to text. The code is specifically made to convert large audio snippets into
text, as most speech recognition models dont work on large audio files. Hence, here the audio is first split and then
decoded to text.

## Dependency Installation

Assuming python and pip is installed, the followed commands on terminal will create a new virtual environment and
install all the necessary dependencies

```commandline
sudo apt install python3-venv
python3 -m venv audio_2_text_env
source audio_2_text/bin/activate
pip install -r requirements.txt
```

## Transcription Stages

The input to the algorithm is a audio file (only wav files supported) and the output is a text file where the first word
of each line corresponds to the name of the audio file from which it was transcribed. This audio file is 10 seconds long
and can be used to further correct the text translation, as the output of the speech recognition is sub-optimal. The 10
second files can be found in a subdirectory "split" in the original directory. 

## Running

Set the directory path of the audio file in the directory variable and the filename of the audio file in the
audio_text.py code and run the following command to generate the transcription.

```pycon
python audio_text.py
```

The output on the console will show the progress of the translation and create a text file in the directory specified by
the user.

