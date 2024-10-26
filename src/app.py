from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

"""from flask_cors import CORS"""

from config import config

app=Flask(__name__)

con=MySQL(app)

@app.route("/alumnos", methods=['GET'])
def lista_alumnos():
    try:
        cursor=con.connection.cursor()
        sql='select * from alumnos'
        cursor.execute(sql)
        datos=cursor.fetchall()
        alumnos=[]
        for fila in datos:
            alumno={ 'matricula': fila[0], 'nombre':[1], 'apaterno':[2], 'amaterno':[3], 'correo':[4] }
            alumnos.append(alumno)
            print(alumnos)
        return jsonify({'alumnos': alumnos, 'mensaje': 'Lista de Alumnos', 'exito':True})
    except Exception as ex:
        return jsonify({"message": "Error al conectar a la base de datos {}".format(ex), 'exito':False})

def pagina_no_encontrada(error):
    return '<h1> La página que estas buscando no existe </h1>', 400

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host='0.0.0.0', port=5000)