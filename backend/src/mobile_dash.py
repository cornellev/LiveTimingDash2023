from fastapi import APIRouter, Request
import json

router = APIRouter()

@router.post("/uc24")
async def insert_uc24(request: Request):
    data = await request.json()
    print("Received Data:", json.dumps(data, indent=2))
    return data