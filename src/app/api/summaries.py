from fastapi import APIRouter, HTTPException
from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema

router = APIRouter()

@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> dict:
    summary_id = await crud.post(payload)
    
    if not summary_id:
        raise HTTPException(status_code=400, detail="Failed to create summary")

    return {"id": summary_id, "url": payload.url}
