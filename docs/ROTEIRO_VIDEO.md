# Roteiro para apresentação — aproximadamente 6 a 8 minutos

Leia e ensaie antes. Use as falas como apoio e explique com suas palavras. Grave a tela e sua câmera; se houver equipe, TODOS precisam aparecer e explicar uma parte. Ajuste a divisão ao número real de integrantes.

## 1. Apresentação (30 segundos)

**Mostrar:** câmera e tela inicial.

“Olá, meu nome é Gustavo Barp. Neste vídeo vou apresentar a Atividade Avaliativa 2, um sistema de cadastro de funcionários desenvolvido com Python, Django e MySQL. O sistema permite cadastrar, consultar, editar e excluir funcionários, mantendo os dados no banco de dados.”

Se houver colegas, cada um se apresenta e informa a parte que vai explicar.

## 2. Estrutura e modelo (1 minuto)

**Mostrar:** VS Code com a estrutura de pastas, models.py e views.py. Não abra config_local.py com a senha.

“A pasta funcionario contém as configurações do projeto, enquanto a aplicação app reúne o modelo, as views, as rotas e os templates. A classe Funcionario define nome, CPF, e-mail e remuneração. A remuneração usa DecimalField, que trabalha com duas casas decimais. As migrações transformam essa definição em uma tabela no MySQL.”

“As rotas direcionam cada endereço para sua view. Foram utilizadas as classes CreateView, ListView, UpdateView, DetailView e DeleteView. Os templates apresentam os formulários e as informações na tela, com Bootstrap para a formatação.”

## 3. Cadastro e leitura (1 minuto)

**Mostrar:** cadastrar dados fictícios, listar e abrir Exibir dados.

“Vou cadastrar um funcionário de demonstração. Ao enviar o formulário, o Django valida os campos e grava os dados. Depois, a aplicação volta para a listagem. A opção Exibir dados permite consultar um funcionário específico pelo seu identificador, sem alterar as informações.”

Mostre também um campo obrigatório vazio para explicar a validação. Depois preencha corretamente.

## 4. Persistência no MySQL (1 minuto)

**Mostrar:** Workbench/DBeaver, banco funcionarios e SELECT de sql/conferir_persistencia.sql.

“Aqui está o banco funcionarios e a tabela app_funcionario. Executando o SELECT, consigo verificar que os mesmos dados apresentados na tela estão armazenados no MySQL. Portanto, a informação não fica somente na página ou em uma lista na memória do programa.”

Pare e inicie o servidor novamente e reabra a lista.

“Mesmo reiniciando a aplicação, o registro continua disponível porque foi persistido no banco.”

## 5. Atualização (45 segundos)

**Mostrar:** editar nome ou remuneração; executar novamente o SELECT.

“Na edição, o mesmo formulário do cadastro é reutilizado, mas já vem preenchido com os dados do funcionário escolhido. Vou alterar a remuneração e salvar. A listagem e a consulta no MySQL mostram o valor atualizado. O identificador continua o mesmo, porque foi atualizado o registro existente.”

## 6. Exclusão (45 segundos)

**Mostrar:** Remover, cancelar, depois confirmar e consultar o banco.

“A exclusão possui uma tela de confirmação. Abrir essa tela não apaga o funcionário. Posso cancelar e voltar, ou confirmar pelo botão. Ao confirmar, a aplicação envia a solicitação por POST e remove o registro. A consulta no MySQL confirma que ele deixou de existir.”

## 7. GitHub e encerramento (45 segundos)

**Mostrar:** repositório público no navegador, arquivos, README e endereço. Confirme acesso em janela anônima.

“O projeto está compartilhado neste repositório público do GitHub. Ele contém o código, a migração, a lista de dependências, os scripts SQL e as instruções para execução. A pasta do ambiente virtual e a senha do banco não são publicadas. Com isso, foram demonstradas as operações de criação, leitura, atualização e exclusão, além da persistência dos dados no MySQL.”

## Checklist antes de entregar

- [ ] Aplicação executada usando MySQL real, sem settings_test.
- [ ] Cadastro, listagem, detalhes, edição e exclusão demonstrados.
- [ ] SELECT mostrado antes e depois das alterações.
- [ ] Todos os integrantes aparecem e explicam ativamente.
- [ ] Áudio compreensível, código e tela legíveis, sem exposição de senhas.
- [ ] Arquivos do projeto em repositório público (não apenas ZIP).
- [ ] Vídeo publicado no YouTube e link testado sem login.
- [ ] Links do GitHub e do YouTube entregues no ambiente da disciplina.
- [ ] Compartilhamento com a professora realizado conforme orientação da aula.

Rubrica fornecida: projeto público no GitHub — 3,5 pontos; vídeo com participação — 3,0; demonstração do projeto, persistência e repositório — 3,5. O pacote de código sozinho não conclui a entrega.
