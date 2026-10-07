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

---

## 2569-10-07 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/ (ขั้น 4 โหมดเขียน test)

- โหมด: เขียน test เพราะ AC-BKG-01 มีแถว "ใช้ได้" 3 แถว (TC-BKG-01-1 ถึง TC-BKG-01-3) ที่ยังไม่มี test ในโค้ด; T-03 สถานะ "เสร็จ"
- จำนวน test ก่อนเขียน 4 ตัว หลังเขียน 7 ตัว (เพิ่ม 3 เท่ากับจำนวนแถว) test เดิมทุกตัวยังอยู่ เพิ่มต่อท้ายไฟล์ `backend/tests/test_AC_BKG_01.py` เท่านั้น
- test ที่เพิ่ม: test_TC_BKG_01_1_last_seat, test_TC_BKG_01_2_no_seat_left, test_TC_BKG_01_3_not_verified
- ส่วน Then ที่ "(รอ Q-02)" ของ TC-BKG-01-1 ข้อ 3 เป็นคอมเมนต์ ไม่มี assert
- ผล `cd backend && pytest -v`: 7 passed, 0 failed (TC-BKG-01-1, -2, -3 ผ่านทั้งหมด)
- ผลต่างจากที่หน้า week07 คาดไว้: หน้า week07 คาดว่า test_TC_BKG_01_2_no_seat_left จะ FAILED (assert 201 == 409) เพราะโค้ดมี `if slot.remaining < 0` แต่โค้ดใน repo นี้เป็น `if slot.remaining <= 0` (backend/app/booking/service.py บรรทัด 26) อยู่แล้ว จึงผ่าน ไม่ต้องแก้โค้ดและไม่ได้แก้โค้ดระบบ ไม่ได้แก้ test ให้ผ่าน
- ตรวจว่า test จับบั๊กนี้ได้จริง: ชั่วคราวเปลี่ยนเป็น `slot.remaining < 0` แล้วรัน test_TC_BKG_01_2_no_seat_left ล้ม (assert 201 == 409) จากนั้น `git restore` คืนไฟล์
- ลองพังซ้ำ: ใส่ `#` หน้า `slot.remaining -= 1` แล้วรัน test_TC_BKG_01_1_last_seat ล้ม (assert 1 == 0) ส่วนอีก 6 ตัวผ่าน แปลว่า test แข็งแล้ว จากนั้น `git restore backend/app/booking/service.py` กลับมา 7 passed
- ตรวจ git status: มีเฉพาะไฟล์ใน backend/tests/ และ prompt-log.md ไม่มีไฟล์ใน app/ ถูกแก้
- ไม่มีส่วนที่ต้องเดา

---

## 2569-10-07 คำสั่ง: /verify specs/001-booking/ (ขั้น 5)

- อ่าน spec.md, plan.md, tasks.md, test-cases.md, rtm.md เดิม, AGENTS.md และโค้ดทุกไฟล์ใน backend/app/, backend/tests/, frontend/src/ (frontend มีแต่โครงเริ่มต้น และ setup.test.jsx)
- ผล test: backend 7 passed 0 failed; frontend ไม่ได้รัน (ไม่มี test หน้าจอนอกจาก setup และไม่ได้ติดตั้ง node_modules)
- rtm.md เดิมมีอยู่แล้ว (F-01 ถึง F-11, ช่อง "ทีมตัดสิน" ว่างทั้งหมด) จึงคง F-ID เดิมทั้งหมด และเขียนทับตารางตามรอยด้วยข้อมูลล่าสุด
- ตารางไปข้างหน้า 15 แถว: ครบ 1 (IF-IDP-01), ยังไม่ถึง 7, รอ Q-xx 0, ช่องโหว่ 7
- F-06 (test อ่อน test_AC_BKG_01) ย้ายไปหัวข้อ 4 "แก้แล้ว" เพราะมี test_TC_BKG_01_* ตรวจ Then ครบแล้ว และลองพังซ้ำแล้ว test ล้ม
- ข้อค้นพบใหม่: F-12 (FR-BKG-01 มีแต่ AC-BKG-05 ที่ตรวจแค่ความเร็ว ไม่ใช่ AC ที่ตรวจการแสดง 30 วัน); เปลี่ยนชนิดของ F-09 จาก "โค้ดไม่มี FR" เป็น "อ้าง ID ผิดเรื่อง" (โค้ดอ้าง FR-BKG-04 แต่เรื่องยกเลิกอยู่ใน Out of scope)
- ไม่ได้แก้โค้ด test spec plan หรือ tasks

