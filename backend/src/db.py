import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # Optional, for local dev

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set. Define it in Heroku or .env.")

def insert_sensor_data(data):
    query = """
        INSERT INTO official_data_2025.sensor_data (
        x_accel, y_accel, z_accel,
        gps_lat, gps_long,
        left_rpm, right_rpm,
        temp
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING *;
    """

    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute(query, (
            data["x_accel"],
            data["y_accel"],
            data["z_accel"],
            data["gps_lat"],
            data["gps_long"],
            data["left_rpm"],
            data["right_rpm"],
            data["temp"]
        ))
        inserted_row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return inserted_row
    except Exception as e:
        print("DB Insert Error:", e)
        raise
