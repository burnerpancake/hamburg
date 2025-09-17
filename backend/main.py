### Objeto ###
from sanduiche import Lanche
from cardapio import Cardapio


resposta = "S"

c = Cardapio()

while resposta == "S":

	ingredientes = []
	nome = input("Nome do sanduíche: ")
	preco = float(input("Preço do sanduíche: "))
	qtdeIngrediente = int(input("Informe quantos ingredientes você quer adicionar: "))

	l = Lanche(nome, preco, ingredientes)

	for item in range(qtdeIngrediente):
		ingrediente = input(f"({item + 1}/{qtdeIngrediente}) Informe o ingrediente: ")
		ingredientes.append(ingrediente)

	# Criando o objeto da classe Lanche dentro do laço
	print(f"Nome: {l.nome}\nPreço: R${l.preco}\nIngredientes: {l.ingredientes}")

	# Adicionando o lanche "l" ao cardapio "c"
	c.adicionarItem(l)
	resposta = input("Deseja adicionar outro item ao cardápio? (S/N): ").upper()

# Fim do laço while

c.exibirCardapio()