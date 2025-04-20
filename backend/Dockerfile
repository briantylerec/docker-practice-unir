# Usar una imagen base de Python
FROM python:3.9-slim

# Configurar el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt en el contenedor
COPY requirements.txt /app/

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación
COPY . /app/

# Exponer el puerto 5000 para que la aplicación sea accesible
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
