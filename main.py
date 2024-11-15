from fastapi import FastAPI
from pydantic import BaseModel
from aift.multimodal import textqa
from aift import setting
from dotenv import load_dotenv
import os

load_dotenv()

# กำหนดค่า API Key
api_key = os.getenv("API_KEY")
setting.set_api_key(api_key)

# สร้าง FastAPI app
app = FastAPI()

# สร้างโมเดลเพื่อรับคำถามในรูปแบบ JSON
class Question(BaseModel):
    question: str

# สร้าง endpoint สำหรับ POST ข้อความคำถาม
@app.post("/ask")
async def ask_question(data: Question):
    # เรียกใช้ฟังก์ชัน generate ของ aift เพื่อสร้างคำตอบ
    response = textqa.generate(data.question, return_json=False)
    return {"question": data.question, "answer": response}
