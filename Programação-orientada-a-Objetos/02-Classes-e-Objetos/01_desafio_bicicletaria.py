class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor       

    def buzinar(self):
        print("Plim plim")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicleta parada")

    def correr(self):
        print("Vrummmmm....")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar() # Bicileta.buzinar(b1)
b1.correr()
b1.parar()
print(f"Bicleta cor: {b1.cor}, marca: {b1.modelo}, ano: {b1.ano} no valor de : R${b1.valor:.2f}")
print(b1)