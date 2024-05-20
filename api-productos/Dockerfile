FROM python:3-slim
WORKDIR /programas/api-productos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["fastapi", "run", "./main.py", "--port", "8000"]