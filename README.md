# 🛡️ Blackwall AI

Assistente virtual educacional para orientação sobre segurança digital e prevenção de ameaças.

## 📌 Sobre o Projeto

O **Blackwall AI** foi desenvolvido como projeto do desafio **Construa Seu Assistente Virtual Com Inteligência Artificial**, da DIO.

O objetivo é criar um assistente capaz de fornecer orientações simples e acessíveis sobre cibersegurança utilizando uma base de conhecimento estruturada.

O protótipo aborda temas como:

- Phishing;
- Senhas;
- Autenticação em dois fatores;
- Engenharia social;
- Links suspeitos;
- Proteção de contas.

## 🤖 Como Funciona

O usuário envia uma pergunta relacionada à segurança digital. A aplicação identifica o assunto, consulta a base de conhecimento correspondente e utiliza essas informações como contexto para o modelo Gemini gerar uma resposta.

O fluxo básico é:

**Usuário → Pergunta → Identificação do Tema → Base de Conhecimento → Gemini → Blackwall AI → Resposta**

Caso o assunto não esteja disponível na base, o assistente informa que não possui informações suficientes, evitando inventar uma resposta.

## 🧠 Base de Conhecimento

A base utilizada pelo assistente está armazenada em:

`data/base_conhecimento.json`

As informações são organizadas por categorias e incluem descrições, sinais de atenção e recomendações de segurança.

## 🛠️ Tecnologias Utilizadas

- Python
- Gradio
- JSON
- GitHub
- Google Colab
- Google Gemini
- Google GenAI SDK

## 📂 Estrutura do Projeto

```text
assistente-ciberseguranca-ia/
│
├── data/
│   └── base_conhecimento.json
│
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
│
├── src/
│   └── app.py
│
└── README.md
```

## ▶️ Como Executar

Clone o repositório e instale o Gradio:

```bash
pip install -r requirements.txt
```

Configure a variável de ambiente `GEMINI_API_KEY` com uma chave válida da API do Gemini. A chave não deve ser adicionada diretamente ao código ou enviada ao GitHub.

Depois execute:

```bash
python src/app.py
```

A aplicação iniciará uma interface de chatbot utilizando o Gradio.

## 📚 Etapas do Desafio

O desenvolvimento foi organizado de acordo com as seis etapas propostas no desafio:

1. [Documentação do Agente](docs/01-documentacao-agente.md)
2. [Base de Conhecimento](docs/02-base-conhecimento.md)
3. [Prompts do Agente](docs/03-prompts.md)
4. [Aplicação Funcional](src/app.py)
5. [Avaliação e Métricas](docs/04-metricas.md)
6. [Pitch](docs/05-pitch.md)

## 🔒 Segurança

O Blackwall AI foi projetado para:

- Não solicitar senhas, códigos de autenticação ou dados bancários;
- Utilizar informações presentes em sua base de conhecimento;
- Informar quando não possui conhecimento suficiente sobre determinado assunto;
- Não fornecer orientações destinadas a atividades maliciosas.

As respostas possuem caráter educacional e não substituem a análise de um profissional de cibersegurança.

## 🚀 Possíveis Evoluções

Entre as melhorias futuras estão:

- Ampliação da base de conhecimento;
- Melhor compreensão de linguagem natural;
- Avaliação automatizada das respostas;
- Hospedagem permanente da aplicação.

## 🎯 Resultado

O projeto resultou em um protótipo funcional de assistente virtual capaz de consultar uma base estruturada e fornecer orientações sobre segurança digital por meio de uma interface conversacional.

O desenvolvimento também demonstra conceitos de organização de conhecimento, engenharia de prompts, prevenção de alucinações e construção de interfaces para assistentes virtuais.
