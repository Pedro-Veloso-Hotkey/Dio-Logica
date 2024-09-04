class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método para retornar as informações formatadas
    def obter_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

# Entrada do usuário
nome = input()
idade = int(input())

# Criando uma instância da pessoa
pessoa = Pessoa(nome, idade)

# Chamando o método para retornar as informações formatadas e imprimindo o resultado
informacoes = pessoa.obter_informacoes()
print(informacoes)