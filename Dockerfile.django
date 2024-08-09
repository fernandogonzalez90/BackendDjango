# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos e instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código del proyecto
COPY . .

# Ejecuta las migraciones y colecta archivos estáticos
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --noinput

# Exponer el puerto en el que Gunicorn escuchará
EXPOSE 8000

# Configura el comando para iniciar Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Backend.wsgi:application"]