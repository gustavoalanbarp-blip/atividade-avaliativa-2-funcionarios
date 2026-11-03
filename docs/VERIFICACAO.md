# Verificação realizada

Foram executados quatro testes automatizados no Django 5.2.19, com django-bootstrap5 26.4 e Python 3.12. Todos passaram. O teste do ciclo completo cobre as cinco telas e verifica as alterações nos registros; os demais verificam campos inválidos, IDs inexistentes e CSRF. A checagem do Django não apontou problemas.

O banco utilizado nesses testes foi SQLite em memória, por uma configuração isolada. Não foi possível testar a integração com MySQL neste ambiente: não há servidor instalado e a compilação de mysqlclient encontrou ausência de bibliotecas/ferramentas de sistema. A configuração padrão do projeto usa MySQL e deve ser validada no computador da apresentação. Não há afirmação de teste real de persistência no MySQL ou de execução no Windows.

Código publicado neste repositório GitHub. Gravação/publicação no YouTube e validação com MySQL real permanecem pendentes.