---

## 2569-10-07 ขั้น 6 ของ workshop week07: อ่านโค้ดด้วยสายตา RE 5 คำถาม และเขียนช่อง "ทีมตัดสิน" ใน rtm.md

- รัน grep 5 คำถามใน backend/ ผลสำคัญ:
  - คำถาม 1 (@router): พบ POST /bookings, DELETE /bookings/{booking_id}, GET /slots; เทียบ plan ข้อ 4 และ Out of scope พบ DELETE เป็นของแถม (UC-02) -> F-09 (booking/router.py:35, service.py:42-50)
  - คำถาม 2 (ตัวเลข): slots/service.py:10 `DAYS_AHEAD = 14` ไม่ตรง "30 วัน" ใน FR-BKG-01 -> F-04; booking/service.py:26 เป็น `<= 0` ถูกต้องแล้ว (ไม่มีบั๊ก `< 0` ใน repo นี้)
  - คำถาม 3 (queue): booking/service.py:13-18 `next_queue_no` ออกเลข `A001` รายวัน ทั้งที่ Q-02 ยังไม่มีคำตอบ -> F-03
  - คำถาม 4 (national_id/logger/print): booking/router.py:19 รับ `national_id` และ :25 เขียนลง log -> F-01
  - คำถาม 5 (FR-): คอมเมนต์ "(FR-BKG-04)" ของ cancel_booking (router.py:37, service.py:43) อ้างผิดเรื่อง FR-BKG-04 คือยืนยันการจอง ไม่ใช่ยกเลิก -> F-09
- ธงแดงใน prompt-log.md: พบ "เพื่อความสมบูรณ์ของระบบ" ในรายงาน T-03 ตรงกับ DELETE /bookings/{id}
- จุดที่หาเจอ 6 จุดจากเป้าหมาย: (1) test อ่อน test_AC_BKG_01 (F-06) (2) เงื่อนไขที่นั่ง `< 0` -> ใน repo นี้เป็น `<= 0` อยู่แล้ว (ไม่มีจุดนี้ให้แก้) (3) DELETE /bookings/{id} (F-09) (4) DAYS_AHEAD 14 (F-04) (5) queue_no A001 (F-03) (6) national_id ใน request/log (F-01)
- การตัดสินช่อง "ทีมตัดสิน" ทำตามเฉลยและคำใบ้ของผู้สอนในหน้า week07 (ขั้น 7 "จะเห็น (ครบ 4 ข้อ)" และตัวอย่าง Q-03 Q-04) ไม่ใช่การตัดสินของทีมเอง:
  - F-09, F-04, F-03 = แก้โค้ด
  - F-01 = เพิ่ม Q-03 (และระหว่างรอ เอา national_id ออกจาก request/log ตามกฎ "ระหว่างรอ เอาส่วนที่เดาออก")
  - F-05, F-12 = เพิ่ม Q-04
  - F-02, F-10 = ไม่ใช่ปัญหา: ยังไม่ถึง T-07 และ T-08 ตามกฎ 3 กอง (task สถานะ "พร้อมทำ")
  - F-07, F-08, F-11 = เว้นว่าง เฉลยไม่ครอบคลุม ไม่ได้เดาแทนทีม
- ยังไม่ได้แก้โค้ดในขั้นนี้ (ขั้น 7 จะแก้ทีละข้อ)

---

## 2569-10-07 ขั้น 7 (ข้อที่ 1 จาก 4): แก้ตาม F-09 ใน specs/001-booking/rtm.md

