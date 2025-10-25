import random
from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida, monta_tabuleiros

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []}

navios = {
    "porta-aviões": {"quantidade": 1, "tamanho": 4},
    "navio-tanque": {"quantidade": 2, "tamanho": 3},
    "contratorpedeiro": {"quantidade": 3, "tamanho": 2},
    "submarino": {"quantidade": 4, "tamanho": 1}}

for nome_navio, info in navios.items():
    for i in range(info["quantidade"]):
        while True:
            print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {info['tamanho']}")
            
            while True:
                try:
                    linha = int(input("Linha: "))
                    if 0 <= linha <= 9:
                        break
                    print("Linha inválida!")
                except ValueError:
                    print("Linha inválida!")
                    
            while True:
                try:
                    coluna = int(input("Coluna: "))
                    if 0 <= coluna <= 9:
                        break
                    print("Coluna inválida!")
                except ValueError:
                    print("Coluna inválida!")

            if nome_navio != "submarino":
                while True:
                    try:
                        orientacao_input = int(input("[1] Vertical [2] Horizontal >"))
                        if orientacao_input in [1, 2]:
                            orientacao = "vertical" if orientacao_input == 1 else "horizontal"
                            break
                        print("Opção inválida.")
                    except ValueError:
                        print("Opção inválida.")
            else:
                orientacao = "horizontal"

            if posicao_valida(frota, linha, coluna, orientacao, info["tamanho"]):
                frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, info["tamanho"])
                break
            else:
                print("Esta posição não está válida!")
            

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

total_navios_oponente = 0
for lista in frota_oponente.values():
    total_navios_oponente += len(lista)

jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    while True:
        while True:
            entrada_linha = input("Jogador, qual linha deseja atacar? ")
            try:
                linha_input = int(entrada_linha)
                if 0 <= linha_input <= 9:
                    break
                print("Linha inválida!")
            except ValueError:
                print("Linha inválida!")

        while True:
            entrada_coluna = input("Jogador, qual coluna deseja atacar? ")
            try:
                coluna_input = int(entrada_coluna)
                if 0 <= coluna_input <= 9:
                    break
                print("Coluna inválida!")
            except ValueError:
                print("Coluna inválida!")

        if str(tabuleiro_oponente[linha_input][coluna_input]) in "X-":
            print(f"A posição linha {linha_input} e coluna {coluna_input} já foi informada anteriormente!")
            continue
        else:
            break
            
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_input, coluna_input)

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios_oponente:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
        break

    while True:
        lin_oponente = random.randint(0, 9)
        col_oponente = random.randint(0, 9)
        if str(tabuleiro_jogador[lin_oponente][col_oponente]) not in "X-":
            print(f"Seu oponente está atacando na linha {lin_oponente} e coluna {col_oponente}")
            tabuleiro_jogador = faz_jogada(tabuleiro_jogador, lin_oponente, col_oponente)
            break

    if afundados(frota, tabuleiro_jogador) == total_navios_oponente:
        print("Xi! O oponente derrubou toda a sua frota =(")
        jogando = False
        break
