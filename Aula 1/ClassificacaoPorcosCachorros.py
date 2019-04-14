from sklearn.naive_bayes import MultinomialNB

# [Gordinho?, Perna curta?, Faz auau?]
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

# Array dados
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# [Porco, Porco, Porco, Cachorro, Cachorro, Cachorro]
marcacoes = [1, 1, 1, -1, -1, -1]

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

misterioso = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]

teste = [misterioso, misterioso2, misterioso3]

#Cachorro, Porco, Cachorro
marcacoes_teste = [-1, 1, 1]

resultado = modelo.predict(teste)

diferencas = resultado - marcacoes_teste

total_de_acertos = len([d for d in diferencas if d == 0])
total_de_elementos = len(teste)

taxa_de_acerto = (total_de_acertos / total_de_elementos)*100

print(resultado)
print(diferencas)
print(taxa_de_acerto)