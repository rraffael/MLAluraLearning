import csv

def carregar_acessos():
    
    X = []
    Y = []

    arquivo = open('acesso.csv', 'r')
    leitor = (csv.reader(arquivo))
    next(leitor)

    for home, busca, logado, comprou in leitor:

        dado = ([int(home), busca, int(logado)])
        X.append(dado)
        Y.append(int(comprou))

    return X, Y