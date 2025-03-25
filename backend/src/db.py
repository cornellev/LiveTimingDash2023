import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # Load DATABASE_URL from .env if not on Heroku

DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable not set")

def insert_sensor_data(data):
    query = """
        INSERT INTO test-2025 (
            Left_rpm, Right_rpm, Gps_lat, Gps_long,
            X_accel, Y_accel, Z_accel, Temp
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute(query, (
            data["left_rpm"],
            data["right_rpm"],
            data["gps_lat"],
            data["gps_long"],
            data["x_accel"],
            data["y_accel"],
            data["z_accel"],
            data["temp"]
        ))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("DB Insert Error:", e)
        raise
