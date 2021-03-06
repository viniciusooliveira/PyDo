# PyDo

Projeto criado com a intenção de aprender um pouco mais sobre Python.
Foram utilizadas as seguintes tecnologias:
- FastApi => Framework para construção de APIs feito utilizando o Starllete
- Uvicorn => Implementação de servidor ASGI
- SQLAlchemy => ORM para bancos relacionais
- Alembic => Implementação de "migrations" para o SQLAlchemy
- MySQL => Banco de dados relacional

## Como executar
Após clonar o repositório, você deverá navegar até a pasta raiz e executar os seguintes passos:

- Criar um arquivo `.env` e preencher seguindo o `.env-example` como referência
- Executar o comando `virtualenv ./` para criar o venv
- Executar o comando `poetry install` para instalar as dependências
- Executar o comando `alembic upgrade head` para criar a estrutura do BD
- Executar o comando `python main.py`para executar o projeto

## Próximos passos
- [x] Adicionar camada para regras de negócio
- [x] Adicionar nova tabela com relação 1-N e verificar como se comportam as migrations 
- [ ] Verificar a viabilidade de um container para DI
- [ ] Adicionar testes unitários e de integração
- [ ] Utilizar métodos assíncronos para comunicação com o BD
- [ ] Adicionar execução por Docker