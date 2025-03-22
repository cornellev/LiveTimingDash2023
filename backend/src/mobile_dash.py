from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect, HTTPException
import json

router = APIRouter()

# Store active WebSocket connections
active_connections = set()

@router.post("/insert/uc24")
async def insert_uc24(request: Request):
    try: 
        data = await request.json()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON payload: {e}")
 
    try: 
         steer_angle = data['steer_angle']
         left_rpm = data['left_rpm']
         right_rpm = data['right_rpm']
         brake_on = data['brake_on']
         accel = data['accel']
         temp = data['temp']
         voltage = data['voltage']
    except KeyError as e:
         missing_field = e.args[0]
         raise HTTPException(status_code=422, detail=f"Missing required field: {missing_field}")
 
    print(f"Steering Angle: {steer_angle}; Left RPM: {left_rpm}; Right RPM: {right_rpm}; "
           f"Brake On: {brake_on}; Accelerometer: {accel}; Temperature: {temp}; Voltage: {voltage}")

    # Send received data to all connected WebSocket clients
    for connection in active_connections:
        await connection.send_text(json.dumps(data))

    
    return {
         "message": "Sensor values received", 
         "steer_angle": steer_angle, 
         "left_rpm": left_rpm, 
         "right_rpm": right_rpm, 
         "brake_on": brake_on, 
         "accel": accel, 
         "temp": temp, 
         "voltage": voltage
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
