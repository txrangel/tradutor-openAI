import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key      = os.getenv("OPENAI_API_KEY")
openai.Model.list()

def traduzir(texto,idioma):
    response            = openai.Completion.create(
    model               = "text-davinci-003",
    prompt              = "Traduza esse texto: '{texto}', para esse idioma: '{idioma}'",
    temperature         = 0.5,
    max_tokens          = 500,
    n                   = 1.0,
    stop                = None
    )
    return response['choice'][0]['text'].strip()

textotraducao   = input("Digite o texto para ser traduzido: ")
idiomatraducao  = input("Digite o idioma para qual deseja traduzir: ")
traducao        = traduzir(textotraducao,idiomatraducao)
print(f"Tradução do texto para {idiomatraducao}: {traducao}")