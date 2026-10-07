# Prompt log

บันทึกทุกครั้งที่ใช้ AI กับ repo นี้ เขียนต่อท้ายเรื่อย ๆ ไม่ลบของเก่า

---

## 2569-09-23 13.40 คำสั่ง: /tasks specs/001-booking/spec.md

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- ผลลัพธ์: specs/001-booking/tasks.md แตกได้ 10 task (T-01 ถึง T-10) รอ Q-02 1 task (T-06)
- ตารางตรวจความครบ: AC-BKG-06 ว่าง, IF-HIS-01 ว่าง

### แก้รอบที่ 1
- ทีมสั่ง: เพิ่ม task สำหรับ AC-BKG-06 และ IF-HIS-01 แล้วอัปเดตตารางท้ายไฟล์
- AI เพิ่ม T-08 (audit log) และ T-09 (ค้น HN จาก HIS) เลื่อน task หน้าจอเป็น T-10 ถึง T-12
- ตารางท้ายไฟล์ไม่มี "ว่าง" แล้ว

---

## 2569-09-23 14.20 คำสั่ง: /implement T-01 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/config.py, backend/app/db/models.py, backend/app/db/session.py, backend/app/db/migrations/001_init.py, backend/tests/test_T01_schema.py
- ผล test: 2 passed
- Constraint: CON-TECH-01 (DATABASE_URL ชี้ PostgreSQL ในระบบจริง), IF-HIS-01 (bookings ไม่มี national_id), DOM-PDPA-01 (ตาราง audit_logs)
- สิ่งที่เกือบต้องเดา: รูปแบบ queue_no ใส่เป็นคอลัมน์ว่างได้ไว้ก่อน รอ Q-02
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-27 19.05 คำสั่ง: /implement T-02 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/slots/router.py, backend/app/slots/service.py, backend/app/main.py, backend/tests/conftest.py, backend/tests/test_AC_BKG_05.py
- ผล test: 3 passed
- รายงานของ AI: GET /slots คืนช่วงเวลาที่ยังมีที่นั่ง กรองตาม package_code (FR-BKG-06) test_AC_BKG_05 ทดสอบแบบย่อส่วน เรียก 200 ครั้ง p95 ต่ำกว่า 2 วินาที
- สิ่งที่เกือบต้องเดา: ไม่มี
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-28 20.30 คำสั่ง: /implement T-03 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/booking/router.py, backend/app/booking/service.py, backend/app/auth/idp.py และแก้ backend/app/main.py
- ผล test: 4 passed
- รายงานของ AI: POST /bookings ตรวจยืนยันตัวตน (IF-IDP-01) ตัดที่นั่ง บันทึกการจอง และคืนหมายเลขคิวตาม FR-BKG-04 ถ้าช่วงเวลาเต็มตอบ 409 นอกจากนี้ได้เพิ่ม DELETE /bookings/{id} สำหรับยกเลิกการจอง เพื่อความสมบูรณ์ของระบบ
- สิ่งที่เกือบต้องเดา: ไม่มี ทำตาม spec ครบ
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-10-07 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/

- เครื่องมือ: Claude Code (VS Code)
- โหมด: ร่าง (AC-BKG-01 ยังไม่มีแถวใน test-cases.md)
- TC ที่เสนอ (สถานะ "ร่าง" ทุกแถว): TC-BKG-01-1 ถึง TC-BKG-01-6 (ปกติ 3: pytest/vitest/คน, ขอบ 2: ว่าง 0 ที่ และ 2 ที่, ทางผิด 1: ยังไม่ยืนยันตัวตน)
- ส่วนที่ติด Q-02: "แสดงหมายเลขคิว" ใน TC-BKG-01-1, 01-2, 01-4, 01-6
- ส่วนที่ spec ไม่ได้บอก: รหัสตอบกลับเมื่อยังไม่ยืนยันตัวตน (TC-BKG-01-5), ข้อความแจ้งจองสำเร็จบนหน้าจอ (TC-BKG-01-2)
- ยังไม่เขียนโค้ด test รอทีมตรวจแถวและเปลี่ยนสถานะเป็น "ใช้ได้"

---

## 2569-10-07 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/

- โหมด: รอทีมตรวจ (พบแถว AC-BKG-01 เดิม 6 แถว สถานะ "ร่าง" ทั้งหมด)
- ตรวจสถานะ task: T-03 เสร็จ, T-06 รอ Q-02
- ผล: ไม่เพิ่มแถวซ้ำและไม่เขียนโค้ด test; ไม่มี test ที่รัน
- ขั้นตอนถัดไป: ทีมตรวจแถวและเปลี่ยนสถานะเป็น "ใช้ได้" ก่อนสั่ง /testcases อีกครั้ง

---

## 2569-10-07 คำสั่ง: แก้ TC-BKG-01-2 ให้ปฏิเสธเมื่อไม่มีที่นั่ง

