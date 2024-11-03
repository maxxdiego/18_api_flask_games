from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os

load_dotenv()

# Criando a instância do Flask
app = Flask(__name__)

# Definindo o endereço do banco
app.config["MONGO_URI"] = f'mongodb+srv://{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}@cluster0.v2pgk.mongodb.net/{os.getenv("DB_NAME")}?retryWrites=true&w=majority&appName=Cluster0'

# Criando a instância de Api do flask_restful e passando o Flask
api = Api(app)

# Criando a instância do PyMongo
mongo = PyMongo(app)

# Criando a instância do Marshmallow
ma = Marshmallow(app)

from .resources import game_resource