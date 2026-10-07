# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md SPEC-BKG-001 Draft v3 | plan.md | tasks.md | test-cases.md
สร้างด้วย `/verify specs/001-booking/` เมื่อ 2569-10-07 (verify v2 หลังแก้ F-09, F-04, F-03, F-01 และเพิ่ม Q-03, Q-04) | test: backend 7 ผ่าน 0 ไม่ผ่าน (frontend ไม่ได้รัน: ยังไม่มี test หน้าจอนอกจาก setup.test.jsx และไม่ได้ติดตั้ง node_modules)

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 (ตรวจแค่ความเร็ว ไม่ตรวจ "แสดง 30 วัน") | T-02 เสร็จ; T-10, T-12 พร้อมทำ | `backend/app/slots/service.py:list_available_slots`, `backend/app/slots/router.py:get_slots` | `test_AC_BKG_05` (ผ่าน; ไม่ตรวจช่วงวัน) | ช่องโหว่ (F-12; F-04 แก้แล้ว) |
| FR-BKG-02 | AC-BKG-02 | T-04 พร้อมทำ | ไม่มีโค้ด | ไม่มี test (test-cases TC-BKG-02-1 ถึง 02-4 ยังเป็น "ร่าง") | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 พร้อมทำ | ยังไม่มีการเสนอ 3 ช่วงใกล้เคียง (`create_booking` ตอบ 409 เมื่อเต็มแล้ว) | `test_TC_BKG_01_2_no_seat_left` ผ่าน (ตรวจเฉพาะ 409 / ไม่มีการจอง / ที่นั่งไม่ติดลบ) | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03 เสร็จ; T-06 รอ Q-02; T-07 พร้อมทำ | `backend/app/booking/service.py:create_booking`, `backend/app/booking/router.py:create_booking` | `test_AC_BKG_01` (ผ่าน แต่อ่อน), `test_TC_BKG_01_1_last_seat` ผ่าน, `test_TC_BKG_01_2_no_seat_left` ผ่าน, `test_TC_BKG_01_3_not_verified` ผ่าน (Then ส่วนหมายเลขคิว รอ Q-02 ไม่ได้ assert) | รอ Q-02 (F-03, F-09 แก้แล้ว; โค้ดไม่ออกเลขคิว queue_no เป็นค่าว่าง) |
| FR-BKG-05 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มีโค้ด | ไม่มี | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-02 เสร็จ; T-10, T-12 พร้อมทำ | `backend/app/slots/service.py:list_available_slots` กรอง `package_code`; ยังไม่มีหน้าจอ | ไม่มี | ช่องโหว่ (F-05) |
| NFR-PERF-01 | AC-BKG-05 | T-02 เสร็จ | `backend/app/slots/router.py:get_slots` | `test_AC_BKG_05` (ผ่าน; เรียกแบบลำดับ ไม่ใช่ผู้ใช้พร้อมกัน 200 คน) | ช่องโหว่ (F-07) |
| NFR-SEC-01 | ไม่มี AC ตรง ๆ | ไม่มี task | ไม่มีการตั้งค่า TLS ในโค้ดที่ตรวจ | ไม่มี | ช่องโหว่ (F-11) |
| NFR-REL-02 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มีโค้ด | ไม่มี | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC ตรง ๆ | ไม่มี task | ไม่มีโค้ดหรือการทดสอบ usability | ไม่มี | ยังไม่ถึง |
| CON-TECH-01 | ไม่มี AC ตรง ๆ | T-01 เสร็จ | `backend/app/config.py`, `backend/app/db/session.py` | `test_T01_tables_created` (ผ่าน; ใช้ SQLite) | ช่องโหว่ (F-08) |
| DOM-PDPA-01 | AC-BKG-06 | T-01 เสร็จ; T-08 พร้อมทำ | มีตาราง `audit_logs` ใน `backend/app/db/models.py` แต่ยังไม่มีการเขียน audit log | ไม่มี | ยังไม่ถึง (F-10) |
| IF-IDP-01 | ไม่มี AC ตรง ๆ | T-03 เสร็จ | `backend/app/auth/idp.py:get_verified_hn` และ dependency ของ `POST /bookings` | `test_TC_BKG_01_3_not_verified` (ผ่าน: ไม่ยืนยันตัวตนได้ 401 ไม่มีการจอง ที่นั่งไม่ถูกตัด) | ครบ |
| IF-HIS-01 | ไม่มี AC ตรง ๆ | T-01 เสร็จ; T-09 พร้อมทำ | ไม่มี HIS lookup; `BookingRequest` รับ `national_id` และ router log ค่า | `test_T01_no_national_id` (ผ่าน; ตรวจเฉพาะ schema) | ช่องโหว่ (F-01 โค้ดแก้แล้ว รอ Q-03) |
| IF-NOT-01 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มีโค้ดคิวส่งข้อความ | ไม่มี | ยังไม่ถึง (F-02) |

