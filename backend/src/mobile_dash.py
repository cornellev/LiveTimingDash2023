from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect, HTTPException
import json
import asyncio

from src.db import insert_sensor_data

router = APIRouter()
active_connections = set()

@router.post("/insert/uc24")
async def insert_uc24(request: Request):
    try:
        payload = await request.json()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON payload: {e}")

    # If it's a single object, wrap it in a list
    data_list = payload if isinstance(payload, list) else [payload]

    for data in data_list:
        try:
            # Validate required fields
            _ = (
                data['left_rpm'],
                data['right_rpm'],
                data['gps_lat'],
                data['gps_long'],
                data['x_accel'],
                data['y_accel'],
                data['z_accel'],
                data['temp'],
            )
        except KeyError as e:
            raise HTTPException(status_code=422, detail=f"Missing required field: {e.args[0]}")

        try:
            await asyncio.to_thread(insert_sensor_data, data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to insert sensor data: {e}")

        # Broadcast to all clients
        for connection in active_connections:
            await connection.send_text(json.dumps(data))

    return {
        "message": "Sensor value(s) received",
        "count": len(data_list)
    }




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



# @router.post("/timing/")
# async def get_timing(request: Request):
#     try:
#         data = await request.json()
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"Invalid JSON payload: {e}")

#     try:
#         lap_ids = data['lap_ids']
#         lap_times = data['lap_times']
#         total_time = data['total_time']
#     except KeyError as e:
#         raise HTTPException(status_code=422, detail=f"Missing required field: {e.args[0]}")

#     print(f"Lap ID: {lap_ids}; Lap Times: {lap_times}; Total Time: {total_time}")

#     return {
#         "message": "Lap times received",
#         "lap_ids": lap_ids,
#         "lap_times": lap_times,
#         "total_time": total_time
#     }
