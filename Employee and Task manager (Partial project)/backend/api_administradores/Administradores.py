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

class Administrador(db.Model):
    dni_admin = db.Column(db.String(8), primary_key = True)
    nombres = db.Column(db.String(100), nullable = False)
    apellidos = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)
    correo = db.Column(db.String(300), nullable = False)
    fecha_anadido = db.Column(db.DateTime(), default = datetime.now)

    def format(self):
        return {
            'dni_admin': self.dni_admin,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'correo': self.correo,
            'password': self.password,
            'fecha_anadido': self.fecha_anadido,
        }

    def get_id(self):
        return (self.dni_admin)

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.dni_admin

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
        return f'Administrador: dni_admin={self.dni_admin}, nombres={self.nombres}, apellidos={self.apellidos}, correo={self.correo}'