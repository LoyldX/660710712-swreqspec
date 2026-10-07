# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md SPEC-BKG-001 Draft v2 | plan.md | tasks.md | test-cases.md
สร้างด้วย `/verify specs/001-booking/` เมื่อ 2569-10-07 | test: 0 ผ่าน 0 ไม่ผ่าน (backend/frontend รันไม่ได้ เพราะไม่พบ `pytest` และ `vitest`)

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 | T-02 เสร็จ | `backend/app/slots/service.py:list_available_slots`, `backend/app/slots/router.py:get_slots` | `test_AC_BKG_05` (ไม่ได้รัน; ทดสอบเฉพาะ status และ p95 ของการเรียกแบบลำดับ) | ช่องโหว่ |
| FR-BKG-02 | AC-BKG-02 | T-04 พร้อมทำ | ไม่มีโค้ด | ไม่มี | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 พร้อมทำ | ไม่มีโค้ด | ไม่มี | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03 เสร็จ; T-06 รอ Q-02; T-07 พร้อมทำ | `backend/app/booking/service.py:create_booking`, `backend/app/booking/router.py:create_booking` | `test_AC_BKG_01` (ไม่ได้รัน; assert เฉพาะ HTTP 201) | ช่องโหว่ |
| FR-BKG-05 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มีโค้ด | ไม่มี | ช่องโหว่ |
| FR-BKG-06 | ไม่มี AC | T-02 เสร็จ; T-10, T-12 พร้อมทำ | `backend/app/slots/service.py:list_available_slots` กรอง `package_code`; ยังไม่มีหน้าจอ | ไม่มี | ช่องโหว่ |
| NFR-PERF-01 | AC-BKG-05 | T-02 เสร็จ | `backend/app/slots/router.py:get_slots` | `test_AC_BKG_05` (ไม่ได้รัน; ไม่ใช่ผู้ใช้พร้อมกัน 200 คน) | ช่องโหว่ |
| NFR-SEC-01 | ไม่มี AC ตรง ๆ | ไม่มี task | ไม่มีการตั้งค่า TLS ในโค้ดที่ตรวจ | ไม่มี | ช่องโหว่ |
| NFR-REL-02 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มีโค้ด | ไม่มี | ช่องโหว่ |
| NFR-USE-01 | ไม่มี AC ตรง ๆ | ไม่มี task | ไม่มีโค้ดหรือการทดสอบ usability | ไม่มี | ยังไม่ถึง |
| CON-TECH-01 | ไม่มี AC ตรง ๆ | T-01 เสร็จ | `backend/app/config.py`, `backend/app/db/session.py` | `test_T01_tables_created` (ไม่ได้รัน; ใช้ SQLite) | ช่องโหว่ |
| DOM-PDPA-01 | AC-BKG-06 | T-01 เสร็จ; T-08 พร้อมทำ | มีตาราง `audit_logs` ใน `backend/app/db/models.py` แต่ไม่มีการเขียน audit log | ไม่มี | ช่องโหว่ |
| IF-IDP-01 | ไม่มี AC ตรง ๆ | T-03 เสร็จ | `backend/app/auth/idp.py:get_verified_hn` และ dependency ของ `POST /bookings` | ไม่มี test เฉพาะ constraint | ช่องโหว่ |
| IF-HIS-01 | ไม่มี AC ตรง ๆ | T-01 เสร็จ; T-09 พร้อมทำ | ไม่มี HIS lookup; `BookingRequest` รับ `national_id` และ router log ค่า | `test_T01_no_national_id` (ไม่ได้รัน; ตรวจเฉพาะ schema) | ช่องโหว่ |
| IF-NOT-01 | AC-BKG-04 | T-07 พร้อมทำ | ไม่มีโค้ดคิวส่งข้อความ | ไม่มี | ช่องโหว่ |

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| `backend/app/slots/router.py:get_slots` (`GET /slots`) | FR-BKG-01, FR-BKG-06 | บางส่วน | คืนช่วงที่ `remaining > 0` และกรองแพ็กเกจได้ แต่ช่วงวันที่ถูกกำหนด 14 วัน และยังไม่มีหน้าจอ |
| `backend/app/slots/service.py:list_available_slots` | FR-BKG-01, FR-BKG-06 | ไม่ตรงทั้งหมด | `DAYS_AHEAD = 14` ไม่ใช่ 30 วัน |
| `backend/app/booking/router.py:create_booking` (`POST /bookings`) | FR-BKG-04, IF-IDP-01 | ไม่ตรงทั้งหมด | จองได้หลังตรวจ header แบบจำลอง แต่ไม่วางคำขอส่งข้อความ และรับ/log `national_id` |
| `backend/app/booking/service.py:create_booking` | FR-BKG-04, Q-02 | ไม่ตรง | สร้างเลขรูปแบบ `A001` และรีเซ็ตตามวัน ทั้งที่ Q-02 ยังไม่มีคำตอบ |
| `backend/app/booking/service.py:next_queue_no` | Q-02 | ไม่ควรมีการตัดสินใจนี้ | เป็นการเลือกทั้งรูปแบบและวิธีนับเลขแทนคำตอบของ Q-02 |
| `backend/app/booking/router.py:cancel_booking` (`DELETE /bookings/{booking_id}`) | ไม่มี; UC-02 | ไม่ตรง | เป็นความสามารถยกเลิกคิว ซึ่งอยู่ใน Out of scope |
| `backend/app/auth/idp.py:get_verified_hn` | IF-IDP-01 | ยังพิสูจน์ไม่ครบ | ตรวจเฉพาะรูปแบบ header จำลอง ยังไม่มี test ที่ยืนยันการปฏิเสธก่อนเข้าถึงข้อมูล |
| `backend/app/config.py`, `backend/app/db/session.py` | CON-TECH-01 | ไม่รับประกัน | ค่าเริ่มต้นเป็น SQLite จึงไม่ได้บังคับ PostgreSQL ตาม constraint หากไม่ตั้ง `DATABASE_URL` |
| `backend/app/db/models.py:Booking` | IF-HIS-01 | บางส่วน | ตารางไม่มี `national_id` และเก็บ HN แต่ request/log ยังรับและเขียนเลขบัตรประชาชน |
| `frontend/src/App.jsx` | FR-BKG-01, FR-BKG-03, FR-BKG-04, FR-BKG-05, FR-BKG-06 | ยังไม่ตรง | เป็นเพียงโครงหน้าจอ ไม่มี flow จองคิวหรือแสดงผลตาม requirements |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง
ทีมตัดสิน: เว้นว่างให้ทีมตัดสิน

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-01 | ละเมิด Constraint | `backend/app/booking/router.py:BookingRequest`, `create_booking` | IF-HIS-01 | รับ `national_id` ใน request และเขียนลง log ทั้งที่ต้องค้นจาก HIS แล้วอ้างอิงด้วย HN และไม่เก็บเลขบัตรประชาชนในบริบทการจอง; ยังไม่มี `/patients/lookup` | |
| F-02 | โค้ดไม่มี FR | `backend/app/booking/router.py:create_booking` | FR-BKG-04, IF-NOT-01 | เมื่อจองสำเร็จไม่มีการวางคำขอส่งข้อความยืนยันแบบ asynchronous | |
| F-03 | เดา Q-02 | `backend/app/booking/service.py:next_queue_no` | Q-02, FR-BKG-04 | โค้ดเลือก `A001` และนับใหม่ทุกวัน ทั้งที่รูปแบบและวิธีนับหมายเลขคิวยังรอคำตอบ | |
| F-04 | ตัวเลขไม่ตรง spec | `backend/app/slots/service.py:DAYS_AHEAD` | FR-BKG-01 | ใช้ 14 วันแทน “ภายใน 30 วันข้างหน้า” | |
| F-05 | FR ไม่มี AC | `spec.md` และการทำงาน FR-BKG-06 | FR-BKG-06 | FR-BKG-06 ไม่มี AC ที่ตรวจการเปลี่ยนแพ็กเกจแล้วคำนวณช่วงเวลาว่างใหม่; โค้ดที่มีเป็นเพียงตัวกรอง API และยังไม่มีหน้าจอ | |
| F-06 | test อ่อน | `backend/tests/test_AC_BKG_01.py:test_AC_BKG_01` | AC-BKG-01 | assert เฉพาะ status 201 ไม่ตรวจ booking id, รายการในฐานข้อมูล, queue_no หรือ remaining ตาม Then | |
| F-07 | test อ่อน | `backend/tests/test_AC_BKG_05.py:test_AC_BKG_05` | AC-BKG-05, NFR-PERF-01 | เรียกแบบลำดับ ไม่ใช่ผู้ใช้พร้อมกัน 200 คน จึงไม่พิสูจน์ p95 ภายใต้ concurrency ตาม requirement | |
| F-08 | ละเมิด Constraint | `backend/app/config.py:DATABASE_URL` | CON-TECH-01 | ค่าเริ่มต้นเป็น SQLite ไม่ใช่ PostgreSQL และไม่มีการบังคับว่าระบบจริงต้องใช้ PostgreSQL | |
| F-09 | โค้ดไม่มี FR | `backend/app/booking/router.py:cancel_booking` | Out of scope (UC-02) | เพิ่ม `DELETE /bookings/{id}` สำหรับยกเลิก/คืนที่นั่ง ทั้งที่การยกเลิกและเลื่อนคิวอยู่นอกขอบเขต | |
| F-10 | โค้ดไม่มี FR | ระบบ audit และหน้าดูข้อมูลการจอง | DOM-PDPA-01, AC-BKG-06 | มีเพียงโมเดล `audit_logs`; ไม่มี middleware/endpoint ที่บันทึกผู้เข้าถึง เวลา และรหัสผู้รับบริการทุกครั้งที่เข้าถึงข้อมูล | |
| F-11 | โค้ดไม่มี FR | `backend/app` และ `frontend/src` | NFR-SEC-01, NFR-REL-02, FR-BKG-05 | ไม่พบ TLS 1.2+, คิวส่งซ้ำภายใน 5 นาที หรือการส่งข้อความซ้ำ/ค้างส่ง | |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| - | ไม่มีข้อค้นพบเดิมให้ตรวจย้าย | ไม่พบ `rtm.md` เดิม |
