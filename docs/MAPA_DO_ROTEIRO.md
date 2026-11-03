# Correspondência com o roteiro da professora

| Etapas do PDF | Implementação / procedimento |
|---|---|
| 1–4 | Pasta atividade-crud, criação e ativação do venv no README. |
| 5 | requirements.txt: Django e mysqlclient. |
| 6 | Projeto funcionario e aplicação app já criados. |
| 7–8 | app e conexão MySQL em funcionario/settings.py. |
| 9 | sql/criar_banco.sql cria funcionarios. |
| 10–11 | funcionario/urls.py inclui app/urls.py; forms.py e templates presentes. |
| 12 | Seleção do interpretador descrita no README. |
| 13–15 | Rotas e runserver. A aplicação final já tem rotas funcionais. |
| 16 | app/models.py e app/migrations/0001_initial.py. |
| 17 | django_bootstrap5; FuncionarioCreateView e form_funcionario.html. |
| 18 | FuncionarioListView e lista_funcionarios.html. |
| 19 | FuncionarioUpdateView reutiliza o formulário. |
| 20 | FuncionarioDetailView; lista_funcionario.html; contexto fun. |
| 21 | Links Exibir dados, Editar e Voltar. |
| 22 | FuncionarioDeleteView; remover_funcionario.html; confirmação por POST. |
| 23 | Tabela, botões, espaçamento e formatação com Bootstrap/CSS. |

## Ordem para estudar ou reconstruir do zero

Em uma pasta nova, siga a ordem do PDF: criar venv; ativar; instalar Django/mysqlclient; `django-admin startproject funcionario .`; `python manage.py startapp app`; registrar app; configurar MySQL; criar banco; criar rotas; definir modelo; gerar e aplicar migração; instalar django-bootstrap5; criar cadastro; listagem; edição; detalhes; links; exclusão; formatação.

O pacote entregue contém o estado final. Não precisa reproduzir os erros intermediários de rota mostrados no PDF. A pasta venv não é distribuída: cada computador deve criar a sua.

## Correções aplicadas aos exemplos

- Corrigidas aspas faltantes nos exemplos de rotas de cadastro.
- Cada funcionário está dentro de seu próprio `<tr>`, com o loop envolvendo a linha completa.
- Exclusão usa sempre o contexto `fun`, coerente entre view e template.
- Redirecionamentos usam `reverse_lazy` com o nome da rota.
- A navegação Voltar usa a rota da lista, funcionando mesmo ao acessar uma tela diretamente.
- Bootstrap é carregado uma vez no template base, evitando duplicidade de versões.
- A senha é lida de arquivo local ignorado pelo Git ou variável de ambiente.

São correções de funcionamento e organização; os quatro campos e as cinco views seguem o roteiro. O formulário automático valida obrigatoriedade, e-mail e limites dos campos. Regras adicionais de CPF não foram introduzidas porque não fazem parte do modelo solicitado.
