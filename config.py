import os

#Diretórios para arquivo JSON

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "imgReceitas")
TIPO_IMAGEM = {'jpeg'}

DATA_FILE = os.path.join(BASE_DIR, "models", "data", "dados.json")
DATA_FILE_PEDIDOS = os.path.join(BASE_DIR, "models", "data", "pedidos.json" )
DATA_FILE_RECEITAS = os.path.join(BASE_DIR, "models", "data", "receitas.json" )