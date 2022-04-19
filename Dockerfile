FROM python:3.10.4-slim

RUN useradd --create-home --shell /bin/bash census

WORKDIR /home/census

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

USER census

COPY . .

CMD ["bash"]
