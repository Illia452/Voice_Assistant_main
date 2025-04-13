from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

clients = {}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        
        name = await websocket.receive_text()
        print(f"Client {name} connected.")
        clients[name] = websocket  # зберігаємо клієнта

        while True:
            try:
                data = await websocket.receive_text()
                print(f"Received message: {data}")
                
                # перевірка чи підключено обидва клієнти:
                if name == "sender" and "receiver" in clients:
                    await clients["receiver"].send_text(data)
                    print(f"Sent message to receiver: {data}")

                elif name == "receiver" and "sender" in clients:
                    await clients["sender"].send_text(data)
                    print(f"Sent message to sender: {data}")

                else:
                    # якщо другий клієнт ще не підключився
                    await websocket.send_text("Інший клієнт ще не підключився. Зачекайте...")
                    print("Waiting for other client.")

            except WebSocketDisconnect:
                print(f"Client {name} disconnected.")
                del clients[name] # видаляємо клієнта зі списку при відключенні
                break

    except Exception as e:
        print(f"Error: {e}")



# uvicorn server:app --reload