from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
import json

router = APIRouter()

# Store active WebSocket connections
active_connections = set()

@router.post("/insert/uc24")
async def insert_uc24(request: Request):
    data = await request.json()
    print("Received Data:", json.dumps(data, indent=2))

    # Send received data to all connected WebSocket clients
    for connection in active_connections:
        await connection.send_text(json.dumps(data))

    return data


@router.websocket("/ws/uc24")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.add(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            print("Received WebSocket Data:", data)

            # Broadcast the received data to all connected clients
            for connection in active_connections:
                await connection.send_text(data)
    except WebSocketDisconnect:
        active_connections.remove(websocket)
        print("WebSocket Disconnected")
