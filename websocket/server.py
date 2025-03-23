import asyncio
import websockets

clients = set()

# Broadcast message to all clients
async def broadcast(message):
    # Send the message to all connected clients
    for client in clients:
        try:
            await client.send(message)
        except:
            clients.remove(client)

# Handle each client connection
async def handle_client(websocket):
    # Register the new client
    clients.add(websocket)
    print(f"New connection from {websocket.remote_address}")

    try:
        while True:
            # Wait for a message from the client
            message = await websocket.recv()
            print(f"Received message: {message}")

            # Broadcast the message to all other clients
            await broadcast(message)
    except websockets.exceptions.ConnectionClosed:
        print(f"Connection closed from {websocket.remote_address}")
    finally:
        # Unregister the client and close the connection
        clients.remove(websocket)
        await websocket.close()

# Start the WebSocket server
async def start_server():
    server = await websockets.serve(handle_client, "127.0.0.1", 8765)
    print("Server started, waiting for clients to connect...")
    await server.wait_closed()

# Run the server
if __name__ == "__main__":
    asyncio.run(start_server())
