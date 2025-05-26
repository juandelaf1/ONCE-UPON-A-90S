# Once-Upon-A-90s/Dockerfile

# Usar una imagen base oficial de Python ligera (basada en Debian Buster)
# Esta imagen ya viene con Python preinstalado.
FROM python:3.9-slim-buster

# Establecer el directorio de trabajo dentro del contenedor.
# Aquí es donde se copiará el código de tu aplicación.
WORKDIR /app

# Copiar el archivo de requisitos al directorio de trabajo en el contenedor.
# Esto se hace primero para aprovechar el cache de Docker. Si requirements.txt no cambia,
# Docker no reinstalará las dependencias, lo que acelera las futuras construcciones.
COPY requirements.txt .

# Instalar las dependencias de Python listadas en requirements.txt.
# --no-cache-dir: No guarda el caché de pip, lo que reduce el tamaño de la imagen.
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación (todos los archivos en el directorio actual)
# al directorio de trabajo '/app' dentro del contenedor.
COPY . .

# Exponer el puerto en el que la aplicación FastAPI escuchará.
# Esto es informativo para Docker, no publica el puerto al host.
EXPOSE 8000

# Comando para ejecutar la aplicación cuando el contenedor se inicie.
# uvicorn: El servidor ASGI que ejecuta FastAPI.
# main:app: Indica a Uvicorn que busque el objeto 'app' dentro del archivo 'main.py'.
# --host 0.0.0.0: Permite que el servidor sea accesible desde cualquier interfaz de red,
#                  no solo localhost dentro del contenedor, lo cual es necesario para Docker.
# --port 8000: Especifica que la aplicación escuchará en el puerto 8000 dentro del contenedor.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]