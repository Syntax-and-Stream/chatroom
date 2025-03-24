import asyncio
import websockets

async def send_messages(websocket):
    while True:
        message = input("You: ")
        await websocket.send(message)

async def receive_messages(websocket):
    async for message in websocket:
        print(f"Friend: {message}")

async def main():
    uri = "ws://localhost:9999"
    async with websockets.connect(uri) as websocket:
        print("Connected to chatroom.")
        await asyncio.gather(send_messages(websocket), receive_messages(websocket))

if __name__ == "__main__":
    asyncio.run(main())
