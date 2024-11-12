from vosk import Model, KaldiRecognizer
import os
import pyaudio

if not os.path.exists("model"):
    print("Porfavor instale o model de https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit(1)

model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())