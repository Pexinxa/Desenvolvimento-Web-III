from Perguntas import perguntas
from Quiz import Quiz

nome = input("Digite seu nome: ").strip()
quiz = Quiz(nome)
quiz.iniciarQuiz()

for i, pergunta in enumerate(perguntas, start=1):
    resposta = quiz.perguntar(pergunta, i)
    quiz.responder(resposta, pergunta["resposta"])

quiz.exibirResultado()