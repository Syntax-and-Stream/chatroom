import asyncio
import websockets

# Function to handle receiving messages from the server
async def receive_messages(websocket):
    try:
        while True:
            message = await websocket.recv()
            print(f"New message: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed.")

# Function to send messages to the server
async def send_messages(websocket):
    while True:
        message = input("Enter your message: ")
        await websocket.send(message)

# Main function to start the client
async def start_client():
    url = "ws://127.0.0.1:8765"  # Server address
    async with websockets.connect(url) as websocket:
        print("Connected to the chatroom!")
        
        # Start receiving messages in the background
        asyncio.create_task(receive_messages(websocket))
        
        # Start sending messages to the server
        await send_messages(websocket)

# Run the client
if __name__ == "__main__":
    asyncio.run(start_client())
