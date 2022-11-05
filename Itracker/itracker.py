from contextlib import nullcontext
from urllib import response
import mysql.connector
from flask import Flask
from flask_mysqldb import MySQL
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from flask_swagger_ui import get_swaggerui_blueprint
import json


app = Flask(__name__)
CORS(app)

mydb = mysql.connector.connect(
 host="localhost",
 port="3307",
 user="root",
 password="",
 database="itracker"
)

#-----------------G E T --------------------------------

@app.route("/getUsuarios", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization', 'Access-Control-Allow-Origin'])
def getUsuarios():
  try: 
    sql="SELECT * FROM usuario"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    usuarios = mycursor.fetchall()
    return (usuarios)
  except Exception as ex:
    return (error_error())

@app.route("/getMotoristas", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def getMotoristas():
 
    
    sql="SELECT * FROM motoristas"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    dataMotoristas = mycursor.fetchall()
    usuarios_data = []
    for row in dataMotoristas:
      id = row[0]
      usuarios_list = {
        "idMotorista" : row[0],
        "nomeCompleto" : row[1],
        "senha" : row[2],
        "email" : row[3],
        "cpf" : row[4],
        "rg" : row[5],
        "telefone" : row[6],
        "latitude" : row[7],
        "longitude" : row[8],
        "cnh" : row[9],
      }
      usuarios_data.append(usuarios_list)
   
    return (usuarios_data)
 

@app.route("/getVeiculos", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def getVeiculos():
  try: 
    sql="SELECT * FROM veiculo"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    usuarios = mycursor.fetchall()
    return (usuarios)
  except Exception as ex:
    return (error_error())

@app.route("/getColetas", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def getColetas():
  try: 
    sql="SELECT * FROM registrocoleta"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    dataMotoristas = mycursor.fetchall()
    usuarios_data = []
    for row in dataMotoristas:
      id = row[0]
      usuarios_list = {
        "idRegistroColeta" : row[0],
        "dataColeta" : row[1],
        "horaColeta" : row[2],
        "estadoColeta" : row[3],
        "cidadeColeta" : row[4],
        "bairroColeta" : row[5],
        "ruaColeta" : row[6],
        "numeroColeta" : row[7],
        "dataEntrega" : row[8],
        "horaEntrega" : row[9],
        "estadoEntrega" : row[10],
        "cidadeEntrega" : row[11],
        "bairroEntrega" : row[12],
        "ruaEntrega" : row[13],
        "numeroEntrega" : row[14],
        "nomeCliente" : row[15],
        "cnpjCliente" : row[16],
        "emailCliente" : row[17],
        "telefoneCliente" : row[18],
        "pesoCarga" : row[19],
        "volumeCarga" : row[20],
        "valorCarga" : row[21],
        "Ocorrencia_idOcorrencia" : row[22],
        "Motoristas_idMotorista" : row[23],
    }
    usuarios_data.append(usuarios_list)
   
    return (usuarios_data)
  except Exception as ex:
    return (error_error())

#-----------------P O S T --------------------------------

@app.route("/login", methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization', 'Access-Control-Allow-Origin'])
def login():
  try:
    print ("--------------------------------------------")
    data = request.get_json(force=True) 
    sql=f"SELECT * FROM usuario WHERE email='{data['email']}' AND senha='{data['senha']}'"
    print (data['senha'])
    mydb.reconnect()
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    dataMotoristas = mycursor.fetchall()
    if (dataMotoristas):
      return{"mensagem" : "Existe"}
    else:
      return {"mensagem" : "Não Existe"}
  except Exception as ex:
    return (error_error())


@app.route("/createUsuario", methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def createUsuario():
  try:
    data = request.get_json()
    sql=f"INSERT INTO usuario (email, senha, nome) VALUES "
    sql = sql + f"('{data['email']}', '{data['senha']}','{data['nome']}')"
    mycursor = mydb.cursor().execute(sql)
    return ("Usuário Cadastrado com Sucesso!")
  except Exception as ex:
    data = request.get_json
    return (error_error())


@app.route("/createMotorista", methods=["POST"])
@cross_origin(origin='*',headers=['Authorization'])
def createMotorista():

  print ("--------------------------------------------")
  data = request.get_json(force=True) 
  sql=f"""
    INSERT INTO motoristas (nomeCompleto, senha, email, cpf, rg, telefone, latitude, longitude, cnh) VALUES 
    ('{data['nomeCompleto']}', '{data['senha']}', '{data['email']}', '{data['cpf']}', '{data['rg']}',
      '{data['telefone']}', '{data['latitude']}', '{data['longitude']}', '{data['cnh']}')
  """
  mydb.reconnect()
  mycursor = mydb.cursor()
  try:
    mycursor.execute(sql)
    return{"mensagem" : "Cadastrado"}

  except Exception as ex:
    return {"mensagem" : error_error()}
    

 
 



@app.route("/createVeiculo", methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def createVeiculo():

  print ("--------------------------------------------")
  data = request.get_json(force=True) 
  sql=f"""
    INSERT INTO veiculo (placa, cor, ano, marca, tipo, modelo, chassi, capacidadePeso, capacidadeVolumetria) VALUES
    ('{data['placa']}', '{data['cor']}', '{data['ano']}', '{data['marca']}', '{data['tipo']}',
      '{data['modelo']}', '{data['chassi']}', '{data['capacidadePeso']}', '{data['capacidadeVolumetria']}')
  """
  mydb.reconnect()
  mycursor = mydb.cursor()
  try:
    mycursor.execute(sql)
    return{"mensagem" : "Cadastrado"}

  except Exception as ex:
    return {"mensagem" : error_error()}



@app.route("/createColeta", methods=["POST"])  #BAD
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def createColeta():
  # try:
  data = request.get_json()
  sql=f"INSERT INTO registrocoleta (dataColeta, horaColeta, estadoColeta, cidadeColeta, bairroColeta, ruaColeta, numeroColeta,"
  sql= sql + f" dataEntrega, horaEntrega, estadoEntrega, cidadeEntrega, bairroEntrega, ruaEntrega, numeroEntrega,"
  sql= sql + f" nomeCliente, cnpjCliente, emailCliente, telefoneCliente, pesoCarga, volumeCarga, valorCarga, Ocorrencia_idOcorrencia, Motoristas_idMotorista) VALUES "
  sql = sql + f"('{data['dataColeta']}', '{data['horaColeta']}', '{data['estadoColeta']}', '{data['cidadeColeta']}', '{data['bairroColeta']}', '{data['ruaColeta']}', '{data['numeroColeta']}'," 
  sql = sql + f" '{data['dataEntrega']}', '{data['horaEntrega']}', '{data['estadoEntrega']}', '{data['cidadeEntrega']}', '{data['bairroEntrega']}', '{data['ruaEntrega']}', '{data['numeroEntrega']}',"
  sql = sql + f" '{data['nomeCliente']}', '{data['cnpjCliente']}', '{data['emailCliente']}', '{data['telefoneCliente']}', '{data['pesoCarga']}', '{data['volumeCarga']}', '{data['valorCarga']}',"
  sql = sql + f" '{data['Ocorrencia_idOcorrencia']}', '{data['Motoristas_idMotorista']}')"
  mycursor = mydb.cursor().execute(sql)
  return ("Coleta Cadastrado com Sucesso!")
  # except Exception as ex:
  #   data = request.get_json
  #   return (error_error())


#-----------------P U T --------------------------------

@app.route("/putUsuario", methods=["PUT"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def putUsuario():
  try:
    data = request.get_json()
    sql=f"UPDATE usuario SET "
    sql = sql + f"email='{data['email']}', senha='{data['senha']}', nome='{data['nome']}' WHERE id={data['id']}"
    mycursor = mydb.cursor().execute(sql)
    return ("Usuário Editado com Sucesso!")
  except Exception as ex:
    data = request.get_json
    return (error_error())


@app.route("/putMotorista", methods=["PUT"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def putMotorista():
  try:
    data = request.get_json()
    sql=f"UPDATE motoristas SET "
    sql = sql + f"nomeCompleto='{data['nomeCompleto']}', senha='{data['senha']}', email='{data['email']}', cpf='{data['cpf']}', rg='{data['rg']}'," 
    sql = sql + f" telefone='{data['telefone']}', latitude='{data['latitude']}', longitude='{data['longitude']}', cnh='{data['cnh']}' WHERE id={data['id']}"
    mycursor = mydb.cursor().execute(sql)
    return ("Motorista Editado com Sucesso!")
  except Exception as ex:
    data = request.get_json
    return (error_error())


@app.route("/putCoordenadas", methods=["PUT"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def putCoordenadas():
  try:
    data = request.get_json()
    sql=f"UPDATE motoristas SET "
    sql = sql + f" latitude='{data['latitude']}', longitude='{data['longitude']}' WHERE id={data['id']}"
    mycursor = mydb.cursor().execute(sql)
    return ("Motorista Editado com Sucesso!")
  except Exception as ex:
    data = request.get_json
    return (error_error())


@app.route("/putVeiculo", methods=["PUT"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def putVeiculo():
  try:
    data = request.get_json()
    sql=f"UPDATE veiculo SET  "
    sql = sql + f"placa='{data['placa']}', cor='{data['cor']}', ano='{data['ano']}', marca='{data['marca']}', tipo='{data['tipo']}'," 
    sql = sql + f" modelo='{data['modelo']}', chassi='{data['chassi']}', capacidadePeso='{data['capacidadePeso']}', capacidadeVolumetria='{data['capacidadeVolumetria']}' WHERE id={data['id']}"
    mycursor = mydb.cursor().execute(sql)
    return ("Veículo Editado com Sucesso!")
  except Exception as ex:
    data = request.get_json
    return (error_error())


@app.route("/putColeta", methods=["PUT"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def putColeta():
  try:
    data = request.get_json()
    sql=f""" UPDATE registrocoleta SET  
    dataColeta='{data['dataColeta']}', horaColeta='{data['horaColeta']}', estadoColeta='{data['estadoColeta']}', cidadeColeta='{data['cidadeColeta']}', 
    bairroColeta='{data['bairroColeta']}', ruaColeta='{data['ruaColeta']}', numeroColeta='{data['numeroColeta']}', 
    dataEntrega='{data['dataEntrega']}', horaEntrega='{data['horaEntrega']}', estadoEntrega='{data['estadoEntrega']}', cidadeEntrega='{data['cidadeEntrega']}', 
    bairroEntrega='{data['bairroEntrega']}', ruaEntrega='{data['ruaEntrega']}', numeroEntrega='{data['numeroEntrega']}',
    nomeCliente='{data['nomeCliente']}', cnpjCliente='{data['cnpjCliente']}', emailCliente='{data['emailCliente']}', telefoneCliente='{data['telefoneCliente']}', 
    pesoCarga='{data['pesoCarga']}', volumeCarga='{data['volumeCarga']}', valorCarga='{data['valorCarga']}' WHERE id={data['id']}"""
    mycursor = mydb.cursor().execute(sql)
    return ("Veículo Editado com Sucesso!")
  except Exception as ex:
    data = request.get_json
    return (error_error())


@app.route("/update", methods=["PUT"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def update():
  try:
    data = request.get_json()
    sql=f"UPDATE usuarios SET nome='{data['nome']}', email='{data['email']}', senha='{data['senha']}', profissao='{data['profissao']}' WHERE id={data['id']}"
    mycursor = mydb.cursor().execute(sql)
    return ("Usuário editado com sucesso!")
  except Exception as ex:
    data = request.get_json
    return (error_error())





@app.route("/getOne/<id>", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def one(id):
  try:
    sql="SELECT * FROM usuarios WHERE id =" + id
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    usuarios = mycursor.fetchall()
    return (usuarios)
  except Exception as ex:
    return (error_error())



@app.route("/delete", methods=["DELETE"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def delete():
  try:
    data = request.get_json()
    sql=f"DELETE FROM usuarios WHERE id ={data['id']}"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    return ("Usuário Deletado com sucesso!")
  except Exception as ex:
    return (error_error()) 



@app.route("/create", methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def create():
  try:
    data = request.get_json()
    sql=f"INSERT INTO usuarios (nome, email, senha, profissao) VALUES ('{data['nome']}', '{data['email']}','{data['senha']}', '{data['profissao']}')"
    mycursor = mydb.cursor().execute(sql)
    return ("Usuário Criado com Sucesso!")
  except Exception as ex:
    data = request.get_json
    return (error_error())






def error_error():       
    return jsonify({"mensagem": "Não foi possível concluir a ação!"})



@app.route("/static/<path:path>")  #Documentação OPENAPI/Swagger
def send_static(path):
  return send_from_directory('static', path)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
  SWAGGER_URL,
  API_URL,
  config={
    'app_name' : 'API'
  }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


if __name__ == '__main__':
    app.run(DEBUG=True)
    
