# Once-Upon-A-90s/start.sh
#!/bin/bash

echo "🚀 Iniciando 'Once Upon a -90s- API'..."

echo "1. Apagando y eliminando contenedores Docker existentes (si los hay)..."
docker-compose down

echo "2. Asegurando la creación de la carpeta de datos para la DB..."
mkdir -p data

echo "3. Construyendo la imagen Docker del servicio 'api'..."
docker-compose build --no-cache

echo "4. Iniciando el servicio Docker en segundo plano..."
docker-compose up -d

echo "🎉 ¡API Iniciada!"
echo "Puedes acceder a la API en tu navegador o cliente REST en: http://localhost:8080"
echo "Para ver la documentación interactiva (Swagger UI), visita: http://localhost:8080/docs"
echo "Para ver los logs en tiempo real, usa: docker-compose logs -f"
echo "Para detener el servicio, ejecuta: docker-compose down"
