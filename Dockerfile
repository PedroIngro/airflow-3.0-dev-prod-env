# Dockerfile
FROM apache/airflow:3.0.0

# Copia os requirements para dentro da imagem
COPY requirements.txt /requirements.txt

# Instala os requisitos adicionais de forma permanente na imagem
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r /requirements.txt
