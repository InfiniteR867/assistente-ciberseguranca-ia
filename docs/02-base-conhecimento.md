# Base de Conhecimento

## Objetivo

A base de conhecimento do Blackwall AI reúne informações sobre boas práticas de cibersegurança que serão utilizadas pelo assistente para orientar suas respostas.

O objetivo é fornecer um conjunto de informações organizado e controlado, reduzindo a possibilidade de respostas incorretas ou inventadas.

## Estrutura dos Dados

A base está armazenada no arquivo:

`data/base_conhecimento.json`

O formato JSON foi escolhido por permitir organizar as informações em categorias de forma simples e facilitar sua leitura pela aplicação.

## Categorias

A primeira versão da base de conhecimento contém informações sobre:

- Phishing;
- Senhas;
- Autenticação em dois fatores;
- Engenharia social;
- Links suspeitos;
- Proteção de contas.

Cada categoria possui uma descrição do tema e recomendações de segurança. Algumas categorias também apresentam sinais que podem ajudar o usuário a reconhecer uma possível ameaça.

## Uso pelo Assistente

Quando o usuário enviar uma pergunta, a aplicação deverá buscar informações relacionadas ao assunto na base de conhecimento.

As informações encontradas serão utilizadas como contexto para a geração da resposta do Blackwall AI.

O fluxo esperado é:

Usuário → Pergunta → Consulta à Base de Conhecimento → Contexto → Blackwall AI → Resposta

## Estratégia Anti-Alucinação

O assistente deverá priorizar as informações disponíveis na base de conhecimento.

Caso a pergunta não esteja relacionada aos assuntos disponíveis ou não existam informações suficientes para uma resposta confiável, o Blackwall AI deverá informar ao usuário que não possui informações suficientes em sua base.

O assistente não deverá inventar procedimentos, dados ou recomendações para preencher informações ausentes.

## Evolução da Base

A base poderá ser expandida futuramente com novos temas, como:

- Malware;
- Ransomware;
- Segurança em redes Wi-Fi;
- Atualizações de software;
- Backup;
- Privacidade de dados;
- Segurança em dispositivos móveis.
