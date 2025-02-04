import os
import json
import config
import requests

#-- Funções para manipular arquivos
def load_data_dados():
    if not os.path.exists(config.DATA_FILE):
        return [ ]
    with open(config.DATA_FILE, "r") as file:
        return (json.load(file))
        
 
def save_data_dados(data):
    with open(config.DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
        
        
def load_data_pedidos():
    if not os.path.exists(config.DATA_FILE_PEDIDOS):
        return [ ]
    with open(config.DATA_FILE_PEDIDOS, "r") as file:
        return (json.load(file))    
 
def save_data_pedidos(data):
    with open(config.DATA_FILE_PEDIDOS, "w") as file:
        json.dump(data, file, indent=4)


def load_data_receitas():
    if not os.path.exists(config.DATA_FILE_RECEITAS):
        return [ ]
    with open(config.DATA_FILE_RECEITAS, "r") as file:
        return (json.load(file))
        
 
def save_data_receitas(data):
    with open(config.DATA_FILE_RECEITAS, "w") as file:
        json.dump(data, file, indent=4)
        
#----------------------------------------------------------------------------------------------------


usuarios = []
pedidos = []
receitas = []
dummy = []

def cadastro_usuario(nome, senha):
    usuarioCadastrado = False

    for i in load_data_dados():
        if(nome == i['nome']):
            usuarioCadastrado = True

    if(usuarioCadastrado == True):
        return False
    else:
        usuarios.append(
            {'nome': nome,
            'senha': senha
            }
        )
        save_data_dados(usuarios) 
        return True
    
def login_usuario(nome, senha):
    for i in load_data_dados():
        if(nome == i['nome'] and senha == i['senha']):
            return True   
    
    return False
    
        
def recupera_itens_armazenados():
    
    #retorna todos os itens armazenados.
    return load_data_dados()

def adicionar(pedido):
    # Carregar os pedidos armazenados
    pedidos = load_data_pedidos()

    # Definir o id como o maior id existente + 1, ou 1 se a lista estiver vazia
    id = max([item['id'] for item in pedidos], default=0) + 1

    # Adicionar o novo pedido
    pedidos.append({'id': id, 'pedido': pedido})

    # Salvar a lista de pedidos atualizada
    save_data_pedidos(pedidos)

    return True


def deletarPedido(idPedido):
    # Carregar os pedidos
    pedidos = load_data_pedidos()

    # Filtrar os pedidos para remover o pedido com o id fornecido
    pedidos = [item for item in pedidos if item['id'] != idPedido]

    # Salvar a lista de pedidos atualizada (sem o pedido excluído)
    save_data_pedidos(pedidos)
    
def carrinhoCompras():
    return(load_data_pedidos())

def adicionaReceita(imagemReceita, nomeReceita, ingredientes):
    load_data_receitas()

    for i in load_data_receitas():
        if(nomeReceita == i['nomeReceita']):
            return False

    ingredientes = ingredientes.strip()
    ingredientes = ingredientes.split("\n")

    receitas.append(
        {'nomeReceita': nomeReceita,
         'ingredientes': ingredientes,
         'imagemReceita': carregaImagem(imagemReceita, nomeReceita)}
    )

    save_data_receitas(receitas)

    return True



UPLOAD_FOLDER = config.UPLOAD_FOLDER
TIPO_IMAGEM = config.TIPO_IMAGEM

def carregaImagem(imagemReceita, nomeReceita):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    extension = imagemReceita.filename.rsplit('.', 1)[1].lower()
    
    unique_filename = f"{nomeReceita}.{extension}"
    filepath = os.path.join(UPLOAD_FOLDER, unique_filename)

    imagemReceita.save(filepath)
    
    return os.path.normpath(f"uploads/image/{unique_filename}").replace("\\", "/")

def verificaArquivos(imagemReceita):
    return '.' in imagemReceita.filename and imagemReceita.filename.rsplit('.', 1)[1].lower() in TIPO_IMAGEM