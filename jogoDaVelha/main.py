from jogo_da_velha import criaBoard, printBoard, getInputValido, verificaMovimento, fazMovimento, verificaGanhador

jogador = 0

board = criaBoard()
ganhador = verificaGanhador(board)

print("-"*20)

while(not ganhador):
    printBoard(board)
    i = getInputValido("Digite a linha: ")
    j = getInputValido("Digite a coluna: ")

    if verificaMovimento(board, i, j):
        fazMovimento(board, i, j, jogador)
        jogador = (jogador + 1) % 2 # troca de joagador
    else:
        print("Movimento invalido!")

    ganhador = verificaGanhador(board)

print("-"*20)
printBoard(board)
print("-"*20)
print("GANHADOR: ", ganhador)