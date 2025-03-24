import openai

# Defina sua chave da API OpenAI aqui
openai.api_key = 'sk-proj-eat1WO25SPs4WySHPddSrH0U5rvgseBWlYOjdcLYxdDKj3gHeofWPzS2iHCHWfJs6Z2NOXddFBT3BlbkFJNFyo8bSmSZaqdZf6ejDcPAA8UYKE0VIERiF7i4uNEEWc_jczxUlD7yoY20mJRSMf2ACrvVcGoAq'

def obter_resposta_gpt(pergunta):
    try:
        # Enviando a pergunta para o modelo GPT-3 ou GPT-4
        resposta = openai.Completion.create(
            model="gpt-3.5-turbo",  # ou "gpt-4" se você tiver acesso
            prompt=pergunta,
            max_tokens=1000,  # Limita o número de tokens na resposta
            n=1,  # Número de respostas geradas
            stop=None,  # Não utilizar nenhum caractere para finalizar a resposta
            temperature=0.7,  # Controla a aleatoriedade das respostas
        )
        # Retorna o conteúdo da resposta gerada
        return resposta.choices[0].text.strip()
    except Exception as e:
        return f"Erro ao obter resposta: {e}"

def iniciar_chat():
    print("Olá! Eu sou um chatbot. Pode me perguntar qualquer coisa.")
    print("Digite 'sair' para encerrar a conversa.")
    
    while True:
        # Recebe a pergunta do usuário
        pergunta = input("Você: ")
        
        # Caso o usuário digite 'sair', encerra o chatbot
        if pergunta.lower() in ['sair', 'exit', 'bye']:
            print("Chatbot: Até logo!")
            break
        
        # Obter resposta do GPT-3 ou GPT-4
        resposta = obter_resposta_gpt(pergunta)
        
        # Exibe a resposta do chatbot
        print(f"Chatbot: {resposta}")

if __name__ == "__main__":
    iniciar_chat()