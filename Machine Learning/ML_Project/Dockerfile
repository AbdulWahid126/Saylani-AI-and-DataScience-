FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860
EXPOSE 8000

CMD uvicorn app:app --host 0.0.0.0 --port 8000 & streamlit run frontend.py --server.port 7860 --server.address 0.0.0.0