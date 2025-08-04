FROM python:3.13-slim

RUN apt-get update;\
    apt-get full-upgrade -y; \
    rm -rf /var/lib/apt/lists/*

RUN pip install playwright && \
    playwright install && \
    playwright install-deps

COPY screenshot.py /app/screenshot.py

WORKDIR /app

ENTRYPOINT ["python", "screenshot.py"]
