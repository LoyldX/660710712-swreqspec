# บันทึกการจองและตัดที่นั่ง (T-03)
# รองรับ FR-BKG-04, FR-BKG-02
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import Booking, Slot


class SlotFullError(Exception):
    """ช่วงเวลาที่เลือกไม่มีที่นั่งเหลือแล้ว"""


class DuplicateBookingError(Exception):
    """ผู้รับบริการมีคิวที่ยังไม่ได้ใช้ในวันเดียวกันอยู่แล้ว (FR-BKG-02)"""

    def __init__(self, existing: Booking):
        super().__init__(existing.id)
        self.existing = existing


def create_booking(db: Session, hn: str, slot_id: int) -> Booking:
    """ยืนยันการจอง: ตรวจที่นั่ง ตัดที่นั่ง บันทึกการจอง ยังไม่ออกหมายเลขคิว รอ Q-02 (FR-BKG-04)"""
    slot = db.get(Slot, slot_id)
    if slot is None:
        raise ValueError("ไม่พบช่วงเวลา")

    # กันจองซ้ำวันเดียวกัน นับต่อผู้รับบริการ (HN) เท่านั้น (FR-BKG-02)
    existing = db.scalar(
        select(Booking).where(
            Booking.hn == hn,
            Booking.booking_date == slot.slot_date,
            Booking.status == "BOOKED",
        )
    )
    if existing is not None:
        raise DuplicateBookingError(existing)

    if slot.remaining <= 0:
        raise SlotFullError(slot_id)

    slot.remaining -= 1
    booking = Booking(
        hn=hn,
        slot_id=slot.id,
        booking_date=slot.slot_date,
        queue_no=None,  # รอ Q-02: ยังไม่กำหนดรูปแบบและวิธีออกเลขคิว
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking
