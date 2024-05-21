# Desafio Backend | Django

Olá, candidato! Se você chegou até aqui, é porque demonstrou interesse em fazer parte do nosso time. Preparamos um desafio para entendermos um pouco mais sobre suas habilidades como desenvolvedor backend em Django.

## 🚀 Objetivo:

Desenvolver uma API para gerenciar um sistema de tarefas e projetos, permitindo que usuários criem projetos e associem tarefas a eles.

## 📖 Regras de Negócio:

1. Somente o criador do projeto pode adicionar ou remover membros.
2. Tarefas só podem ser criadas por membros do projeto ao qual a tarefa pertence.
3. Um usuário só pode ser adicionado a um projeto se ele já estiver registrado na plataforma.
4. Tarefas concluídas não podem ser editadas.
5. As tarefas precisam ter tags.

## 💻 Tecnologias:

- Django

# Desafio Backend | Django

Olá, candidato! Se você chegou até aqui, é porque demonstrou interesse em fazer parte do nosso time. Preparamos um desafio para entendermos um pouco mais sobre suas habilidades como desenvolvedor backend em Django.

## 🚀 Objetivo:

Desenvolver uma API para gerenciar um sistema de tarefas e projetos, permitindo que usuários criem projetos e associem tarefas a eles.

## 📖 Regras de Negócio:

1. Somente o criador do projeto pode adicionar ou remover membros.
2. Tarefas só podem ser criadas por membros do projeto ao qual a tarefa pertence.
3. Um usuário só pode ser adicionado a um projeto se ele já estiver registrado na plataforma.
4. Tarefas concluídas não podem ser editadas.
5. As tarefas precisam ter tags.

## 💻 Tecnologias:

- Django
- PostgreSQL
- Django REST framework
- Django ORM

## 📜 Requisitos:

### 1. Configuração Inicial:

- Configurar um projeto usando Django.
- Configurar um banco de dados PostgreSQL (Local).
- Utilizar o Django ORM.

### 2. Modelo de Dados:

#### Usuário (`User`):

- ID: ID gerado automaticamente.
- Nome: Texto.
- Email: Texto, único.
- Senha: Texto, encriptada.

#### Projeto (`Project`):

- ID: ID gerado automaticamente.
- Nome: Texto.
- Descrição: Texto.
- Membros: Lista de usuários associados ao projeto.

#### Tarefa (`Task`):

- ID: ID gerado automaticamente.
- Título: Texto, máximo de 255 caracteres.
- Descrição: Texto.
- Data de criação: Data e hora, gerada automaticamente.
- Status: Enum (Pendente, Em andamento, Concluída).
- Projeto: Referência ao projeto ao qual pertence.

#### Tag (`Tag`):

- ID: ID gerado automaticamente.
- Título: Texto.
- Tarefa: Referência a tarefa ao qual pertence.

### 3. Autenticação e Autorização:

- Implementar autenticação usando Django Rest Framework com JWT.
- Garantir que somente usuários autenticados possam acessar os endpoints.
- Implementar permissões para garantir que somente o criador do projeto possa adicionar ou remover membros.

### 4. Validações e Erros:

- Implemente validações para garantir a integridade dos dados.
- Responda com mensagens de erro claras e status HTTP apropriados.

## 🥇 Diferenciais:

- Testes unitários e/ou de integração.
- Documentação com Swagger ou DRF-YASG.
- Paginação nos endpoints.
- Registro de logs.
- Dockerização da aplicação.
- Uso de um linter (como Flake8) e formatador de código (como Black).

## 🗳️ Instruções de Submissão:

1. Faça um fork deste repositório para sua conta pessoal do GitHub.
2. Commit e push suas mudanças para o seu fork.
3. Envie um e-mail para [arthur.olga@khipo.com.br] com o link do repositório.

## 🧪 Avaliação:

- Estrutura do código e organização.
- Uso adequado das ferramentas e tecnologias.
- Implementação dos requisitos e regras de negócio.
- Design e usabilidade.
- Funcionalidades extras (diferenciais).

Boa sorte com o desafio! Estamos ansiosos para ver sua solução.

# Implentação:
## Dados para criação do banco de dados no env.example

```
    python -m venv venv
```

```
    source venv/bin/activate
``` 

```
    pip install -r requirements.txt
```

```
    mv .env.example .env
```

```
    python manage.py makemigrations
```

```
    python manage.py migrate
```

```
    python manage.py runserver
```

- https://www.postman.com/leonardofguedes/workspace/khipo/overview


Criando o Primeiro Usuário
Para criar o primeiro usuário na sua aplicação, siga os passos abaixo utilizando o Postman:

Passo 1: Configurar o Postman
Abrir o Postman.

Criar uma nova requisição:

Método: POST
URL: http://localhost:8000/api/create-user/
Configurar o cabeçalho (Headers):

Adicionar um cabeçalho Content-Type com valor application/json.
Configurar o corpo da requisição (Body):

Selecionar raw e definir o tipo como JSON.
Adicionar o seguinte JSON no corpo da requisição para criar um novo usuário especial (admin):
json
Copiar código
{
    "username": "admin",
    "email": "admin@example.com",
    "nome": "Administrador",
    "password": "senha_segura"
}
Passo 2: Enviar a Requisição
Clique no botão Send para enviar a requisição.

Verificar a resposta:

Se o usuário for criado com sucesso, você receberá uma resposta JSON com os detalhes do usuário criado.
Exemplo de resposta:
json
Copiar código
{
    "id": 1,
    "username": "admin",
    "email": "admin@example.com",
    "nome": "Administrador"
}
Passo 3: Utilizar o Usuário Criado para Autenticação
Após criar o usuário admin, você pode utilizá-lo para autenticar-se e realizar outras operações na sua API.

Obter um token JWT:

Método: POST
URL: http://localhost:8000/api/token/
Headers:
Content-Type: application/json
Body:
json
Copiar código
{
    "username": "admin",
    "password": "senha_segura"
}
Usar o token JWT para autenticação em outras requisições:

Inclua o token JWT no cabeçalho Authorization das suas requisições:
Authorization: Bearer <seu_token_jwt>
Exemplo de Criação de Outros Usuários
Para criar outros usuários após ter autenticado o usuário admin:

Criar uma nova requisição no Postman:

Método: POST
URL: http://localhost:8000/api/create-user/
Headers:
Content-Type: application/json
Authorization: Bearer <seu_token_jwt>
Body:
json
Copiar código
{
    "username": "novo_usuario",
    "email": "novo_usuario@example.com",
    "nome": "Novo Usuário",
    "password": "senha_segura"
}
Enviar a requisição e verificar a resposta:

Se o usuário for criado com sucesso, você receberá uma resposta JSON com os detalhes do novo usuário.
Seguindo esses passos, você pode criar o primeiro usuário especial e utilizar a autenticação JWT para gerenciar outros usuários e recursos na sua API.