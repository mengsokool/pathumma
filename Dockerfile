# ใช้ Python 3.9 เป็น base image
FROM python:3.9-slim

# ตั้งค่า working directory
WORKDIR /app

# ติดตั้ง dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy โค้ดแอพพลิเคชันเข้าไปใน container
COPY . .

# Expose port 5645
EXPOSE 5645

# รัน FastAPI ด้วย uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5645"]
