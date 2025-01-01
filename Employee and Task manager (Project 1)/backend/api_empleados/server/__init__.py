from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from Empleados import setup_db, db, datetime, Empleado

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

    @app.route('/empleados', methods=["GET"])
    def empleados():
        empleados = Empleado.query.all()
        return jsonify({
            'success': True,
            'empleados': [empleado.format() for empleado in empleados],
        })

    @app.route('/empleados/new_empleado', methods=["POST"])
    def new_empleado():
        error = False
        response = {}
        try:
            dni_empleado = request.get_json()['dni_empleado']
            nombres = request.get_json()['nombres']
            apellidos = request.get_json()['apellidos']
            genero = request.get_json()['genero']
            admin = request.get_json()['admin']

            empleado = Empleado(
                dni_empleado = dni_empleado,
                nombres = nombres,
                apellidos = apellidos,
                genero = genero,
                admin = admin
            )
            db.session.add(empleado)
            db.session.commit()
            response['success'] = True
            response['empleado'] = empleado.format()
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

    @app.route('/empleados/delete_empleado/<dni>', methods=['DELETE'])
    def delete_empleado(dni):
        error = False
        response = {}
        try:
            # Tarea.query.filter_by(asignado = dni).delete()
            Empleado.query.filter_by(dni_empleado = dni).delete()
 
            db.session.commit()
            response['success'] = True
            response['admin'] = dni

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

    @app.route('/empleados/update_empleado/<dni>', methods=['PATCH'])
    def update_empleado(dni):
        error = False
        response = {}

        try:
            edit_dni_empleado = request.get_json()["edit_dni_empleado"]
            edit_nombres = request.get_json()["edit_nombres"]
            edit_apellidos = request.get_json()["edit_apellidos"]

            empleado = Empleado.query.filter_by(dni_empleado = dni)

            if edit_dni_empleado != "":
                empleado.update({'dni_empleado': edit_dni_empleado})
            else:
                response['mensaje_error'] = 'Ingrese un dni valido'

            if edit_nombres != "":
                empleado.update({'nombres': edit_nombres})
            else:
                response['mensaje_error'] = 'Ingrese un nombre valido'            

            if edit_apellidos != "":
                empleado.update({'apellidos': edit_apellidos})
            else:
                response['mensaje_error'] = 'Ingrese un apellido valido'            

            empleado.update({'fecha_modificado': datetime.now()})
            db.session.commit()

            response['dni_empleado'] = dni

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