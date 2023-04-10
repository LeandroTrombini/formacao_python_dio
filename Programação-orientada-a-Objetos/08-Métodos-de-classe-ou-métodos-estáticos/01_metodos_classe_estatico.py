class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia , nome):
        idade = 2023 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18

p = Pessoa.criar_de_data_nascimento(1982, 12, 28, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.maior_idade(20))
print(Pessoa.maior_idade(14))