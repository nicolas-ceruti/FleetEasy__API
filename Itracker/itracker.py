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

mydb = mysql.connector.connect(
 host="localhost",
 port="3306",
 user="root",
 password="",
 database="mydb"
)

#-----------------G E T --------------------------------

@app.route("/getUsuarios", methods=["GET"])
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
  try: 
    sql="SELECT * FROM motoristas"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    usuarios = mycursor.fetchall()
    return (usuarios)
  except Exception as ex:
    return (error_error())

@app.route("/getVeiculos", methods=["GET"])
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
def getColetas():
  try: 
    sql="SELECT * FROM registrocoleta"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    usuarios = mycursor.fetchall()
    return (usuarios)
  except Exception as ex:
    return (error_error())

#-----------------P O S T --------------------------------

@app.route("/login", methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def login():
  try:
    data = request.get_json() 
    sql=f"SELECT * FROM usuario WHERE email='{data['email']}' AND senha='{data['senha']}'"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    usuarios = mycursor.fetchall()
    if (usuarios) != nullcontext:
      return ("ok")
    else:
      return ("ff")
  except Exception as ex:
    return (error_error())


@app.route("/createUsuario", methods=["POST"])
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
def createMotorista():
  try:
    data = request.get_json()
    sql=f"INSERT INTO motoristas (nomeCompleto, senha, email, cpf, rg, telefone, latitude, longitude, cnh) VALUES "
    sql = sql + f"('{data['nomeCompleto']}', '{data['senha']}', '{data['email']}', '{data['cpf']}', '{data['rg']}'," 
    sql = sql + f" '{data['telefone']}', '{data['latitude']}', '{data['longitude']}', '{data['cnh']}')"
    mycursor = mydb.cursor().execute(sql)
    return ("Motorista Cadastrado com Sucesso!")
  except Exception as ex:
    data = request.get_json
    return (error_error())


@app.route("/createVeiculo", methods=["POST"])
def createVeiculo():
  try:
    data = request.get_json()
    sql=f"INSERT INTO veiculo (placa, cor, ano, marca, tipo, modelo, chassi, capacidadePeso, capacidadeVolumetria) VALUES "
    sql = sql + f"('{data['placa']}', '{data['cor']}', '{data['ano']}', '{data['marca']}', '{data['tipo']}'," 
    sql = sql + f" '{data['modelo']}', '{data['chassi']}', '{data['capacidadePeso']}', '{data['capacidadeVolumetria']}')"
    mycursor = mydb.cursor().execute(sql)
    return ("Veículo Cadastrado com Sucesso!")
  except Exception as ex:
    data = request.get_json
    return (error_error())

@app.route("/createColeta", methods=["POST"])  #BAD
def createColeta():
  try:
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
  except Exception as ex:
    data = request.get_json
    return (error_error())


#-----------------P U T --------------------------------

@app.route("/putUsuario", methods=["PUT"])
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
    
