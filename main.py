import os
import speech_recognition as sr
import ffmpeg

# pip install next libraries:
## pip install ffmpeg-python
## pip install SpeechRecognition

# get necessary data from current folder
ffmpeg_home = '/usr/bin/ffmpeg'
current_directory = os.getcwd()
input_video = 'C6190.MP4'

# turn input video into .mp3
ffmpeg = f'{ffmpeg_home} -i {current_directory}/{input_video} {current_directory}/processed.mp3'
os.system(ffmpeg)

# turn input video into .wav
ffmpeg_wav = f'{ffmpeg_home} -i {current_directory}/processed.mp3 {current_directory}/processed190.wav'
os.system(ffmpeg_wav)

# set up string recognizer and .wav audio file asa AudioFile
r = sr.Recognizer()
audio = sr.AudioFile('processed190.wav')

# check audio (transcription process)
with audio as source:
    audio = r.record(source)
    text = r.recognize_google(audio)

# print result
print(text)