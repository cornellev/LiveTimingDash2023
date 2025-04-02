from fastapi import APIRouter, Request, HTTPException
from services.redis_service import RedisService
from models.schemas import *
from pydantic import BaseModel

router = APIRouter()
redis_service = RedisService()


@router.get("/")
async def root():
    return {"message": "Welcome to API v1"}


@router.get("/status")
async def status():
    return {"status": "operational"}

# Getting data from sensors
@router.get("/sensor/{sensor_id}")
async def read_latest_sensor_data(sensor_id):
    sensor_data = await redis_service.get_sensor_data_all(sensor_id)
    sensor_responses = []
    for sensor_type, sensor_json in sensor_data.items():
        sensor_values = SensorData.model_validate_json(sensor_json)
        sensor_response = SensorResponse(
            device_id=sensor_id,
            sensor_type=sensor_values.sensor_type,
            latest_value=sensor_values.value,
            unit=sensor_values.unit,
            last_update=sensor_values.timestamp,
        )
        sensor_responses.append(sensor_values)
    return sensor_responses


@router.get("/sensor/{sensor_id}/{sensor_type}")
async def read_sensor_type_data(sensor_id, sensor_type):
    sensor_data = await redis_service.get_sensor_data(sensor_id, sensor_type)
    if sensor_data is None:
        return ""
    else:
        sensor_values = SensorData.model_validate_json(sensor_data)
        sensor_response = SensorResponse(
            device_id=sensor_id,
            sensor_type=sensor_values.sensor_type,
            latest_value=sensor_values.value,
            unit=sensor_values.unit,
            last_update=sensor_values.timestamp,
        )
        return sensor_response


@router.post("/timing")
async def get_timing(request: Request):
    try:
        data = await request.json()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON payload: {e}")

    try:
        lap_ids = data['lap_ids']
        lap_times = data['lap_times']
        total_time = data['total_time']
    except KeyError as e:
        raise HTTPException(status_code=422, detail=f"Missing required field: {e.args[0]}")

    print(f"Lap ID: {lap_ids}; Lap Times: {lap_times}; Total Time: {total_time}")

    return {
        "message": "Lap times received",
        "lap_ids": lap_ids,
        "lap_times": lap_times,
        "total_time": total_time
    }