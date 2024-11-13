from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core

#Síntese de fala
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


if not os.path.exists("model"):
    print("Porfavor instale o model de https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit(1)

#Reconhecimento de fala

model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, frames_per_buffer=2048, input=True)
stream.start_stream()

#Loop do reconhecimento de fala
while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']
            print(text)
            speak(text)

        if text == 'que horas são' or text == 'me diga as horas':
            speak(core.SystemInfo.get_time())

        if text == 'maria':
            speak('pois não sônia?')

