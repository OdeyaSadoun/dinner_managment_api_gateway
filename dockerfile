FROM python:3.12

RUN apt-get update && apt-get install -y \
    imagemagick \
    libffi-dev \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ENV PYTHONPATH="/src"
