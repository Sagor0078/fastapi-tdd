from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary
from tortoise.transactions import in_transaction
from typing import Optional

async def post(payload: SummaryPayloadSchema) -> Optional[int]:
    try:
        async with in_transaction():
            summary = await TextSummary.create(
                url=payload.url,
                summary="dummy summary",
            )
            return summary.id
    except Exception as e:
        # Log error (replace with actual logging)
        print(f"Database error: {e}")
        return None
