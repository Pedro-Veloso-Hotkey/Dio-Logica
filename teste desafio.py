# No "TODO", abaixo: Crie a função 'soma_tupla' para receber uma tupla de números inteiros como argumento:
def soma_tupla(tupla):
    return sum(tupla)

if __name__ == "__main__":
    entrada = "2 5 6 7 9"
    entrada1 = "9 8 7 6 5"
    entrada2 = "50 50 50 50"
# No "TODO", abaixo: Defina tupla para receber os números inteiros:
    elementos = tuple(map(int, entrada.split()))
    elementos1 = tuple(map(int, entrada1.split()))
    elementos2 = tuple(map(int, entrada2.split()))
    
    resultado = soma_tupla(elementos)
    resultado1 = soma_tupla(elementos1)
    resultado2 = soma_tupla(elementos2)
    
    print(f"A soma dos elementos da tupla é: {resultado}")
    print(f"A soma dos elementos da tupla é: {resultado1}")
    print(f"A soma dos elementos da tupla é: {resultado2}")