สรุปแถว: ครบ 1, ยังไม่ถึง 7, รอ Q-02 1 (FR-BKG-04), ช่องโหว่ 6 (รวม 15 แถว)

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| `backend/app/slots/router.py:get_slots` (`GET /slots`) | FR-BKG-01, FR-BKG-06 | ตรง (หลังบ้าน) | คืนช่วงที่ `remaining > 0` ภายใน 30 วัน และกรองแพ็กเกจได้ ยังไม่มีหน้าจอ |
| `backend/app/slots/service.py:list_available_slots` | FR-BKG-01, FR-BKG-06 | ตรง | `DAYS_AHEAD = 30` ตรง FR-BKG-01 (แก้ F-04 แล้ว) |
| `backend/app/booking/router.py:create_booking` (`POST /bookings`) | FR-BKG-04, IF-IDP-01 | ตรง | จองได้หลังตรวจ header แบบจำลอง; ไม่รับและไม่ log `national_id` แล้ว (แก้ F-01 แล้ว); ยังไม่วางคำขอส่งข้อความ (F-02 ยังไม่ถึง T-07); ไม่มี endpoint DELETE แล้ว (แก้ F-09) |
| `backend/app/booking/service.py:create_booking` | FR-BKG-04, FR-BKG-03, Q-02 | ตรง | ปฏิเสธเมื่อ `slot.remaining <= 0` ตัดที่นั่งเมื่อสำเร็จ (ยืนยันด้วย test_TC_BKG_01_1/2) `queue_no=None` รอ Q-02 |
| `backend/app/auth/idp.py:get_verified_hn` | IF-IDP-01 | ตรง (ตามที่จำลอง) | ปฏิเสธ 401 เมื่อไม่มี token รูปแบบที่กำหนด ยืนยันด้วย test_TC_BKG_01_3_not_verified |
| `backend/app/config.py`, `backend/app/db/session.py` | CON-TECH-01 | ไม่รับประกัน | ค่าเริ่มต้นเป็น SQLite จึงไม่ได้บังคับ PostgreSQL หากไม่ตั้ง `DATABASE_URL` (F-08) |
| `backend/app/db/models.py:Booking` | IF-HIS-01 | ตรง | ตารางไม่มี `national_id` และเก็บ HN; request/log ไม่รับเลขบัตรแล้ว (F-01 โค้ดแก้แล้ว เหลือรอ Q-03 ว่า log ต้องห้ามตามข้อกำหนดหรือไม่) |
| `backend/app/db/models.py:AuditLog` | DOM-PDPA-01 | ตรง (เฉพาะตาราง) | ยังไม่มีโค้ดเขียน audit log (ยังไม่ถึง T-08) |
| `frontend/src/App.jsx`, `frontend/src/api/client.js` | FR-BKG-01, FR-BKG-03, FR-BKG-04 | ยังไม่ตรง | เป็นโครงหน้าจอและตัวเรียก API ที่รายวิชาให้มา ยังไม่มี flow จองคิว |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง
ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)
หมายเหตุ: ช่อง "ทีมตัดสิน" ที่กรอกไว้ ตัดสินตามเฉลยและคำใบ้ของผู้สอนในหน้า week07 (ไม่ใช่การตัดสินของ AI เอง) ช่องที่เฉลยไม่ครอบคลุมเว้นว่างไว้

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-01 | ละเมิด Constraint | `backend/app/booking/router.py:BookingRequest`, `create_booking` | IF-HIS-01 | รับ `national_id` ใน request และเขียนลง log (บรรทัด 19 และ 25) ทั้งที่ต้องค้นจาก HIS แล้วอ้างอิงด้วย HN และไม่เก็บเลขบัตรประชาชนในบริบทการจอง; ยังไม่มี `/patients/lookup` | (โค้ดแก้แล้ว ดูหัวข้อ 4; เหลือรอผู้ใช้) เพิ่ม Q-03: IF-HIS-01 ระบุแค่ "ไม่เก็บในตารางการจอง" ไม่ได้พูดถึง log ต้องถามฝ่าย IT; ระหว่างรอ เอา national_id ออกจาก request และ log (ส่วนที่เดา) |
| F-02 | โค้ดไม่มี FR | `backend/app/booking/router.py:create_booking` | FR-BKG-04, IF-NOT-01 | เมื่อจองสำเร็จไม่มีการวางคำขอส่งข้อความยืนยันแบบ asynchronous | ไม่ใช่ปัญหา: ยังไม่ถึง T-07 (สถานะ "พร้อมทำ") |
| F-05 | FR ไม่มี AC | `spec.md` และการทำงาน FR-BKG-06 | FR-BKG-06 | FR-BKG-06 ไม่มี AC ที่ตรวจการเปลี่ยนแพ็กเกจแล้วคำนวณช่วงเวลาว่างใหม่; โค้ดที่มีเป็นเพียงตัวกรอง API และยังไม่มีหน้าจอ | เพิ่ม Q-04: FR-BKG-06 ควรมีเกณฑ์ยอมรับอย่างไร (ยังไม่เขียน AC ใหม่จนกว่าผู้ใช้ยืนยัน) |
| F-07 | test อ่อน | `backend/tests/test_AC_BKG_05.py:test_AC_BKG_05` | AC-BKG-05, NFR-PERF-01 | เรียกแบบลำดับ ไม่ใช่ผู้ใช้พร้อมกัน 200 คน จึงไม่พิสูจน์ p95 ภายใต้ concurrency ตาม requirement | |
| F-08 | ละเมิด Constraint | `backend/app/config.py:DATABASE_URL` | CON-TECH-01 | ค่าเริ่มต้นเป็น SQLite ไม่ใช่ PostgreSQL และไม่มีการบังคับว่าระบบจริงต้องใช้ PostgreSQL | |
| F-10 | โค้ดไม่มี FR | ระบบ audit และหน้าดูข้อมูลการจอง | DOM-PDPA-01, AC-BKG-06 | มีเพียงโมเดล `audit_logs`; ไม่มี middleware/endpoint ที่บันทึกผู้เข้าถึง เวลา และรหัสผู้รับบริการทุกครั้งที่เข้าถึงข้อมูล | ไม่ใช่ปัญหา: ยังไม่ถึง T-08 (สถานะ "พร้อมทำ") |
| F-11 | โค้ดไม่มี FR | `backend/app` และ `frontend/src` | NFR-SEC-01, NFR-REL-02, FR-BKG-05 | ไม่พบ TLS 1.2+, คิวส่งซ้ำภายใน 5 นาที หรือการส่งข้อความซ้ำ/ค้างส่ง (ส่วนคิวส่งซ้ำเป็นงานของ T-07; NFR-SEC-01 ไม่มี task รองรับใน tasks.md) | |
| F-12 | FR ไม่มี AC | `spec.md` และการทำงาน FR-BKG-01 | FR-BKG-01 | FR-BKG-01 (แสดงช่วงเวลาว่าง 30 วัน พร้อมที่นั่งคงเหลือ) มีแต่ AC-BKG-05 ซึ่งตรวจแค่ความเร็ว ไม่มี AC ที่ตรวจว่าแสดงครบ 30 วัน (ข้อค้นพบใหม่ในรอบนี้) | เพิ่ม Q-04: FR-BKG-01 ควรมีเกณฑ์ยอมรับอย่างไร (ยังไม่เขียน AC ใหม่จนกว่าผู้ใช้ยืนยัน) |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| F-06 | เพิ่ม test_TC_BKG_01_1_last_seat, test_TC_BKG_01_2_no_seat_left, test_TC_BKG_01_3_not_verified ต่อท้าย `backend/tests/test_AC_BKG_01.py` (test เดิม `test_AC_BKG_01` ยังอยู่ ไม่ได้แก้) ตรวจ Then ครบ (ยกเว้นหมายเลขคิว รอ Q-02) | ลองพังซ้ำ: ใส่ `#` หน้า `slot.remaining -= 1` แล้ว test_TC_BKG_01_1_last_seat ล้ม (assert 1 == 0); ปกติ 7 passed (ทีมตัดสิน: แก้ test ด้วยแถว test-cases ที่ใช้ได้ ตามเฉลยผู้สอนขั้น 3 และ 4) |
| F-01 (ส่วนโค้ด) | ลบฟิลด์ `national_id` ออกจาก `BookingRequest` และตัดออกจากข้อความ log ใน `backend/app/booking/router.py` (commit "fix F-01") ทีมตัดสินเดิม: เพิ่ม Q-03 และระหว่างรอ เอาส่วนที่เดาออก | grep "national_id" ใน backend/app/ ไม่พบ; pytest 7 passed; ยังคงอยู่ในหัวข้อ 3 เพราะรอคำตอบ Q-03 |
| F-03 | ลบ `next_queue_no` (A001) ให้ `queue_no=None  # รอ Q-02` ใน `backend/app/booking/service.py` (commit "fix F-03") ทีมตัดสินเดิม: แก้โค้ด: ให้ queue_no เป็นค่าว่างพร้อมคอมเมนต์ "รอ Q-02" เลิกออกเลข A001 | grep "queue" ไม่พบการออกเลข A001; pytest 7 passed |
| F-04 | แก้ `DAYS_AHEAD` จาก 14 เป็น 30 ใน `backend/app/slots/service.py` (commit "fix F-04") ทีมตัดสินเดิม: แก้โค้ด: spec พูดชัดว่า 30 วัน | grep ตัวเลข `DAYS_AHEAD = 30`; pytest 7 passed |
| F-09 | ลบ `DELETE /bookings/{booking_id}` และ `cancel_booking` ออกจาก `backend/app/booking/router.py` และ `service.py` (commit "fix F-09") ทีมตัดสินเดิม: แก้โค้ด: ของแถม อยู่ใน Out of scope (UC-02) ลบ endpoint และ cancel_booking ออก | grep "@router" เหลือ POST /bookings และ GET /slots เท่านั้น; grep "cancel" ไม่พบ; pytest 7 passed |
