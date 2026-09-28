# Avaliação e Métricas

## Objetivo da Avaliação

A avaliação do Blackwall AI tem como objetivo verificar se o assistente consegue identificar assuntos presentes na base de conhecimento, fornecer orientações coerentes e evitar respostas inventadas quando não possui informações suficientes.

## Critérios de Avaliação

Foram considerados os seguintes critérios:

- **Assertividade:** a resposta deve estar relacionada à pergunta realizada.
- **Uso da base de conhecimento:** as orientações apresentadas devem utilizar as informações disponíveis no arquivo `base_conhecimento.json`.
- **Segurança:** o assistente não deve solicitar informações sensíveis.
- **Anti-alucinação:** quando não encontrar informações relacionadas à pergunta, deve informar que não possui dados suficientes.
- **Clareza:** as respostas devem utilizar linguagem simples e apresentar recomendações de forma organizada.

## Cenários de Teste

Foram definidos diferentes cenários para verificar o comportamento do assistente.

| Teste | Pergunta | Resultado Esperado |
|---|---|---|
| Phishing | "Recebi um e-mail suspeito. O que devo fazer?" | Identificar o tema e apresentar sinais e recomendações sobre phishing |
| Senhas | "Posso usar a mesma senha em vários sites?" | Recomendar senhas diferentes e boas práticas de proteção |
| Autenticação | "Vale a pena ativar autenticação em dois fatores?" | Explicar a importância da autenticação em dois fatores |
| Proteção de conta | "Como posso proteger minha conta?" | Apresentar recomendações disponíveis na base |
| Tema desconhecido | Pergunta fora da base de conhecimento | Informar que não possui informações suficientes |

## Resultados

Durante os testes realizados no protótipo, o Blackwall AI conseguiu consultar corretamente a base de conhecimento e retornar as informações correspondentes aos assuntos reconhecidos.

O teste com uma pergunta sobre e-mail suspeito identificou corretamente a categoria de phishing e apresentou os sinais de atenção e recomendações cadastrados na base.

Também foi verificado o comportamento para assuntos não reconhecidos. Nesses casos, o assistente retorna a mensagem:

> "Não possuo informações suficientes sobre esse assunto na minha base de conhecimento."

Esse comportamento ajuda a reduzir respostas inventadas quando o conhecimento necessário não está disponível.

## Limitações da Avaliação

A avaliação foi realizada utilizando um conjunto pequeno de perguntas e cenários previamente definidos.

Como a identificação dos assuntos utiliza palavras-chave, perguntas escritas de formas muito diferentes das previstas podem não ser classificadas corretamente.

Em versões futuras, a avaliação poderá utilizar um conjunto maior de perguntas e métricas quantitativas para medir a taxa de respostas corretas e a cobertura da base de conhecimento.

## Conclusão

Os testes iniciais demonstraram que o protótipo consegue utilizar sua base de conhecimento para fornecer orientações simples de segurança digital e possui um comportamento definido para situações em que não encontra informações suficientes.

A avaliação também mostrou oportunidades de evolução, principalmente na identificação da intenção das perguntas e na ampliação da base de conhecimento.
