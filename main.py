import librosa
from TimeStream import TimeStream

audio = librosa.load('04 33 _GOD_.mp3')
print(len(audio[0]))
