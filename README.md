# Atividade Avaliativa 2 — CRUD de Funcionários

Projeto didático de persistência com Python, Django e MySQL, elaborado a partir do roteiro de 23 etapas fornecido na atividade. Comece por este arquivo no VS Code (Ctrl+Shift+V abre a visualização Markdown).

## O que está implementado

Cadastro, listagem, detalhes, edição e exclusão com confirmação. Campos obrigatórios: nome (100 caracteres), CPF (14), e-mail e remuneração (8 dígitos no total, 2 decimais). Banco `funcionarios`, tabela `app_funcionario`, projeto `funcionario`, aplicação `app`. Interface com Bootstrap e botões de navegação.

O modelo mantém as regras do PDF: o CPF é um texto obrigatório, sem validação de dígitos verificadores ou unicidade. Use apenas dados fictícios na demonstração. A aplicação é didática e local, sem controle de acesso nas telas do CRUD.

## 1. Preparar o Windows

Tenha Python 3.12 de 64 bits, MySQL Server 8.0.11 ou superior (por exemplo, 8.4), VS Code e MySQL Workbench ou DBeaver. Workbench/DBeaver são clientes; o servidor MySQL também precisa estar instalado e iniciado. Guarde a senha definida na instalação.

Extraia o ZIP antes de abrir o projeto. Abra a pasta `atividade-crud` no VS Code. No terminal, escolha **Command Prompt / Prompt de Comando (cmd)**. Os comandos abaixo usam CMD, não PowerShell.

```bat
py -m pip install virtualenv
py -m virtualenv venv
venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Selecione o interpretador em Ctrl+Shift+P → Python: Select Interpreter → `venv\Scripts\python.exe`.

O projeto já contém os arquivos finais de `startproject` e `startapp`. NÃO execute esses comandos novamente sobre esta pasta. Para entender a criação do zero, consulte `docs/MAPA_DO_ROTEIRO.md`.

## 2. Criar o banco MySQL

Conecte-se ao servidor pelo Workbench/DBeaver com suas credenciais e execute `sql/criar_banco.sql`:

```sql
CREATE DATABASE IF NOT EXISTS funcionarios
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

No terminal CMD, copie o exemplo de configuração:

```bat
copy funcionario\config_local.example.py funcionario\config_local.py
```

Abra `funcionario/config_local.py` e substitua o texto de exemplo pela sua senha, mantendo as aspas. Esse arquivo está no `.gitignore` e não deve ser enviado ao GitHub nem exibido na gravação.

O padrão de conexão é usuário `root`, servidor `127.0.0.1`, porta `3306` e banco `funcionarios`. Se seu ambiente for diferente, ajuste as variáveis no CMD antes de executar:

```bat
set DB_USER=seu_usuario
set DB_HOST=127.0.0.1
set DB_PORT=3306
```

## 3. Gerar/aplicar migrações e iniciar

```bat
python manage.py makemigrations
python manage.py migrate
python manage.py check
python manage.py runserver
```

A migração inicial já está incluída. Por isso, `makemigrations` deve informar `No changes detected`; isso é esperado. `migrate` cria as tabelas no MySQL.

Abra http://127.0.0.1:8000/ . O endereço inicial redireciona à listagem. O cadastro também está em http://127.0.0.1:8000/app/form_funcionario .

Para encerrar: Ctrl+C e `deactivate`. Para voltar, abra o CMD na pasta, execute `venv\Scripts\activate` e `python manage.py runserver`.

## 4. Demonstrar a persistência

1. Cadastre `Funcionário Demonstração`, CPF `000.000.000-00`, e-mail `demo@example.com`, remuneração `2500.00` (dados fictícios; o CPF não representa um documento válido).
2. Abra a listagem e clique em **Exibir dados**.
3. No Workbench/DBeaver, execute:

```sql
USE funcionarios;
SELECT id, nome, cpf, email, remuneracao FROM app_funcionario ORDER BY id;
```

4. Edite a remuneração para `3100.50` e execute a consulta novamente. O formulário pode apresentar separador decimal localizado; use o formato aceito pelo navegador, sem separador de milhares.
5. Pare e inicie novamente o Django. Reabra a lista: o registro deve continuar lá.
6. Clique em Remover e depois em Cancelar para demonstrar a confirmação. Repita e confirme a exclusão. Execute novamente o SELECT: o registro não deve mais aparecer.
7. Use `DESCRIBE app_funcionario;` para mostrar a estrutura dos campos.

