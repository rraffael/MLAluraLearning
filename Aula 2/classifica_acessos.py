from dados import carregar_acessos
from sklearn.naive_bayes import MultinomialNB

X, Y = carregar_acessos()

# 90% do modelo utilizado para treino
treinoDados = X[:90]
treinoMarcacoes = Y[:90]
# 10% para teste
teste_dados = X[-9:]
teste_marcacoes = Y[-9:]

modelo = MultinomialNB()
modelo.fit(treinoDados, treinoMarcacoes)

resultado = modelo.predict(teste_dados)

diferencas = resultado - teste_marcacoes

acertos = [d for d in diferencas if d == 0]

totalAcertos = len(acertos)
totalElementos = len(teste_dados)

taxaAcerto = 100*(totalAcertos / totalElementos)

print(taxaAcerto)
print(totalElementos)