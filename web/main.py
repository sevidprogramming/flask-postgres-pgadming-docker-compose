from flask import Flask,jsonify
from sqlalchemy import create_engine 
from faker import Faker
app = Flask(__name__)
connection_db = "postgresql://postgres_user:postgrespwd1@db:5432/postgresdb"
app.config["SQLALCHEMY_DATABASE_URI"] = connection_db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine(connection_db)

@app.route('/insertar_datos',methods=["POST"])
def insertar_datos():
    fake = Faker()
    try:
        for i in range(10):
            nombre = fake.name()
            telefono = fake.phone_number()
            engine.execute(f""" INSERT INTO usuarios(nombre,telefono) values ('{nombre}','{telefono}') """)
    except:
        return jsonify({"Respuesta":"No se inserto"})
    return jsonify({"Respuesta":"Datos insertados!!"})
@app.route('/creartabla',methods=["POST"])
def crear_tabla():
    try:
        engine.execute("CREATE TABLE IF NOT EXISTS usuarios(id serial, nombre varchar(200),telefono varchar(200))")
    except:
        return jsonify({"Respuesta":"FALLE"})
    return jsonify({"Respuesta":"Tabla creada exitosamente"})

if __name__=="__main__":
    app.run(host="0.0.0.0",port=80)