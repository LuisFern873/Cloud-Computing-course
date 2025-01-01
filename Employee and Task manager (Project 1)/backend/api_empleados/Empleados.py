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

class Empleado(db.Model):
    dni_empleado = db.Column(db.String(8), primary_key = True)
    nombres = db.Column(db.String(50), nullable = False)
    apellidos = db.Column(db.String(50), nullable = False)
    genero = db.Column(db.String(1), nullable = False)
    fecha_anadido = db.Column(db.DateTime(), default = datetime.now)
    fecha_modificado = db.Column(db.DateTime(), nullable = True, default = None)
    admin = db.Column(db.String(8), nullable = False)

    # admin = db.Column(db.String(8), db.ForeignKey('administrador.dni_admin'))
    # tareas = db.relationship('Tarea', backref = 'empleado')

    def format(self):
        return {
            'dni_empleado': self.dni_empleado,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'genero': self.genero,
            'fecha_anadido': self.fecha_anadido,
            'fecha_modificado': self.fecha_modificado,
            'admin': self.admin,
        }

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.dni_empleado

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
        return f'Empleado: dni_empleado={self.dni_empleado}, nombres={self.nombres}, apellidos={self.apellidos}, genero={self.genero}, fecha_añadido={self.fecha_anadido}'