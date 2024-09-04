def contar_caracteres(string):
    contador = {}
    for caracteres in string:
        if caracteres in contador:
            contador[caracteres] += 1
        else:
            contador[caracteres] = 1
    
    return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)