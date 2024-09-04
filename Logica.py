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
                 # WHILE

nome = "Cegolas"               
experiencia = int("7000")

if experiencia < 1001:
        nivel = "Ferro" 
elif 1001 <= experiencia < 2001:
        nivel = "Bronze"
elif 2001 <= experiencia < 5001:
        nivel = "Prata"
elif 5001 <= experiencia < 7001:
        nivel = "Ouro"
elif 7001 <= experiencia < 8001:
        nivel = "Platina"
elif 8001 <= experiencia < 9001:
        nivel = "Ascendente"
elif 9001 <= experiencia < 10001:
        nivel = "Imortal"
elif 10001 <= experiencia:
        nivel = "Radiante"
    
print(f"O Herói de nome {nome} está no nível de {nivel}")
                             