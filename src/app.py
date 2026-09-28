import gradio as gr
import json
import os
from google import genai


# Localiza e carrega a base de conhecimento
CAMINHO_BASE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "base_conhecimento.json"
)

with open(CAMINHO_BASE, "r", encoding="utf-8") as arquivo:
    base_conhecimento = json.load(arquivo)


# Configuração do Gemini
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "A variável de ambiente GEMINI_API_KEY não foi configurada."
    )

client = genai.Client(api_key=api_key)


def buscar_conhecimento(pergunta):
    pergunta = pergunta.lower()

    palavras_chave = {
        "phishing": [
            "phishing", "email suspeito", "e-mail suspeito",
            "mensagem suspeita"
        ],
        "senhas": ["senha", "senhas"],
        "autenticacao_dois_fatores": [
            "2fa", "dois fatores", "autenticação", "autenticacao"
        ],
        "engenharia_social": [
            "engenharia social", "manipulação", "manipulacao"
        ],
        "links_suspeitos": [
            "link", "links", "site suspeito"
        ],
        "protecao_de_contas": [
            "proteger conta", "proteção da conta",
            "protecao da conta", "conta invadida"
        ]
    }

    for categoria, termos in palavras_chave.items():
        if any(termo in pergunta for termo in termos):
            return base_conhecimento[categoria]

    return None


def gerar_resposta(pergunta):
    conhecimento = buscar_conhecimento(pergunta)

    if conhecimento is None:
        return (
            "Não possuo informações suficientes sobre esse assunto "
            "na minha base de conhecimento."
        )

    contexto = json.dumps(
        conhecimento,
        ensure_ascii=False,
        indent=2
    )

    prompt = f"""
Você é o Blackwall AI, um assistente virtual educacional
especializado em segurança digital.

Responda à pergunta utilizando somente as informações
fornecidas na base de conhecimento abaixo.

Regras:
- Responda de forma clara, objetiva e acessível.
- Não invente informações.
- Não solicite senhas, códigos de autenticação, dados bancários
  ou outras informações sensíveis.
- Não forneça instruções para invasão de sistemas, roubo de
  credenciais, criação de malware ou outras atividades maliciosas.
- Quando possível, apresente recomendações práticas.
- Informe que as orientações possuem caráter educacional.

BASE DE CONHECIMENTO:
{contexto}

PERGUNTA DO USUÁRIO:
{pergunta}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception:
        return (
            "Não foi possível consultar o modelo de IA neste momento. "
            "Tente novamente mais tarde."
        )


def responder_chat(mensagem, historico):
    return gerar_resposta(mensagem)


chat = gr.ChatInterface(
    fn=responder_chat,
    title="Blackwall AI",
    description=(
        "Assistente virtual educacional com IA para orientação "
        "sobre segurança digital."
    ),
    examples=[
        "Recebi um e-mail suspeito. O que devo fazer?",
        "Posso usar a mesma senha em vários sites?",
        "Vale a pena ativar autenticação em dois fatores?",
        "Como posso proteger minha conta?"
    ]
)


if __name__ == "__main__":
    chat.launch()
