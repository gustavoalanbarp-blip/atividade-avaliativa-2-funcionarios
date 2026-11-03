# CRUD de Funcionários

Sistema desenvolvido com Python, Django e MySQL para cadastrar e gerenciar funcionários.

## Funcionalidades

- Cadastro de funcionários com nome, CPF, e-mail e remuneração.
- Listagem dos funcionários cadastrados.
- Consulta dos dados de um funcionário.
- Edição das informações.
- Exclusão com confirmação.

## Tecnologias

- Python 3.12
- Django 5.2
- MySQL
- mysqlclient
- Bootstrap 5 e django-bootstrap5

## Executar localmente

Os comandos abaixo utilizam o Prompt de Comando (CMD) do Windows. É necessário ter Python, Git e MySQL Server instalados, com o serviço MySQL em execução.

### 1. Baixar o projeto e instalar as dependências

```bat
git clone https://github.com/gustavoalanbarp-blip/atividade-avaliativa-2-funcionarios.git
cd atividade-avaliativa-2-funcionarios
py -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 2. Configurar o banco de dados

No MySQL Workbench ou DBeaver, execute o script `sql/criar_banco.sql`:

```sql
CREATE DATABASE IF NOT EXISTS funcionarios
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Copie o arquivo de configuração:

```bat
copy funcionario\config_local.example.py funcionario\config_local.py
```

Em `funcionario/config_local.py`, configure `DB_PASSWORD` com a senha do seu MySQL. Esse arquivo é ignorado pelo Git.

A conexão padrão utiliza banco `funcionarios`, usuário `root`, endereço `127.0.0.1` e porta `3306`. Caso necessário, ajuste as variáveis de ambiente `DB_NAME`, `DB_USER`, `DB_HOST` e `DB_PORT`.

### 3. Aplicar as migrações e iniciar

```bat
python manage.py migrate
python manage.py runserver
```

Acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Organização do projeto

| Caminho | Conteúdo |
|---|---|
| `funcionario/` | Configurações e rotas principais |
| `app/models.py` | Modelo Funcionario |
| `app/views.py` | Operações de cadastro, consulta, edição e exclusão |
| `app/urls.py` | Rotas da aplicação |
| `app/templates/` | Páginas HTML |
| `app/migrations/` | Migrações do banco de dados |
| `app/tests.py` | Testes automatizados |
| `sql/` | Scripts de criação e consulta do banco |

## Testes

Para executar os testes com MySQL:

```bat
python manage.py test
```

O usuário do banco precisa ter permissão para criar e remover o banco temporário de testes.

Também é possível testar a lógica com SQLite em memória, utilizando a configuração separada:

```bat
python manage.py test --settings=funcionario.settings_test
```

Essa configuração não altera o banco MySQL usado na execução normal da aplicação e não substitui a validação da integração com ele.

## Observações

Aplicação acadêmica destinada à execução local. As telas do CRUD não possuem autenticação. O CPF é armazenado como texto, sem validação dos dígitos verificadores. O Bootstrap é carregado pela internet.
