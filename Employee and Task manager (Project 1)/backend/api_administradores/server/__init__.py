from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from Administradores import setup_db, db, Administrador
import jwt

def create_app(test_config = None):
    app = Flask(__name__)
    
    with app.app_context():
        setup_db(app)

    app.config['SECRET_KEY'] = "12345"

    CORS(app)

    @app.after_request
    def after_resquest(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE,OPTIONS')
        return response
    
    @app.route('/administradores', methods=['GET'])
    def administradores():
        administradores = Administrador.query.all()
        return jsonify({
            'success': True,
            'administradores': [administrador.format() for administrador in administradores],
        })

    @app.route('/register/register_admin', methods = ['POST'])
    def register_admin():
        error = False
        response = {}

        try:
            dni_admin = request.get_json()['dni']
            nombres = request.get_json()['nombres']
            apellidos = request.get_json()['apellidos']
            correo = request.get_json()['correo']
            password = request.get_json()['password']
            confirm_password = request.get_json()['cpassword']

            hashed = generate_password_hash(password)

            if check_password_hash(hashed, confirm_password):
                admin = Administrador(
                    dni_admin = dni_admin,
                    nombres = nombres,
                    apellidos = apellidos,
                    correo = correo,
                    password = hashed)
                db.session.add(admin)
                db.session.commit()
                response['success'] = True
                response['admin'] = admin.format()
            else:
                response['success'] = False
                response['message'] = 'Confirm correctly validation password'

        except Exception as exp:
            db.session.rollback()
            error = True
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exp).__name__, exp.args)
            print(message)
            
        finally:
            db.session.close()

        if error:
            abort(500)
        else:
            return jsonify(response)


    @app.route('/login/log_admin', methods = ['POST'])
    def log_admin():
        response = {}
        error = False

        try:
            dni_admin = request.get_json()['dni']
            password = request.get_json()['password']
            admin = Administrador.query.filter_by(dni_admin = dni_admin).first()
            
            if admin is not None and check_password_hash(admin.password, password):
                response['success'] = True
                response['admin'] = admin.format()
                response['token']  = jwt.encode({
                    'dni_admin': dni_admin
                }, app.config['SECRET_KEY'])
            else:
                response['success'] = False
                response['message'] = 'Incorrect dni/password combination'

        except Exception as exp:
            error = True
            response['success'] = False
            response['message'] = 'Exception is raised'
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exp).__name__, exp.args)
            print(message)

        if error:
            abort(500)
        else:
            return jsonify(response)

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'code': 500,
            'message': 'Internal Server Error'
        }), 500

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'code': 404,
            'message': 'resource not found'
        }), 404

    return app  