É necessário executar a consulta novamente para atualizar o resultado. Reiniciar apenas o navegador não é uma demonstração tão clara quanto reiniciar a aplicação e mostrar o SELECT no MySQL.

## 5. Publicar no GitHub

Crie na sua conta um repositório **público** para a atividade. O ZIP é um pacote de entrega; o repositório deve conter os arquivos extraídos, permitindo consultar o código diretamente.

Com Git instalado, execute na pasta `atividade-crud`:

```bat
git init
git add .
git status
git commit -m "Implementa CRUD de funcionarios com Django e MySQL"
git branch -M main
```

Confira no `git status` que `venv`, `config_local.py`, senhas e arquivos `.env` não estão incluídos. Depois copie a URL exata do repositório criado e use-a no lugar do marcador:

```bat
git remote add origin URL_DO_SEU_REPOSITORIO
git push -u origin main
```

Faça a autenticação pelo procedimento apresentado pelo GitHub. Não publique tokens ou senhas.

Alternativa pelo site: use a opção de upload de arquivos no repositório e envie os arquivos de código e documentação extraídos, preservando as pastas. Não envie `venv`, `config_local.py` ou apenas o ZIP.

Verifique o repositório em uma janela anônima. Siga a forma de compartilhamento com a professora indicada em aula e entregue também o link no ambiente da disciplina.

## 6. Gravar e publicar o vídeo

Use `docs/ROTEIRO_VIDEO.md`. Todos os integrantes precisam aparecer e participar ativamente das explicações. Mostre as telas, o código principal, os dados no MySQL e o repositório público. Publique no YouTube e confira se o link abre sem solicitar acesso; para evitar dúvida de acesso, use visibilidade pública, observando as orientações da professora.

Entregue os dois links no local solicitado: repositório GitHub e vídeo YouTube. O código está publicado em https://github.com/gustavoalanbarp-blip/atividade-avaliativa-2-funcionarios . A gravação/publicação do vídeo e a validação local com MySQL ainda precisam ser realizadas.

## Problemas frequentes

- `Access denied`: confira usuário e senha do MySQL e o arquivo `config_local.py`.
- `Can't connect`: confirme se o serviço MySQL está iniciado e se a porta está correta.
- `Unknown database`: execute o script de criação do banco.
- `Table ... doesn't exist`: execute `python manage.py migrate`.
- `No module named django`: ative o venv e instale `requirements.txt`.
- Falha compilando `mysqlclient` no Windows: confirme Python 3.12 64 bits e pip atualizado; versões/arquiteturas sem pacote binário podem exigir compilador e bibliotecas do cliente. Não substitua por SQLite na apresentação, pois a atividade exige MySQL.
- Estilo simples: o Bootstrap é carregado pela internet; confira a conexão. O CRUD continua usando os templates locais.
- Porta ocupada: use `python manage.py runserver 8001` e abra a porta 8001.

## Testes e limites de verificação

Os testes em `app/tests.py` verificam cadastro, listagem, detalhes, edição, confirmação/exclusão, campos inválidos, registros inexistentes e proteção CSRF. Para testar com seu MySQL, execute `python manage.py test`; o usuário precisa poder criar e remover o banco temporário `test_funcionarios`.

Neste ambiente foi usada uma configuração separada de SQLite em memória apenas para testes da lógica (`python manage.py test --settings=funcionario.settings_test`). O funcionamento com servidor MySQL real deve ser confirmado localmente pelos passos acima. `settings.py`, usado normalmente por `runserver`, está configurado exclusivamente para MySQL.

## Fontes

- Roteiro fornecido: Atividade Avaliativa 2.pdf, 23 páginas.
- Django 5.2 — bancos de dados: https://docs.djangoproject.com/en/5.2/ref/databases/
- Django — views genéricas de edição: https://docs.djangoproject.com/en/5.2/ref/class-based-views/generic-editing/

Consulte `docs/MAPA_DO_ROTEIRO.md` para relacionar o código às etapas do PDF.
