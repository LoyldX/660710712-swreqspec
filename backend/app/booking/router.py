# API จองคิว POST /bookings (T-03)
# รองรับ FR-BKG-04, FR-BKG-02, IF-IDP-01
import logging

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.auth.idp import get_verified_hn
from app.booking import service
from app.db.session import get_db

logger = logging.getLogger("booking")
router = APIRouter()


class BookingRequest(BaseModel):
    slot_id: int


@router.post("/bookings", status_code=201)
def create_booking(req: BookingRequest, hn: str = Depends(get_verified_hn), db: Session = Depends(get_db)):
    """ยืนยันการจอง แล้วคืนหมายเลขคิว (FR-BKG-04)"""
    logger.info("booking request slot=%s hn=%s", req.slot_id, hn)
    try:
        booking = service.create_booking(db, hn=hn, slot_id=req.slot_id)
    except service.DuplicateBookingError as dup:
        # ปฏิเสธ และคืนการจองเดิมกลับไป (FR-BKG-02)
        e = dup.existing
        return JSONResponse(
            status_code=409,
            content={"detail": "มีคิวที่ยังไม่ได้ใช้ในวันเดียวกันแล้ว", "booking_id": e.id, "slot_id": e.slot_id, "queue_no": e.queue_no},
        )
    except service.SlotFullError:
        raise HTTPException(status_code=409, detail="ช่วงเวลาเต็ม")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"booking_id": booking.id, "slot_id": booking.slot_id, "queue_no": booking.queue_no}
