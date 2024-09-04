          # Primeiro Desafio DIO Logistica 

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