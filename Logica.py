# reset_de_senha = "Enviamos um link para o reset de senha no e-mail cadastrado"
# segunda_via = "Gerando o Boleto"

# nome = input("Digite seu nome: ")

# print(f"Bem-vindo(a), {nome}! Como posso lhe ajudar?\n"
#       "1 - Reset de senha\n"
#       "2 - 2ª Via da conta\n"
#       "3 - Outros")

# # Captura a escolha do usuário
# opcao = int(input("Digite o número da opção desejada: "))

# # Verifica a escolha do usuário e imprime a mensagem correspondente
# if opcao == 1:
#     print(reset_de_senha)
# elif opcao == 2:
#     print(segunda_via)
# else:
#     print("Outros serviços não estão disponíveis no momento.")
  
#--------------------------------------------------------------------------------------------------------#      
                  #teste
                 
# nome = input("digite o seu nome : ")
# print("Bem vindo(a) " + nome)

#                 lista, dicionario 

# carros = ["Dodge", "Mustang", "Corola", "Civic"]

# def compra_carro(escolha):
#     return carros[escolha]

# escolha = int(input("Digite um número de 0-3 "))
# carro_selecionado = compra_carro(escolha)

# print(f"O carro selecionado foi o {carro_selecionado}.")  

          #-------------x-------------------#

# idade = int(input("Digite sua idade: "))
# visto = str(input("Possui visto? responda apenas Sim ou Não : "))  

# if idade >= 18 and visto == "sim" :
#     print("pode entrar")
# else:
#     print("você não pode entrar")

          # ---------------x--------------- #
# idade_minima = 18
# idade_usuario = 18
# idade_permitida_valida = idade_usuario >= idade_minima

# print(idade_permitida_valida)
#                    ----------x------------
                 # desafio 1 

# nome = "Cegolas"               
# experiencia = int("1000")

# if experiencia < 1000:
#         nivel = "Ferro" 
# elif 1000 <= experiencia <= 2000:
#         nivel = "Bronze"
# elif 2000 <= experiencia <= 5000:
#         nivel = "Prata"
# elif 5000 <= experiencia <= 7000:
#         nivel = "Ouro"
# elif 7000 <= experiencia <= 8000:
#         nivel = "Platina"
# elif 8000 <= experiencia <= 9000:
#         nivel = "Ascendente"
# elif 9000 <= experiencia <= 10000:
#         nivel = "Imortal"
# elif 10000 <= experiencia:
#         nivel = "Radiante"
    
# print(f"O Herói de nome {nome} está no nível de {nivel}")

#           ------Funções----------

# def torrar(pao, valor, nome = "Cliente"):
#     print(f"torrada feita com {pao}")
#     print(f"Foi um pedido de {nome}") 
#     print(f"o preço é {valor}") 
# # Chamando a função com o argumento "pão de forma"
# torrar("pão de forma","10,90", "Pedro")
# # torrar("pão integral", "Jose")
#--------------------------------x---------------------------
           # Código em JS
# torrar("pão de forma")

# function torrar(pao){
#         console.log("torrada feita com " + pao)
# }
#---------------------------x----------------------------
#               Desafio 1

# posicaoInicial = int(input())
# totalPassos = int(input())

# posicaoFinal = (posicaoInicial + totalPassos)

# print(f"Posição final do heroi {posicaoFinal}")

#-------------------------x--------------------

class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome  # Propriedade 'nome'
        self.preco = preco  # Propriedade 'preço'
        self.categoria = categoria  # Propriedade 'categoria'

    def exibir_detalhes(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Categoria: {self.categoria}")

# Criando uma instância da classe Produto
produto1 = Produto("Laptop", 3500.00, "Eletrônicos")

# Chamando o método que exibe os detalhes do produto
produto1.exibir_detalhes()