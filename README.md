docker build -t fastapi-service .

docker run -p 5645:5645 fastapi-service

คุณจะสามารถเข้าถึง service ได้ที่ http://localhost:5645/ask