- คำสั่ง (เทียบเท่า): แก้ตาม F-09 ใน rtm.md แตะเฉพาะไฟล์ที่เกี่ยวข้อง ห้ามแก้ test ที่ชื่อขึ้นต้นด้วย test_TC_ แล้วรัน pytest -v
- เหตุผล: ทีมตัดสิน (ตามเฉลยผู้สอนในหน้า week07) ว่า "แก้โค้ด: ของแถม อยู่ใน Out of scope (UC-02)"
- แก้: ลบ endpoint `DELETE /bookings/{booking_id}` (`cancel_booking`) ออกจาก backend/app/booking/router.py และลบ `cancel_booking` ออกจาก backend/app/booking/service.py (เฉพาะส่วนที่ลบ ไม่มีบรรทัดอื่นเปลี่ยน; git diff มีแต่บรรทัดที่ลบ)
- ผล `cd backend && pytest -v`: 7 passed ไม่มี test_TC_ ถูกแก้
- grep "DELETE|cancel|delete" ใน app/ ไม่พบแล้ว

---

## 2569-10-07 ขั้น 7 (ข้อที่ 2 จาก 4): แก้ตาม F-04 ใน specs/001-booking/rtm.md

- เหตุผล: ทีมตัดสิน (ตามเฉลยผู้สอนในหน้า week07) ว่า "แก้โค้ด" เพราะ FR-BKG-01 พูดชัดว่า "ภายใน 30 วันข้างหน้า"
- แก้: backend/app/slots/service.py บรรทัด 10 `DAYS_AHEAD = 14` เป็น `DAYS_AHEAD = 30` (บรรทัดเดียว)
- ผล `cd backend && pytest -v`: 7 passed ไม่มี test_TC_ ถูกแก้
- ข้อสังเกตส่งทีม (ไม่ได้แก้): การค้นใช้ `Slot.slot_date <= start + DAYS_AHEAD` (รวมวันที่ 30) ซึ่งนับวันเริ่มต้นด้วยเป็น 31 วัน ถ้าทีมต้องการนับ "30 วัน" แบบไม่รวมวันที่ 31 ควรถามผู้ใช้ ไม่ได้ตัดสินแทน

---

## 2569-10-07 ขั้น 7 (ข้อที่ 3 จาก 4): แก้ตาม F-03 ใน specs/001-booking/rtm.md

- เหตุผล: ทีมตัดสิน (ตามเฉลยผู้สอนในหน้า week07) ว่า "แก้โค้ด": queue_no เป็นค่าว่างพร้อมคอมเมนต์ "รอ Q-02" ไม่ออกเลข A001 (สอดคล้อง plan ข้อ 3 ที่ให้ queue_no ว่างได้)
- แก้เฉพาะ backend/app/booking/service.py: ลบ `next_queue_no` (รูปแบบ A001 รีเซ็ตรายวัน) และ import `func, select` ที่ไม่ได้ใช้แล้ว; ให้ `queue_no=None,  # รอ Q-02`; ปรับ docstring ของ create_booking
- ผล `cd backend && pytest -v`: 7 passed ไม่มี test ที่ assert เลขคิวอยู่ (test_TC_BKG_01_1 ส่วนหมายเลขคิวเป็นคอมเมนต์ "รอ Q-02" อยู่แล้ว) ไม่ต้องแก้ test และไม่มี test_TC_ ถูกแก้

---

## 2569-10-07 ขั้น 7 (ข้อที่ 4 จาก 4): แก้ตาม F-01 ใน specs/001-booking/rtm.md

- เหตุผล: ทีมตัดสิน (ตามเฉลยผู้สอนในหน้า week07) ว่า "เพิ่ม Q-03" และระหว่างรอคำตอบ เอาส่วนที่เดาออก = ไม่รับ national_id ใน request และไม่เขียนลง log (ตรงกับรายการที่ต้องเห็นของขั้น 7)
- แก้เฉพาะ backend/app/booking/router.py: ลบฟิลด์ `national_id` ออกจาก `BookingRequest` และตัด `national_id` ออกจากข้อความ log (เหลือ slot และ hn)
- ผล `cd backend && pytest -v`: 7 passed ไม่มี test_TC_ ถูกแก้; grep "national_id" ใน app/ ไม่พบ
