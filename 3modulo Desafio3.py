class ConversorTemperatura:
    def celsius_para_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

# Entrada do usuário
celsius = float(input())

# Criando uma instância do conversor
conversor = ConversorTemperatura()

# Convertendo a temperatura de Celsius para Fahrenheit
fahrenheit = conversor.celsius_para_fahrenheit(celsius)

# Exibindo o resultado
print(fahrenheit)