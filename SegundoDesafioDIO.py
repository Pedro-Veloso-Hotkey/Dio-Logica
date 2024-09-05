          # Segundo desafio DIO Formação Lógica de Programação
# função para o calculo que vai ser utilizado 
def saldo(vitoria, derrota):
    return vitoria - derrota

# Número de vitorias e derrotas para o calculo
vitoria = int("94")   # < pode ser input antes do int para interação com usuário
derrota = int("19")   # <

# Váriavel para fazer o calculo da função saldo com o valor fornecido pelas variaveis Vitoria e derrota
saldoVitorias = saldo(vitoria, derrota)  

# Estrutura de decisões  
if saldoVitorias < 10:
    nivel = "Ferro"
elif 11 <= saldoVitorias < 20:
    nivel = "Bronze"
elif 21 <= saldoVitorias < 50:
    nivel = "Prata"   
elif 51 <= saldoVitorias < 80:
    nivel = "Ouro"    
elif 81 <= saldoVitorias < 90:
    nivel = "Diamante"
elif 91 <= saldoVitorias < 100:
    nivel = "Lendário"
elif 101 <= saldoVitorias:
    nivel = "Imortal"

# Saída 
print(f"O Herói tem saldo de {saldoVitorias} vitorias e está no rank de {nivel}")