- ขอบเขตที่ขอ: ตรวจ/แก้เฉพาะ `backend/app/booking/service.py`; ห้ามแก้ test; รัน `pytest -v`
- ผลตรวจ: `create_booking` มีเงื่อนไข `slot.remaining <= 0` และยก `SlotFullError`; router ตอบ HTTP 409 สำหรับกรณีนี้ จึงไม่พบส่วนที่ต้องแก้ใน service และไม่ได้แก้โค้ด
- หมายเหตุ: TC-BKG-01-2 ใน `test-cases.md` เป็นกรณีหน้าจอ ใช้ API จำลองที่ตอบสำเร็จและตรวจการแสดงหมายเลขคิว ไม่ได้ทดสอบกรณีที่นั่งเต็ม
- ผล `cd backend && pytest -v`: เริ่มโหลด conftest ไม่สำเร็จ เพราะ environment ไม่มี `fastapi` (`ModuleNotFoundError: No module named 'fastapi'`); ไม่มี test ได้ถูกรัน
- test ไม่ถูกแก้

---

## 2569-10-07 คำสั่ง: /verify specs/001-booking/

- อ่าน `spec.md`, `plan.md`, `tasks.md`, `test-cases.md`, `AGENTS.md` และโค้ดทุกไฟล์ใน `backend/app/`, `frontend/src/`, `backend/tests/`, `frontend/src/__tests__/`
- ผล test: backend รันไม่ได้เพราะไม่พบคำสั่ง `pytest`; frontend รันไม่ได้เพราะไม่พบคำสั่ง `vitest`; จึงไม่มี test ผ่านหรือไม่ผ่านจากการรันครั้งนี้
- สร้าง `specs/001-booking/rtm.md` โดยไม่แก้โค้ด, test, spec, plan หรือ tasks
- RTM: ครบ 0, ยังไม่ถึง 3, รอ 0, ช่องโหว่ 12; ข้อค้นพบใหม่ F-01 ถึง F-11

---

## 2569-10-07 คำสั่ง: /testcases AC-BKG-02 specs/001-booking/

- โหมด: ร่าง เพราะ `test-cases.md` ยังไม่มีแถวของ AC-BKG-02 และ T-04 มีสถานะ “พร้อมทำ”
- เพิ่ม test case สถานะ “ร่าง” 4 แถว: TC-BKG-02-1 ถึง TC-BKG-02-4
- ครอบคลุมทางปกติ, ขอบเขตวันเดียวกัน, กรณีมีที่นั่งแต่ถูกกันจองซ้ำ และทางผิดที่คิวเดิมถูกใช้แล้ว
- กรณีคิวเดิมถูกใช้แล้ว: spec ไม่ได้บอกผลลัพธ์ที่คาดหวัง จึงยังไม่กำหนด assert
- ยังไม่เขียนโค้ด test และยังไม่รัน test; รอทีมตรวจแถวและเปลี่ยนสถานะเป็น “ใช้ได้”

---

## 2569-10-07 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/

- โหมด: หยุด เพราะแถวของ AC-BKG-01 ใน `test-cases.md` (TC-BKG-01-1 ถึง TC-BKG-01-6) ยังเป็นสถานะ "ร่าง" ทุกแถว ไม่มีแถว "ใช้ได้"
- ไม่ได้เพิ่มหรือแก้แถวในตาราง ไม่ได้เขียนโค้ด test และไม่ได้รัน test
- ข้อสังเกตให้ทีมตรวจ: TC-BKG-01-1 ส่วนที่ 2 (queue_no) เขียนว่า "(ใช้ได้)" แต่ TC-BKG-01-2, -4, -6 เขียนว่า "(รอ Q-02)" ขณะที่ spec.md ยังระบุว่า Q-02 ยังไม่ได้คำตอบ
- ขั้นตอนถัดไป: ทีมตรวจแถวและเปลี่ยนสถานะเป็น "ใช้ได้" ก่อนสั่ง /testcases อีกครั้ง

---

## 2569-10-07 คำสั่ง: แก้ TC-BKG-01-2 ให้ปฏิเสธเมื่อไม่มีที่นั่ง (รอบที่ 2)

- ขอบเขตที่ขอ: แก้เฉพาะ `backend/app/booking/service.py` ให้ปฏิเสธเมื่อไม่มีที่นั่ง; ห้ามแก้ test; รัน `pytest -v`
- ผลตรวจ: `create_booking` (service.py บรรทัด 26-27) มี `if slot.remaining <= 0: raise SlotFullError` อยู่แล้ว และ `router.py` บรรทัด 28-29 ตอบ 409 จึงไม่ได้แก้โค้ด
- ข้อสังเกต: TC-BKG-01-2 ในตารางเป็นกรณีหน้าจอ (vitest แสดงหมายเลขคิว) ไม่ใช่กรณีที่นั่งเต็ม กรณีที่นั่งเต็มคือ TC-BKG-01-3; ทุกแถวของ AC-BKG-01 ยังเป็น "ร่าง" และยังไม่มี test `test_TC_BKG_01_*` ในโค้ด จึงไม่มี test ของ TC-BKG-01-2 ที่ไม่ผ่าน
- ผล `cd backend && pytest -v` (สภาพแวดล้อมชั่วคราวจาก requirements.txt ผ่าน `uv run` เพราะเครื่องไม่มี pytest): 4 passed — test_AC_BKG_01, test_AC_BKG_05, test_T01_tables_created, test_T01_no_national_id
- ไม่ได้แก้โค้ดระบบและไม่ได้แก้ test

