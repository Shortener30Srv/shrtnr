FROM python:3.10

# 
WORKDIR /app_shortener

# 
COPY /requirements.txt requirements.txt

# 
RUN  pip install --upgrade pip \
     && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]
