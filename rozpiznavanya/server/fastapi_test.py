from fastapi import FastAPI, WebSocket
import pyaudio
import wave

app = FastAPI()

cap = pyaudio.PyAudio()

@app.get("/")
def test():
    return {"message": "Hello World"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # клієнт підключився
    print("Connecting")
    await websocket.send_text("Аудіо отримано!")

    try:
        stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
        stream.start_stream()
        while True:
            data = stream.read(1024)  # Читаємо аудіопотік
            await websocket.send_bytes(data) 
    except Exception as e:
        print("Помилка аудіопотоку")

# uvicorn fastapi_test:app --reload