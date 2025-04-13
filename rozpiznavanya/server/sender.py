import asyncio
import websockets

async def sender():
    async with websockets.connect("wss://server-hpxl.onrender.com/ws") as websocket:
        # надсилаємо перше повідомлення як ім'я "sender"
        await websocket.send("sender")
        
        while True:
            message = input("Enter message to send: ")
            await websocket.send(message)
            print(f"Message sent: {message}")
            await asyncio.sleep(1)

# run_until_complete() — цей метод блокує програму і чекає, поки не завершиться виконання асинхронної функції send_audio()
asyncio.get_event_loop().run_until_complete(sender())

# ws://localhost:8000/ws

