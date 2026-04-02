from Perguntas import perguntas
class Quiz:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0
 
    def iniciarQuiz(self):
        print("=" * 50)
        print("QUIZ PYTHON")
        print("=" * 50)
        print(f"\nOlá, {self.nome}! O quiz possui {len(perguntas)} questões.")
        input("Pressione ENTER para começar...\n")
    
    def perguntar(self, pergunta, numero):
        alternativas_validas = [alt[0] for alt in pergunta["alternativas"]]
 
        while True:
            print(f"[{numero}/{len(perguntas)}] {pergunta['enunciado']}\n")
            for alternativa in pergunta["alternativas"]:
                print(f"  {alternativa}")
 
            resposta = input("\nSua resposta: ").strip().upper()
 
            if resposta in alternativas_validas:
                return resposta
            else:
                print(f"\n Resposta inválida! Digite uma das letras: {', '.join(alternativas_validas)}\n")
 
    def responder(self, resposta_aluno, resposta_correta):
        if resposta_aluno == resposta_correta:
            print("Correto!\n")
            self.pontuacao += 1
        else:
            print(f"Errado! Resposta correta: {resposta_correta}\n")
 
    def exibirResultado(self):
        total = len(perguntas)
        percentual = (self.pontuacao / total) * 100
 
        if percentual >= 90:
            situacao = "Excelente!"
        elif percentual >= 70:
            situacao = "Bom desempenho!"
        elif percentual >= 50:
            situacao = "Desempenho regular."
        else:
            situacao = "Abaixo da média."
 
        print("=" * 50)
        print(f"  Aluno     : {self.nome}")
        print(f"  Acertos   : {self.pontuacao}/{total}")
        print(f"  Aproveit. : {percentual:.1f}%")
        print(f"  Situação  : {situacao}")
        print("=" * 50)