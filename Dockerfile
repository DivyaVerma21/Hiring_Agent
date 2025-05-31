
FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip install streamlit

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]