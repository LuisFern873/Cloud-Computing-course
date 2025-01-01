from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from Tareas import setup_db, db, Tarea

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

    @app.route('/tareas', methods = ['GET'])
    def tareas():
        tareas = Tarea.query.all()
        return jsonify({
            'success': True,
            'tareas': [tarea.format() for tarea in tareas]
        })

    @app.route('/tareas/update_tarea/<id>', methods = ['PATCH'])
    def update_tarea(id):
        # Tarea que va ser completada
        tarea = Tarea.query.filter_by(id_tarea = id)
        if tarea is None:
            abort(404)
        # Tarea marcada como completa
        tarea.update({'completo': True})
        db.session.commit()

        return jsonify({
            'success': True,
            'tarea': tarea.format()
        })

    @app.route('/tareas/asignar_tarea/<dni>', methods = ['POST'])
    def asignar_tarea(dni):
        # Recuperar datos de la tarea
        titulo = request.get_json()["titulo"]
        descripcion = request.get_json()["descripcion"]

        # Creamos la tarea
        tarea = Tarea(
            titulo = titulo,
            descripcion = descripcion,
            completo = False,
            empleado = dni
        )
        # Añadimos la tarea
        db.session.add(tarea)
        db.session.commit()

        # Respuesta
        return jsonify({
            'success': True, 
            'tarea': tarea.format()
        })
    
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