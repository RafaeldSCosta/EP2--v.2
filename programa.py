from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida

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
        linha, coluna = -1, -1
        orientacao = "horizontal"
        while not posicao_valida(frota, linha, coluna, orientacao, info["tamanho"]):
            print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {info['tamanho']}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if nome_navio != "submarino":
                orientacao_input = int(input("[1] Vertical [2] Horizontal >"))
                orientacao = "vertical" if orientacao_input == 1 else "horizontal"
            else:
                orientacao = "horizontal"
            if not posicao_valida(frota, linha, coluna, orientacao, info["tamanho"]):
                print("Esta posição não está válida!")
        frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, info["tamanho"])

print(frota)