from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

database_path = 'mysql://{}:{}@{}:{}/{}'.format(
    'admin', # Username
    'pt9vfW7tYQJPxI5U5o6C', # Password
    'database-1.czmlp3xton0a.us-east-1.rds.amazonaws.com', # Host
    '3306', # Port
    'tambo' # Database
)

def setup_db(app, database_path = database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Tarea(db.Model):
    id_tarea = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(50), nullable = True)
    descripcion = db.Column(db.String(500), nullable = True)
    completo = db.Column(db.Boolean, nullable = False)
    asignado = db.Column(db.String(8), nullable = False) # empleado.dni_empleado 

    def format(self):
        return {
            'id_tarea': self.id_tarea,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'completo': self.completo,
            'asignado': self.asignado
        }

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id_tarea
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def __repr__(self):
        return f'Tarea: id_tarea={self.id_tarea}, titulo={self.titulo}, descripcion={self.descripcion}, completado={self.completo}, asignado={self.asignado}'
