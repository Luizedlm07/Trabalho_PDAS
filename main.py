from Jogo.jogo import Jogo

if __name__ == "__main__":
    jogo = Jogo()
    alvo_atual = jogo.iniciar_jogo()
    
    while alvo_atual <= 100:
        palpite_usuario = int(input("Dê seu palpite: "))
        resultado = jogo.jogar(palpite_usuario)

        if resultado:
            print("Parabéns! Você acertou o alvo. Vitória do usuário!")
            break
        else:
            alvo_atual = jogo.alvo
            print(f"Alvo atual: {alvo_atual}")

    if alvo_atual >= 100:
        print("Você perdeu :(")
