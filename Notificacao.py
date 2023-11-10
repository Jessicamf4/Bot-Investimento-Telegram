import requests

def enviar_mensagem(token, chat_id, mensagem):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    parametros = {"chat_id": chat_id, "text": mensagem}
    resposta = requests.get(url, params=parametros)
    enviarJson(token, chat_id, resposta.json())
    return resposta.json()
    
def enviarJson(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    parametros = {"chat_id": chat_id, "text": text}
    resposta = requests.get(url, params=parametros)



