# test จาก test-cases.md (AC-BKG-02, FR-BKG-02) ชื่อขึ้นต้น test_TC_ ห้ามแก้ให้ผ่าน
from app.db.models import Booking
from tests.conftest import AUTH

# คนอื่น (HN ต่างจาก AUTH ซึ่งเป็น 0001234)
OTHER_AUTH = {"Authorization": "Bearer verified:0009999"}


def test_TC_BKG_02_1_same_day(client, db, make_slot):
    """TC-BKG-02-1 ทางปกติ (AC-BKG-02, FR-BKG-02)"""
    # Given มีคิวที่ยังไม่ได้ใช้ พรุ่งนี้ 09.00 น.
    first = client.post("/bookings", json={"slot_id": make_slot(start="09:00").id}, headers=AUTH)

    # When จองพรุ่งนี้ 13.00 น.
    res = client.post("/bookings", json={"slot_id": make_slot(start="13:00").id}, headers=AUTH)

    # Then (1) ปฏิเสธ ไม่มีการจองใหม่
    assert db.query(Booking).count() == 1
    # Then (2) ได้การจองเดิมกลับมา
    assert res.json()["booking_id"] == first.json()["booking_id"]
    # Then (3) แสดงหมายเลขคิวเดิม: รอ Q-02 ยังไม่ตรวจ (ยังไม่มีใครตัดสินรูปแบบเลขคิว)


def test_TC_BKG_02_2_next_day(client, db, make_slot):
    """TC-BKG-02-2 ขอบ (AC-BKG-02, FR-BKG-02)"""
    # Given มีคิวที่ยังไม่ได้ใช้ พรุ่งนี้ 09.00 น.
    client.post("/bookings", json={"slot_id": make_slot(start="09:00", days_from_today=1).id}, headers=AUTH)

    # When จองมะรืนนี้ 09.00 น.
    res = client.post("/bookings", json={"slot_id": make_slot(start="09:00", days_from_today=2).id}, headers=AUTH)

    # Then (1) จองสำเร็จ เพราะคนละวัน
    assert res.status_code == 201
    # Then (2) มีการจอง 2 รายการ
    assert db.query(Booking).count() == 2


def test_TC_BKG_02_3_other_person(client, db, make_slot):
    """TC-BKG-02-3 ทางผิด (AC-BKG-02, FR-BKG-02)"""
    # Given คนอื่นมีคิวพรุ่งนี้ 09.00 น. เรายังไม่มีคิว
    client.post("/bookings", json={"slot_id": make_slot(start="09:00").id}, headers=OTHER_AUTH)
    slot_1300 = make_slot(start="13:00", remaining=2)

    # When จองพรุ่งนี้ 13.00 น.
    res = client.post("/bookings", json={"slot_id": slot_1300.id}, headers=AUTH)

    # Then (1) จองสำเร็จ เพราะกฎนี้นับต่อคน
    assert res.status_code == 201
    # Then (2) ที่นั่งช่วง 13.00 น. ลดลง 1
    db.refresh(slot_1300)
    assert slot_1300.remaining == 1
