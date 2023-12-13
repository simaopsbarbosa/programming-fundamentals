def tic_tac_toe(board: str, player):
    correspondencia = {0:"A", 1:"B", 2:"C"}
    
    # check linhas
    for i in range(3):
        linha = [board[4 * i], board[4 * i + 1], board[4 * i + 2]]
        if linha.count(player) == 2 and linha.count(' ') == 1:
            return f"{correspondencia.get(i)}{linha.index(' ')+1}"
    
    # check colunas
    for i in range(3):
        coluna = [board[i], board[4 + i], board[8 + i]]
        if coluna.count(player) == 2 and coluna.count(' ') == 1:
            return f"{correspondencia.get(coluna.index(' '))}{i+1}"
        
    # check diagonais
    diag1 = [board[8], board[5], board[2]]
    if diag1.count(player) == 2 and diag1.count(' ') == 1:
        corr2 = {0:"C1", 1:"B2", 2:"A3"}
        return f"{corr2.get(diag1.index(' '))}"
    
    diag2 = [board[0], board[5], board[10]]
    if diag2.count(player) == 2 and diag2.count(' ') == 1:
        corr2 = {0:"A1", 1:"B2", 2:"C3"}
        return f"{corr2.get(diag2.index(' '))}"
    
