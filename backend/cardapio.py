### Classe ###
class Cardapio:
	def __init__(self):
		self.itens = []
		self.categoria = ""
	
	# Fim do construtor

	def __str__(self):
		return f"Item: {self.itens}"

	# CRIAÇÃO DO MÉTODO ADICIONAR ITEM
	def adicionarItem(self, item):
		"""
		Adiciona um objeto (item) da classe Lanche ao cardápio
		"""
		self.itens.append(item)
	
	# Fim do método adicionarItem

	def exibirCardapio(self):
		for item in self.itens:
			item.exibirLanche()

# Fim da classe
