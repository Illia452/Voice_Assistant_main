import asyncio
import websockets

async def receiver():
    async with websockets.connect("wss://server-hpxl.onrender.com/ws") as websocket:
        # надсилаємо перше повідомлення як ім'я "receiver"
        await websocket.send("receiver")
        
        while True:
            # Отримуємо повідомлення від sender
            message = await websocket.recv()
            print(f"Received message: {message}")


asyncio.get_event_loop().run_until_complete(receiver())