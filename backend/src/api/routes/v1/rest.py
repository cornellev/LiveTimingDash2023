from fastapi import APIRouter, Request, HTTPException
from services.redis_service import RedisService
from models.schemas import *
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import uuid

router = APIRouter()
redis_service = RedisService()

# Database connection parameters
DB_HOST = "172.245.184.138"
DB_PORT = "5432"
DB_NAME = "laptimer"
DB_USER = "postgres"
DB_PASSWORD = "mysecretpassword"

# Function to get database connection
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    conn.autocommit = False
    return conn

# Initialize database tables if they don't exist
def init_db():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Create sessions table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id SERIAL PRIMARY KEY,
                session_id VARCHAR(50) UNIQUE NOT NULL,
                total_time FLOAT NOT NULL
            )
        """)
        
        # Create lap_times table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS lap_times (
                id SERIAL PRIMARY KEY,
                lap_id INTEGER NOT NULL,
                lap_time FLOAT NOT NULL,
                session_id VARCHAR(50) REFERENCES sessions(session_id)
            )
        """)
        
        conn.commit()
        print("Database tables initialized successfully")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Database initialization error: {e}")
    finally:
        if conn:
            conn.close()

# Initialize database tables
init_db()

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
    
    # Generate a unique session ID
    session_id = str(uuid.uuid4())
    
    # Store data in the database
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Insert session record
        cur.execute(
            "INSERT INTO sessions (session_id, total_time) VALUES (%s, %s)",
            (session_id, total_time)
        )
        
        # Insert lap time records
        for i in range(len(lap_ids)):
            cur.execute(
                "INSERT INTO lap_times (lap_id, lap_time, session_id) VALUES (%s, %s, %s)",
                (lap_ids[i], lap_times[i], session_id)
            )
        
        conn.commit()
        print(f"Timing data saved to database with session_id: {session_id}")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Database error: {str(e)}")
        # Continue with the original response even if database storage fails
    finally:
        if conn:
            conn.close()

    return {
        "message": "Lap times received",
        "lap_ids": lap_ids,
        "lap_times": lap_times,
        "total_time": total_time,
        "session_id": session_id
    }

@router.get("/timing/sessions")
async def get_sessions():
    """Retrieve all timing sessions"""
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT session_id, total_time FROM sessions")
        sessions = cur.fetchall()
        return list(sessions)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if conn:
            conn.close()

@router.get("/timing/sessions/{session_id}")
async def get_session_details(session_id: str):
    """Retrieve details for a specific session including all lap times"""
    conn = None
    try:
        conn = get_db_connection()
        
        # Get session details
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT session_id, total_time FROM sessions WHERE session_id = %s", (session_id,))
        session = cur.fetchone()
        
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")
        
        # Get lap times for this session
        cur.execute("SELECT lap_id, lap_time FROM lap_times WHERE session_id = %s ORDER BY lap_id", (session_id,))
        lap_times = cur.fetchall()
        
        return {
            "session_id": session["session_id"],
            "total_time": session["total_time"],
            "lap_times": lap_times
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if conn:
            conn.close()