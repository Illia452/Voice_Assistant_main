import pyaudio
import whisper
import time
import torch

# Завантажуємо модель
model = whisper.load_model("turbo", device="cuda")

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

print("Lisening...")

while True:
    data = stream.read(4096)

    result = model.transcribe(data, language="uk")
    print(torch.cuda.memory_allocated()) 
    print(result["text"])

