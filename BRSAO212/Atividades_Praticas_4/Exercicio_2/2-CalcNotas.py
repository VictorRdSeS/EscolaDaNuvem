#2 - Criar um código que registre as notas de alunos e calcular a média da turma.

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

notas_alunos = []
while True:
    entrada = input("Digite a nota do aluno (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas_alunos.append(nota)
        else:
            print("Por favor, insira uma nota válida entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número ou 'sair'.")
media_turma = calcular_media(notas_alunos)
print(f"A média da turma é: {media_turma:.2f}")
