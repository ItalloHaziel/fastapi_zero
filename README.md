FASTAPI ZERO — API BASE PROFISSIONAL COM BOAS PRÁTICAS

Projeto base para construção de APIs modernas utilizando FastAPI, com foco em organização, qualidade de código, testes automatizados e boas práticas de engenharia de software.

Este repositório representa a estrutura inicial de um backend profissional pronto para escalar, servindo como template para novos projetos em Python.

OBJETIVO

Criar uma base sólida e organizada para desenvolvimento de APIs REST aplicando:

Arquitetura limpa e modular
Gerenciamento de dependências com Poetry
Ambiente virtual isolado
Padronização automática de código
Testes automatizados
Automação de tarefas de desenvolvimento
Estrutura preparada para crescimento

STACK UTILIZADA

FastAPI — Framework moderno, rápido e tipado para APIs
Uvicorn — Servidor ASGI de alta performance
Poetry — Gerenciamento de dependências e ambiente virtual
Ruff — Lint e formatação de código
Pytest — Framework de testes
Taskipy — Automação de comandos de desenvolvimento

ESTRUTURA DO PROJETO

fast_api_zero/
│
├── fast_api_zero/
│ └── app.py # Instância principal da aplicação
│
├── tests/
│ └── test_app.py # Testes automatizados
│
├── pyproject.toml # Configuração central do projeto
├── poetry.lock # Controle de versões exatas
└── README.md # Documentação

FUNCIONALIDADE ATUAL

A API possui uma rota inicial para validação da estrutura:

GET /

Retorno:
{
"message": "ola mundo!"
}

A documentação automática está disponível em:

/docs
/redoc

TESTES AUTOMATIZADOS

O projeto utiliza pytest juntamente com o TestClient do FastAPI para validação dos endpoints.

Boas práticas aplicadas:

Convenção test_*.py
Separação clara entre aplicação e testes
Execução isolada em ambiente virtual
Cobertura de testes preparada para evolução

QUALIDADE E PADRONIZAÇÃO

Integração com ferramentas modernas para garantir:

Organização automática de imports
Correção de estilo (PEP8)
Padronização consistente
Verificação estática de código

PREPARADO PARA ESCALAR

Esta base já está estruturada para evolução futura com:

Integração com banco de dados
Autenticação JWT
Dockerização
CI/CD
Deploy em nuvem
Separação por camadas (schemas, services, repositories)

SOBRE O PROJETO

Este repositório demonstra:

Organização profissional de backend em Python
Aplicação prática de testes automatizados
Uso de ferramentas modernas de desenvolvimento
Estrutura pronta para ambientes de produção

Projeto desenvolvido como base estratégica de portfólio para desenvolvimento backend com FastAPI.