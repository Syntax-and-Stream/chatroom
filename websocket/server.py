import asyncio
import websockets

connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    print(f"New connection from {websocket.remote_address}")

    try:
        async for message in websocket:
            print(f"Received from {websocket.remote_address}: {message}")
            # await broadcast(message)
    except websockets.ConnectionClosed as e:
        print(f"Client {websocket.remote_address} disconnected: {e}")
    finally:
        connected_clients.remove(websocket)

# def broadcast(message):
#     return asyncio.gather(*(client.send(message) for client in connected_clients if client.open))

async def main():
    server = await websockets.serve(handler, '127.0.0.1', 9990)
    print("Server started on ws://localhost:9990")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())