# Pitch — Blackwall AI

## O Problema

A segurança digital faz parte do cotidiano de qualquer pessoa que utiliza serviços online. E-mails falsos, links suspeitos, reutilização de senhas e tentativas de engenharia social podem colocar contas e informações pessoais em risco.

Ao mesmo tempo, usuários com pouco conhecimento em cibersegurança podem ter dificuldade para identificar essas ameaças e saber como agir.

## A Solução

O Blackwall AI é um assistente virtual educacional criado para fornecer orientações simples e acessíveis sobre segurança digital.

O usuário pode fazer perguntas sobre temas como phishing, senhas, autenticação em dois fatores, engenharia social, links suspeitos e proteção de contas.

A aplicação identifica o assunto da pergunta, consulta uma base de conhecimento controlada e apresenta informações e recomendações relacionadas ao tema.

## Como Funciona

O protótipo foi desenvolvido em Python utilizando Gradio para disponibilizar uma interface de conversa.

O fluxo da aplicação é:

Usuário → Pergunta → Identificação do Tema → Base de Conhecimento → Blackwall AI → Resposta

A base de conhecimento é armazenada em JSON e contém informações organizadas sobre diferentes temas de cibersegurança.

## Segurança e Confiabilidade

Um dos principais objetivos do projeto é evitar respostas inventadas.

Quando o Blackwall AI não encontra informações suficientes em sua base de conhecimento, ele informa ao usuário que não possui dados sobre aquele assunto.

O assistente também foi projetado para não solicitar informações sensíveis, como senhas, códigos de autenticação ou dados bancários.

## Diferencial

O Blackwall AI combina uma interface simples de chatbot com uma base de conhecimento controlada.

Em vez de tentar responder qualquer pergunta, o protótipo reconhece suas próprias limitações e prioriza informações previamente organizadas, tornando seu comportamento mais previsível e seguro.

## Evoluções Futuras

O projeto poderá evoluir com:

- Ampliação da base de conhecimento;
- Identificação de intenção utilizando modelos de linguagem;
- Integração com uma LLM;
- Melhor compreensão de diferentes formas de fazer uma pergunta;
- Métricas automatizadas para avaliação das respostas;
- Disponibilização permanente da aplicação na web.

## Resumo do Pitch

O Blackwall AI é um assistente virtual educacional de cibersegurança que ajuda usuários a reconhecer ameaças digitais e adotar boas práticas de proteção.

O projeto demonstra como uma aplicação de IA pode utilizar uma base de conhecimento estruturada, regras de segurança e uma interface conversacional para fornecer orientações úteis, mantendo limites claros quando não possui informações suficientes.
