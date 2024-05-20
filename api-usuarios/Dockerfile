FROM python:3-slim
WORKDIR /programas/api-usuarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["fastapi", "run", "./app.py", "--port", "80"]