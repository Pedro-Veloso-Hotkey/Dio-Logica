          # Primeiro Desafio DIO Logistica 

nome = "Cegolas"          # ou input para interação com usuário    
experiencia = int("7000")  # ou input 

if experiencia < 1000:
        nivel = "Ferro" 
elif 1000 <= experiencia < 2000:
        nivel = "Bronze"
elif 2000 <= experiencia < 5000:
        nivel = "Prata"
elif 5000 <= experiencia < 7000:
        nivel = "Ouro"
elif 7000 <= experiencia < 8000:
        nivel = "Platina"
elif 8000 <= experiencia < 9000:
        nivel = "Ascendente"
elif 9000 <= experiencia < 10000:
        nivel = "Imortal"
elif 10000 <= experiencia:
        nivel = "Radiante"
    
print(f"O Herói de nome {nome} está no nível de {nivel}")