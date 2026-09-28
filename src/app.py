import gradio as gr
import json
import os


# Localiza e carrega a base de conhecimento
CAMINHO_BASE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "base_conhecimento.json"
)

with open(CAMINHO_BASE, "r", encoding="utf-8") as arquivo:
    base_conhecimento = json.load(arquivo)


def buscar_conhecimento(pergunta):
    pergunta = pergunta.lower()

    palavras_chave = {
        "phishing": ["phishing", "email suspeito", "e-mail suspeito", "mensagem suspeita"],
        "senhas": ["senha", "senhas"],
        "autenticacao_dois_fatores": [
            "2fa", "dois fatores", "autenticação", "autenticacao"
        ],
        "engenharia_social": [
            "engenharia social", "manipulação", "manipulacao"
        ],
        "links_suspeitos": ["link", "links", "site suspeito"],
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

    resposta = conhecimento["descricao"]

    if "sinais" in conhecimento:
        resposta += "\n\nSinais de atenção:\n"
        for sinal in conhecimento["sinais"]:
            resposta += f"• {sinal}\n"

    if "recomendacoes" in conhecimento:
        resposta += "\nRecomendações:\n"
        for recomendacao in conhecimento["recomendacoes"]:
            resposta += f"• {recomendacao}\n"

    resposta += (
        "\nEstas orientações possuem caráter educacional e não substituem "
        "a análise de um profissional de cibersegurança."
    )

    return resposta


def responder_chat(mensagem, historico):
    return gerar_resposta(mensagem)


chat = gr.ChatInterface(
    fn=responder_chat,
    title="Blackwall AI",
    description=(
        "Assistente virtual educacional para orientação "
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
