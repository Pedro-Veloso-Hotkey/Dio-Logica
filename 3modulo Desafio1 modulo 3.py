class Calculadora:
    def soma(self, num1, num2):
        return num1 + num2

# Solicita entrada do usuário
num1 = int(input())
num2 = int(input())

# Criando uma instância da calculadora
calc = Calculadora()

# Realizando a soma e imprimindo o resultado
resultado = calc.soma(num1, num2)
print(resultado)