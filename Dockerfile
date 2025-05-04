FROM python:latest

# Establecer directorio de trabajo
RUN mkdir /app
WORKDIR /app

# Copiar archivos al docker
COPY . /app

# Instalar Dependencias
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Punto de entrada
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]