import math
import os
import speech_recognition as sr
from pydub import AudioSegment


class ProcessAudio():
    def __init__(self, folder, filename):
        self.total_secs = 0
        self.folder = folder
        self.filename = filename.split('.')[0]  # preserving the name without the extension type
        self.filepath = folder + '/' + filename

        self.audio = AudioSegment.from_file(self.filepath, format='wav')

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_sec, to_sec, split_filename):
        t1 = from_sec * 1000  # library deals with microseconds instead of seconds, hence the 1000
        t2 = to_sec * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '/split/' + split_filename, format="wav")

    def multiple_split(self, sec_per_split):
        self.total_secs = math.ceil(self.get_duration())
        for i in range(0, self.total_secs, sec_per_split):
            split_fn = self.filename + '-' + str(i // 10 + 1).zfill(4)  # naming with leading zeros for nice sort
            self.single_split(i, i + sec_per_split, split_fn)
            if i == self.total_secs - sec_per_split:
                print('All split successfully')

    def convert_to_text(self):
        os.makedirs(self.folder + '/split/', exist_ok=True)
        self.multiple_split(10)
        with open(directory + '/text.txt', 'w+') as f:
            for file in sorted(os.listdir(self.folder + '/split/')):
                AUDIO_FILE = self.folder + '/split/' + file

                # use the audio file as the audio source
                r = sr.Recognizer()
                with sr.AudioFile(AUDIO_FILE) as source:
                    audio = r.record(source)  # read the entire audio file

                    # with open(directory + '/text.txt', 'a+') as f:
                    f.write(AUDIO_FILE.split('/')[-1] + " " + r.recognize_google(audio) + '\n')
                    print("Finished Processing: " + str(int(AUDIO_FILE.split('/')[-1].split('-')[1]) * 10) + '/' + str(
                        self.total_secs) + ' secs')


directory = "audio/Sample"
file = "sample.wav"
ps_audio = ProcessAudio(directory, file)
ps_audio.convert_to_text()
