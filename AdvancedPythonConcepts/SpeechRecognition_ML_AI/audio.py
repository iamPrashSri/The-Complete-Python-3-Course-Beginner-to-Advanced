# import pyglet
#
# file = pyglet.resource.media('./sounds/cheerful.mp3')
# file.play()
#
# pyglet.app.run()

import pyaudio
import wave
import speech_recognition as sr
import subprocess
from .commands import Commander

running = True
def say(text):
    subprocess.call('say ' + text, shell=True)

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

r = sr.Recognizer()
cmd = Commander()
def initSpeech():
    print("Listening...")

    # play_audio('./sounds/cheerful.mp3')
    with sr.Microphone() as source:
        print('Say Something')
        audio = r.listen(source)

    # play_audio('./sounds/cheerful.mp3')

    command = ''
    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand you")

    cmd.discover(command)
    if command in ['quit', 'exit', 'bye', 'goodbye']:
        global running
        running = False

while running == True:
    initSpeech()