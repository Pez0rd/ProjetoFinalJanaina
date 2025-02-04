# Projeto Culinária - Flask Web Application

Este é um projeto de um aplicativo web utilizando Flask para gerenciar receitas, pedidos e usuários. O sistema permite que usuários se cadastrem, façam login, adicionem receitas, vejam receitas existentes, e adicionem ou removam itens de um carrinho de compras. Além disso, o projeto também inclui a funcionalidade de tradução de receitas utilizando uma API de tradução externa.

## Funcionalidades

### 1. **Cadastro de Usuário**
   - O usuário pode criar uma conta fornecendo um nome e uma senha.
   - Se o usuário já estiver cadastrado, será informado com uma mensagem.

### 2. **Login e Logout**
   - Usuários podem fazer login no sistema utilizando suas credenciais (nome e senha).
   - Após o login, o sistema salva a sessão do usuário.
   - O usuário pode se deslogar, encerrando sua sessão.

### 3. **Carrinho de Compras**
   - O usuário pode adicionar itens ao carrinho de compras.
   - Também pode visualizar os itens do carrinho e deletar itens do mesmo.

### 4. **Gestão de Receitas**
   - Os usuários podem inserir suas próprias receitas, fornecendo um nome, ingredientes e uma imagem.
   - As receitas são armazenadas e podem ser visualizadas por outros usuários.
   - Caso o nome da receita já exista, o sistema avisa o usuário para alterar o nome.

### 5. **Tradução de Receitas**
   - O sistema permite traduzir um texto fornecido pelo usuário de um idioma para outro, utilizando uma API externa (Apertium).

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

- `app.py`: Arquivo principal que inicializa o aplicativo Flask e registra o Blueprint.
- `controllers/`: Contém os controladores das rotas da aplicação.
  - `front_controller.py`: Controlador que define as rotas principais da aplicação.
- `models/`: Contém funções para manipulação de dados, como cadastro de usuário, pedidos e receitas.
  - `data_manager.py`: Contém funções que lidam com o armazenamento e carregamento de dados em arquivos JSON.
- `templates/`: Contém os arquivos HTML utilizados para renderizar as páginas da aplicação.
- `config.py`: Contém configurações como caminhos de arquivos e tipos de imagem permitidos.

## Instalação

1. Clone o repositório para sua máquina local:

    ```bash
    git clone https://github.com/seu_usuario/seu_repositorio.git
    cd seu_repositorio
    ```

2. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure as variáveis de ambiente e as chaves de API (como `YANDEX_API_KEY` para tradução).

4. Inicie o servidor Flask:

    ```bash
    python app.py
    ```

## Funcionalidade das Rotas

### `/`
A página inicial do aplicativo.

### `/cadastro`
Formulário de cadastro para novos usuários. O usuário fornece um nome e senha para criar uma conta.

### `/logar`
Formulário de login, onde o usuário fornece suas credenciais (nome e senha) para acessar a aplicação.

### `/logout`
Encerra a sessão do usuário e redireciona para a página inicial.

### `/culinaria`
Página com as receitas cadastradas pelos usuários. Exibe uma lista de receitas.

### `/adicionarCarrinho`
Permite que o usuário adicione um item ao carrinho de compras.

### `/carrinho`
Exibe os itens no carrinho de compras do usuário.

### `/deletar/<int:id>`
Remove um item do carrinho de compras.

### `/inserirReceita`
Página para adicionar uma nova receita.

### `/adicionarReceita`
Formulário para adicionar uma nova receita. O usuário fornece o nome, ingredientes e uma imagem da receita.

### `/traduzir`
Permite que o usuário traduza um texto de um idioma para outro utilizando a API Apertium.

## Dependências

- Flask: Para criação do servidor web.
- Requests: Para fazer solicitações HTTP para a API de tradução.
- Configurações para trabalhar com arquivos JSON.
  
Instale as dependências com o comando:

```bash
pip install flask requests
