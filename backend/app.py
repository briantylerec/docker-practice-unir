from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Importar CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/fintech_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Habilitar CORS para todas las rutas
CORS(app, resources={r"/*": {"origins": "http://localhost"}})  # Cambia la URL del frontend si es necesario

# Modelo de usuario
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Ruta para login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Crear la base de datos y agregar un usuario por defecto
if __name__ == "__main__":
    with app.app_context():  # Contexto de la aplicación
        db.create_all()  # Crear las tablas de la base de datos

        # Verificar si el usuario ya existe
        existing_user = User.query.filter_by(username='brianmora').first()
        if not existing_user:
            # Si no existe, agregar un nuevo usuario
            new_user = User(username='brianmora', password='123456')
            db.session.add(new_user)
            db.session.commit()
            print("Usuario 'brianmora' creado exitosamente.")
    
    app.run(host="0.0.0.0", port=5000)
