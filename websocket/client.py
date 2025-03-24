import asyncio
import websockets

async def send_messages(websocket):
    while True:
        message = input("You: ")
        await websocket.send(message)
        await asyncio.sleep(0.1)  # Prevent message collisions

async def receive_messages(websocket):
    try:
        async for message in websocket:
            print(f"Friend: {message}")
    except websockets.ConnectionClosed:
        print("Server closed the connection.")

async def main():
    uri = "ws://localhost:9990"
    try:
        async with websockets.connect(uri, ping_interval=10, ping_timeout=20) as websocket:
            print("Connected to chatroom.")
            await asyncio.gather(send_messages(websocket), receive_messages(websocket))
    except ConnectionRefusedError:
        print("Failed to connect to the server. Ensure the server is running.")

if __name__ == "__main__":
    asyncio.run(main())
