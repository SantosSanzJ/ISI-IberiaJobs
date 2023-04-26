FROM python:3.9

WORKDIR /app
# Copiar el archivo HTML al directorio de trabajo del contenedor
COPY . /app/

ENV FLASK_APP=src/stats.py

# Instalar las dependencias necesarias
RUN pip install -r requirements.txt

# Exponer el puerto 5000
EXPOSE 5000
