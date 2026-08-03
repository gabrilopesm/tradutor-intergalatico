tabela_sinais = {"zog": "Olá",
                 "blip": "Humano",
                 "glub": "Paz",
                 "krak": "Perigo"
}

def traduzir_palavra(palavra):
    try:
        return tabela_sinais[palavra]

    except KeyError:
        return "[DESCONHECIDO]"

def decodificar_mensagem(mensagem_bruta):
    mensagem_traduzida = []
    mensagem = mensagem_bruta.split()

    for palavra in mensagem:
        palavra_traduzida = traduzir_palavra(palavra)
        mensagem_traduzida.append(palavra_traduzida)

    return ' '.join(mensagem_traduzida)

print(" =========== TRADUTOR INTERGALÁTICO ===========\n v1.0.1 \n")
opcao = input("DIGITE [PALAVRA] PARA CONSULTAR UMA PALAVRA OU [FRASE] PARA CONSULTAR UMA FRASE >>> ").upper()

if opcao == "PALAVRA":
    palavra = input("SINAL RECEBIDO >>> ").lower()
    print(f"Tradução de {palavra} = {traduzir_palavra(palavra)}")

elif opcao == "FRASE":
    frase = input("SINAL RECEBIDO >>> ").lower()
    print(f"\n >>> MENSAGEM TRADUZIDA: {decodificar_mensagem(frase)}")

elif opcao == "SAIR" or opcao == "FECHAR" or opcao == "ENCERRAR":
    print("\nSaindo do sistema...")
    exit()

else:
    print("\nComando desconhecido.\nEncerrando sistema...")
    exit()