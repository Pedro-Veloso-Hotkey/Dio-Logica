          # Primeiro Desafio DIO Logistica 
          # Feito em Python

nome = "Cegolas"          # ou input para interação com usuário    
experiencia = int("7000")  # ou input 

if experiencia < 1000:
        nivel = "Ferro" 
elif 1001 <= experiencia <= 2000:
        nivel = "Bronze"
elif 2001 <= experiencia <= 5000:
        nivel = "Prata"
elif 5001 <= experiencia <= 7000:
        nivel = "Ouro"
elif 7001 <= experiencia <= 8000:
        nivel = "Platina"
elif 8001 <= experiencia <= 9000:
        nivel = "Ascendente"
elif 9001 <= experiencia <= 10000:
        nivel = "Imortal"
elif 10001 <= experiencia:
        nivel = "Radiante"
    
print(f"O Herói de nome {nome} está no nível de {nivel}")
