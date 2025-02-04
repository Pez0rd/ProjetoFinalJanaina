from flask import render_template, request, redirect, url_for, flash, Blueprint, session
from models.data_manager import cadastro_usuario, login_usuario, adicionar, deletarPedido, load_data_pedidos, adicionaReceita, load_data_receitas, carregaImagem
import requests
import os
# Cria um Blueprint para as rotas
front_controller = Blueprint('front_controller', __name__)
# Blueprint (front_controller) no controlador (front_controller.py) é um módulo que agrupa rotas relacionadas.
# Flask precisa saber que o front_controller existe, então você o registra com app.register_blueprint(front_controller).


YANDEX_API_KEY = "sua_chave_de_api_yandex"

# ---------- Rota Principal ---------- #

@front_controller.route('/')
def index():

    return(render_template('index.html'))

# ---------- Rota Principal ---------- #


# ---------- Rota para Cadastro do Usuário ---------- #

@front_controller.route('/cadastro', methods = ['GET', 'POST'])
def cadastro():
    nome = request.form.get('nomeCadastro') # Recupera o nome para cadastro
    senha = request.form.get('senhaCadastro') # Recupera a senha do usuário

    if(request.method == 'POST'):
        if(cadastro_usuario(nome, senha)): # Função para validar o Cadastro do Usuário
            flash(nome + " Cadastrado com sucesso!")
            return(redirect(url_for('front_controller.login')))
        else:
            flash(nome + " Já possui cadastro!")
            return(redirect(url_for('front_controller.login')))

    return(render_template('cadastro.html'))

# ---------- Rota para Cadastro do Usuário ---------- #





# ---------- Rota para Login do Usuário ---------- #

@front_controller.route('/logar', methods = ['GET', 'POST'])
def login():
    nome = request.form.get('nomeLogin') # Recupera o nome inserido para Login
    senha = request.form.get('senhaLogin') # Recupera a senha do usuário

    if(request.method == "POST"):
        if(login_usuario(nome, senha)): # Função para validar o Login do Usuário
            session['usuarioLogado'] = nome
            flash(nome + " Logado com sucesso!")
            return(render_template('index.html'))
        else:
            flash("Confira seu usuário e/ou senha. Erro de login")
            session['usuarioLogado'] = None
            return(redirect(url_for('front_controller.login')))
        
    return(render_template('login.html'))

# ---------- Rota para Login do Usuário ---------- #





# ---------- Rota para Logout ---------- #

@front_controller.route('/logout', methods = ['GET', 'POST'])
def logout():
    session['usuarioLogado'] = None
    return(redirect(url_for('front_controller.index')))

# ---------- Rota para Logout ---------- #



# ---------- Rota para a página foco do Projeto ---------- #

@front_controller.route('/culinaria')
def culinaria():
    receitas = load_data_receitas() # Recupera as receitas inseridas pelo Usuário
    return(render_template('culinaria.html', receitas = receitas))

# ---------- Rota para a página foco do Projeto ---------- #



# ---------- Rota para adicionar um item ao Carrinho de Compras ---------- #

@front_controller.route('/adicionarCarrinho', methods = ['GET', 'POST'])
def adicionarCarrinho():
    pedido = request.form.get('selecionar') # Recupera o id do item selecionado
    
    if (request.method == 'POST'):
        if(adicionar(pedido)): # Função para aicionar o item no Carrinho de Compras
            flash("Item adicionado com sucesso!")
            return redirect(url_for('front_controller.culinaria'))
    
    return(render_template('adicionar.html'))

# ---------- Rota para adicionar um item ao Carrinho de Compras ---------- #






# ---------- Rota para a página que mostra os itens inseridos no Carrinho de Compra ---------- #

@front_controller.route('/carrinho')
def carrinho():
    carrinhoCompras = load_data_pedidos() # Recupera os pedidos feitos pelo Usuário
    return(render_template('carrinho.html', carrinhoCompras = carrinhoCompras))

# ---------- Rota para a página que mostra os itens inseridos no Carrinho de Compra ---------- #



# ---------- Rota para deletar algum item do Carrinho de Compras ---------- #

@front_controller.route('/deletar/<int:id>', methods = ['GET', 'POST'])
def deletar(id):
    deletarPedido(id) # Função para deletar o item
    return redirect(url_for('front_controller.carrinho'))

# ---------- Rota para deletar algum item do Carrinho de Compras ---------- #



# ---------- Rota para a página de Inserir Receitas ---------- #

@front_controller.route('/inserirReceita')
def inserirReceita():
    return(render_template('adicionarReceita.html'))

# ---------- Rota para a página de Inserir Receitas ---------- #





# ---------- Rota para Adicionar as Receitas do Usuário ---------- #

@front_controller.route('/adicionarReceita', methods=['GET', 'POST'])
def adicionarReceita():
    if (request.method == 'POST'):
        imagemReceita = request.files.get('imagemReceita')  # Recebe o arquivo de imagem
        nomeReceita = request.form.get('nomeReceita')  # Recebe o nome da receita
        ingredientes = request.form.get('ingredientes')  # Recebe os ingredientes

        if imagemReceita and nomeReceita and ingredientes:
            
            if(adicionaReceita(imagemReceita, nomeReceita, ingredientes)):
                flash('Receita adicionada com sucesso!')
                return redirect(url_for('front_controller.culinaria'))
            flash('Nome da receita repetida. Verifique o nome')

        else:
            flash('Erro ao adicionar a receita. Certifique-se de que todos os campos estão preenchidos!')
    
    return render_template('adicionar.html')

# ---------- Rota para Adicionar as Receitas do Usuário ---------- #



#----------Rota da API para traduzir receitas do site--------#
@front_controller.route('/traduzir', methods=['GET', 'POST'])
def traduzir():
    if request.method == 'POST':
        #1--OBTENDO OS DADOS DO FORMULARIO NO HTML--#
        texto_traduzir = request.form.get('texto') #texto dado pelo usuario
        idioma_traduzir = request.form.get('idioma_origem') #idioma do usuario
        idioma_traducao = request.form.get('idioma_destino') #iidoma de destino

        #2--VERIFICA SE O TEXTO FOI INSERIDO--#
        if texto_traduzir:
            langpair = f"{idioma_traduzir}|{idioma_traducao}" #--A API da Apertium espera que os idiomas sejam passados em um formato específico chamado langpair--#
        #------------------------------------------------------#
            #--Fazer a solicitação à API Apertium
            url = "https://apertium.org/apy/translate"
            payload = {
                "langpair": langpair,
                "q": texto_traduzir
            } #--dicionario que contém os parâmetros que serão enviados na solicitação--#
            response = requests.post(url, data=payload)

            #3--VERIFICA A RESPOSTA DA API--#
            if response.status_code == 200:
                resultado = response.json()
                traducao = resultado.get('responseData', {}).get('translatedText', None)#--tenta obter a tradução do JSON retornado pela API--#
                #responseData contém os dados principais da resposta.
                #translatedText é o campo onde a tradução do texto está.

                #4--EXIBE O RESULTADO--#
                if traducao:
                    flash(f"Tradução: {traducao}")
                    return render_template('traduzir.html', traducao=traducao, texto=texto_traduzir)
            else:
                flash("Erro ao traduzir. Tente novamente.")

        else:
            flash("Por favor, insira o texto para tradução.")

    return render_template('traduzir.html')





