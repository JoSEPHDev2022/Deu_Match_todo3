# Definindo as variáveis e listas que serão usadas no programa:
# - dados_temporarios: uma lista que abriga temporariamente os inputs do usuário, inserindo os nomes e notas dos candidatos;
# - candidatos_e_notas: a lista final composta pelos candidatos e suas notas;
# - comparacao: lista que abriga os valores da nota de corte;
# - validNumbers: lista de prevenção de erros. Abriga os valores esperados na atribuição de notas;
# - e,t,p,s: notas de Entrevista, Teste Teórico, Teste Prático e Soft Skills do candidato no processo seletivo.
dados_temporarios = []
candidatos_e_notas = []
comparacao = []
validNumbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
e = ''
t = ''
p = ''
s = ''
e2 = ''
t2 = ''
p2 = ''
s2 = ''

# checkNotas(nota,letra): Função que checa a integridade do input. Faz com que os únicos valores
# aceitos para atribuição de notas sejam números inteiros de 0 a 10.
def checkNotas(nota, letra):
    while True:
        if nota not in validNumbers:
            print('Valor inválido! Apenas valores de 0 a 10 aceitos.')
            nota = int(input(f"Nota {letra}_: "))
            checkNotas(nota, letra)
        else:
            dados_temporarios.append(nota)
        break

# checkNotaCorte(nota,letra): Mesma função da função checkNotas, porém essa checa a integridade dos valores
# para as notas de corte.
def checkNotaCorte(nota, letra):
    while True:
        if nota not in validNumbers:
            print('Valor inválido! Apenas valores de 0 a 10 aceitos.')
            nota = int(input(f"Nota {letra}_: "))
            checkNotaCorte(nota, letra)
        else:
            comparacao.append(nota)
        break

# adicao_de_candidatos(): Função que aloja a parte de adição dos candidatos e suas notas, utilizando as funções
# de check para prevenir erros.
def adicao_de_candidatos():
    print("Bem vindo ao sistema de notas integrado da Empresa X!")
    print("A seguir, insira o nome e as notas dos candidatos\n")
    print("Notas devem ser números inteiros entre 0 e 10.")
    print("=*"*30)
    while True:
        dados_temporarios.append(str(input("Quem é o candidato? ")))

        notaE = int(input(f"Nota e_: {e}"))
        checkNotas(notaE, 'e')

        notaT = int(input(f"Nota t_: {t}"))
        checkNotas(notaT, 't')

        notaP = int(input(f"Nota p_: {p}"))
        checkNotas(notaP, 'p')

        notaS = int(input(f"Nota s_: {s}"))
        checkNotas(notaS, 's')

        candidatos_e_notas.append(dados_temporarios[:])
        dados_temporarios.clear()
        adicionar = str(input("Deseja adicionar outro candidato? [S/N] "))

        if adicionar in 'Ss':
            continue
        if adicionar in 'Nn':
            break
        if adicionar not in 'Nn' or 'Ss':
            print("Resposta inválida, use 'S' para sim ou 'N' para não.")
            adicionar = str(input("Deseja adicionar outro candidato? [S/N] "))
            adicao_de_candidatos()

    print("=*"*30)
    print("Candidatos aplicados:\n")

    for pessoas in candidatos_e_notas:
        print(f"{pessoas}")

    print(f"\nForam aplicados {len(candidatos_e_notas)} candidatos a lista.")
    print("=*"*30)
    filtragem_de_dados()

# filtragem_de_dados: Função que aloja os valores para a filtragem da lista de candidatos e notas
# e da função de check dessa nota de corte. Ao final, mostrando os candidatos que atendem aos requisitos
# de busca.
def filtragem_de_dados():
    print("Defina as notas de corte: ")
    notaE2 = int(input(f"Nota e_: {e2}"))
    checkNotaCorte(notaE2, 'e')
    notaT2 = int(input(f"Nota t_: {t2}"))
    checkNotaCorte(notaT2, 't')
    notaP2 = int(input(f"Nota p_: {p2}"))
    checkNotaCorte(notaP2, 'p')
    notaS2 = int(input(f"Nota s_: {s2}"))
    checkNotaCorte(notaS2, 's')
    print()
    print("=*"*30)

    while True:
        for pessoas, notas in enumerate(candidatos_e_notas, start=1):
            if notas[1] >= comparacao[0] and notas[2] >= comparacao[1] and notas[3] >= comparacao[2] and notas[4] >= comparacao[3]:
                print(f"Candidato {pessoas} ==> {notas[1:]} foi aprovado.")
            else:
                print(f"Nenhum candidato aprovado com no mínimo: e_:{comparacao[0]}, t_:{comparacao[1]}, p_:{comparacao[2]}, s_:{comparacao[3]}.\n")
            break
        exit()

adicao_de_candidatos()