   # Terceiro desafio 
               # Python

class heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome    
        self.idade = idade
        self.tipo = tipo
        
    def exibir_detalhes(self, ataque , dano = 0):
        print(f"O(A) {self.tipo} {self.nome} atacou usando {ataque} e causou {dano} de dano no World Boss")
          
heroi1 = heroi("Cegolas", 23, "Arqueiro")       
heroi2 = heroi("SapoBoi", 29, "Guerreiro")
heroi3 = heroi("jaodalf", 37, "Mago")

heroi1.exibir_detalhes("Flecha de fogo", 80)
heroi2.exibir_detalhes("Espada longa",)
heroi3.exibir_detalhes("Feitiço de gelo", 50)

