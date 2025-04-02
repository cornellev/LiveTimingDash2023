from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.routes.v1 import router as v1_router
from config import settings
from mobile_dash import router as mobile_dash_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(v1_router, prefix=settings.API_V1_PREFIX)
app.include_router(mobile_dash_router, prefix='')

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}


@app.post("/timing/")
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