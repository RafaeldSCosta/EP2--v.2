def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = []
    frota[nome_navio].append(posicoes)
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        linha = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        tabuleiro.append(linha)

    for nome_navio in frota:
        for navio in frota[nome_navio]:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro

def afundados(frota, tabuleiro):
    contador = 0
    for nome_navio in frota:
        for navio in frota[nome_navio]:
            afundou = True
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] != "X":
                    afundou = False
            if afundou == True:
                contador = contador + 1
    return contador

def posicao_valida(frota,linha, coluna, orientacao, tam):
    posicoes= define_posicoes(linha, coluna, orientacao, tam)
    for line, column in posicoes:
        if line <0 or line>9 or column<0 or column>9:
            return False
    
    for nome in frota:
        for navio in frota[nome]:
            for posicao in navio:
                if posicao in posicoes:
                    return False
    return True

    