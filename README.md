# FinTech Solutions - Full Stack App

## Descripción
Aplicación web segura para gestión financiera con tres capas (Frontend, Backend, Base de datos) utilizando Docker y Flask. 

## Tecnologías
- **Backend**: Python, Flask, SQLAlchemy, psycopg2
- **Base de datos**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript (Formulario de login)
- **Docker**: Para contenerizar los servicios

## Instrucciones para ejecutar

### 1. Clonar el repositorio:
```bash
git clone <url_del_repositorio>
cd fintech-app
```

## Construir y ejecutar los contenedores
- docker-compose build
- docker-compose up

## Subir imágenes a Docker Hub
- docker login
- docker build -t myusername/backend ./backend
- docker push myusername/backend
- docker build -t myusername/frontend ./frontend
- docker push myusername/frontend