---

## 2569-10-07 ขั้น 2 ของ workshop week07: รัน test เดิมและทำให้พังโดยตั้งใจ (ไม่ใช้ AI ช่วยตัดสิน)

- ที่มา: ทำตามหัวข้อ // 07 ขั้น 2 ของหน้า week07
- รัน `cd backend && pytest -v` (ผ่าน uv): 4 passed — test_AC_BKG_01, test_AC_BKG_05, test_T01_tables_created, test_T01_no_national_id
- ใส่ `#` หน้าบรรทัด `slot.remaining -= 1` ใน `backend/app/booking/service.py` (บรรทัด 29) แล้วรันใหม่: ยัง 4 passed (ไม่มี test ไหนล้ม)
- ข้อสรุป: จุดที่ 1 = test อ่อน: `test_AC_BKG_01` (backend/tests/test_AC_BKG_01.py บรรทัด 12) assert แค่ status 201 ไม่ตรวจ Then ส่วน "ที่นั่งว่างของช่วงนั้นเป็น 0" (ตรงกับ F-06 ใน rtm.md)
- คืนไฟล์ด้วย `git restore backend/app/booking/service.py` แล้วรันใหม่: 4 passed และไม่มีไฟล์ใน app/ ถูกแก้
- ข้อสังเกต: เงื่อนไขในบรรทัด 26 เป็น `slot.remaining <= 0` อยู่แล้ว (ไม่ใช่ `< 0` ตามที่หน้า week07 คาดไว้) จึงไม่ได้ re-introduce บั๊กนี้

---

## 2569-10-07 ขั้น 3 ของ workshop week07: คนตรวจแถว AC-BKG-01 ใน test-cases.md (ร่าง เป็น ใช้ได้)

- การตัดสินใจนี้ทำตามเฉลยของผู้สอนในหน้า week07 (หัวข้อ // 07 ขั้น 3 "ดูเฉลย test cases ของ AC-BKG-01") ไม่ใช่การตัดสินของทีมเอง
- แถวร่างเดิมของ AI (TC-BKG-01-1 ถึง TC-BKG-01-6) ถูกแทนที่ด้วยแถวตามเฉลย 3 แถว สถานะ "ใช้ได้":
  - TC-BKG-01-1 ทางปกติ (test_TC_BKG_01_1_last_seat): Then 3 ส่วน ส่วนหมายเลขคิวเป็น "(รอ Q-02)"
  - TC-BKG-01-2 ขอบ (test_TC_BKG_01_2_no_seat_left): เหลือ 0 ที่ ตอบ 409 ไม่มีการจองใหม่ ที่นั่งไม่ติดลบ (FR-BKG-03, plan ข้อ 4)
  - TC-BKG-01-3 ทางผิด (test_TC_BKG_01_3_not_verified): ยังไม่ยืนยันตัวตน ตอบ 401 ไม่มีการจอง ที่นั่งยังเป็น 1 (IF-IDP-01)
- แถวร่างเดิมที่ถูกนำออก และเหตุผล:
  - TC-BKG-01-1 เดิม (backend ทางปกติ): แทนด้วยแถวตามเฉลย เพราะส่วน queue_no เดิมเขียน "(ใช้ได้)" ขัดกับ Q-02 ที่ยังไม่มีคำตอบ
  - TC-BKG-01-2 เดิม (vitest หน้า BookingResult): ออกจากตารางตามคำสั่งให้แทนที่ด้วย 3 แถวเฉลย; ส่วน Then ข้อ 1 spec ไม่ได้บอกข้อความ และส่วนข้อ 2 รอ Q-02 (หน้าจอเป็นขอบเขตของ T-06 ที่รอ Q-02)
  - TC-BKG-01-3 เดิม (ที่นั่งเต็ม 409): ซ้ำกับ TC-BKG-01-2 ใหม่ตามเฉลย
  - TC-BKG-01-4 เดิม (เหลือ 2 ที่ ขยับไปอีกฝั่ง): ผลไม่ต่างจากทางปกติ (จองสำเร็จเหมือนกัน) ตามกฎของหน้า week07 ให้ลบแถว "ขอบ" ที่ผลไม่ต่าง
  - TC-BKG-01-5 เดิม (ยังไม่ยืนยันตัวตน): ซ้ำกับ TC-BKG-01-3 ใหม่ตามเฉลย (รหัสตอบกลับที่เดิมเขียนว่า spec ไม่ได้บอก เฉลยกำหนด 401 จาก IF-IDP-01)
  - TC-BKG-01-6 เดิม (คนลองทั้งเส้น): ออกจากตารางตามคำสั่งให้แทนที่ด้วย 3 แถวเฉลย
- แถวของ AC-BKG-02 (TC-BKG-02-1 ถึง 02-4) ไม่ได้แตะ เก็บไว้รอขั้น 8
- ยังไม่เขียนโค้ด test ในขั้นนี้
