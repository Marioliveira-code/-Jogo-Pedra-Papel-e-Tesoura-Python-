from enum import Enum
import random

# Definição das formas possíveis no jogo
class Forma(Enum):
    PEDRA = 'pedra'
    PAPEL = 'papel'
    TESOURA = 'tesoura'

# Classe que representa o jogador
class Jogador:
    def __init__(self):
        self.pontuacao = 0
        self.formas = [Forma.PEDRA.name, Forma.PAPEL.name, Forma.TESOURA.name]
        self.nome = input("Digite seu nome: ")  # Solicita o nome do jogador
    
    # Método para o jogador escolher uma forma
    def escolher(self):
        while True:
            entrada_usuario = input("Por favor, insira sua escolha (pedra, papel, tesoura): ").upper()
            if entrada_usuario in self.formas:
                print(f"Usuário escolheu: {entrada_usuario}")
                return entrada_usuario
            print("Opção inválida. Por favor, tente novamente (pedra, papel, tesoura): ")

# Classe que representa o computador
class Computador:
    def __init__(self):
        self.pontuacao = 0
        self.formas = [Forma.PEDRA.name, Forma.PAPEL.name, Forma.TESOURA.name]
        self.nome = "Computador"

    # Método para o computador escolher uma forma aleatoriamente
    def escolher(self):
        escolha = random.choice(self.formas)
        print(f"Computador escolheu: {escolha}")
        return escolha

# Classe que gerencia o jogo
class Jogo:
    def __init__(self):
        self.max_rodadas = 3  # Define um número padrão de rodadas
        self.rodada = 0
        self.computador = Computador()
        self.jogador = Jogador()
        self.historico = []  # Lista para armazenar o histórico das jogadas
        self.frases_vitoria = [
            "Parabéns! Você arrasou nessa rodada!",
            "Incrível! Você está dominando o jogo!",
            "Boa! Continue assim e a vitória será sua!"
        ]
        self.frases_derrota = [
            "Não desista! Você pode virar o jogo!",
            "Continue tentando, a próxima rodada é sua!",
            "Não se preocupe, até os melhores perdem às vezes!"
        ]

    # Método principal para jogar o jogo
    def jogar(self):
        while self.rodada < self.max_rodadas:
            escolha_jogador = self.jogador.escolher()
            escolha_computador = self.computador.escolher()
            self.historico.append((escolha_jogador, escolha_computador))  # Armazena as escolhas no histórico
            self.ajustar_pontuacao(escolha_computador, escolha_jogador)
            self.mostrar_pontuacoes()
        self.mostrar_historico()  # Exibe o histórico ao final do jogo
        vencedor = self.determinar_vencedor()
        print(f"{vencedor} VENCEU!")

    # Método para ajustar a pontuação com base nas escolhas
    def ajustar_pontuacao(self, escolha_computador, escolha_jogador):
        # pedra > tesoura
        # papel > pedra
        # tesoura > papel
        if escolha_computador == escolha_jogador:
            print("Empate! Ninguém pontuou nesta rodada.")
            return
        if ((escolha_computador == Forma.PEDRA.name and escolha_jogador == Forma.TESOURA.name) or
            (escolha_computador == Forma.PAPEL.name and escolha_jogador == Forma.PEDRA.name) or
            (escolha_computador == Forma.TESOURA.name and escolha_jogador == Forma.PAPEL.name)):
            self.computador.pontuacao += 1
            print(random.choice(self.frases_derrota))  # Exibe uma frase motivacional
        else:
            self.jogador.pontuacao += 1
            print(random.choice(self.frases_vitoria))  # Exibe uma frase de vitória
        self.rodada += 1

    # Método para determinar o vencedor do jogo
    def determinar_vencedor(self):
        return self.computador.nome if self.computador.pontuacao > self.jogador.pontuacao else self.jogador.nome
    
    # Método para exibir as pontuações atuais
    def mostrar_pontuacoes(self):
        print(f"Pontuação do {self.jogador.nome}: {self.jogador.pontuacao}")
        print(f"Pontuação do {self.computador.nome}: {self.computador.pontuacao}")

    # Método para exibir o histórico das jogadas
    def mostrar_historico(self):
        print("\nHistórico das jogadas:")
        for i, (jogador, computador) in enumerate(self.historico, start=1):
            print(f"Rodada {i}: Jogador escolheu {jogador}, Computador escolheu {computador}")

# Execução principal do programa
if __name__ == "__main__":
    jogo = Jogo()
    jogo.jogar()
