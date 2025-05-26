# Once-Upon-A-90s/Dockerfile
FROM python:3.9-slim-buster

# Establecer el directorio de trabajo dentro del contenedor.
WORKDIR /app

# Copiar el archivo de requisitos al directorio de trabajo en el contenedor.
COPY requirements.txt .

# Instalar las dependencias de Python listadas en requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación (todos los archivos en el directorio actual)
COPY . .

# Exponer el puerto en el que la aplicación FastAPI escuchará.
EXPOSE 8000

# Comando para ejecutar la aplicación cuando el contenedor se inicie.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
