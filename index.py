# =========================
# VANTAGENS DE TIPOS
# =========================

vantagens = {
    "fogo": "planta",
    "agua": "fogo",
    "planta": "agua",
    "eletrico": "agua",
    "lutador": "noturno",
    "psiquico": "lutador",
    "noturno": "psiquico"
}

# =========================
# CLASSE POKEMON
# =========================

class Pokemon:
    def __init__(self, nome, tipo, fraquezas):
        self.nome = nome
        self.tipo = tipo
        self.hp = 100
        self.fraquezas = fraquezas

    def atacar(self, outro):
        print("Ações de", self.nome)
        print("1 - Ataque fraco (10)")
        print("2 - Ataque forte (20)")
        print("3 - Curar (15 HP)")
        print("4 - Fugir")

        escolha = input("Escolha: ")

        if escolha == "1":
            dano = 10
            tipo_ataque = self.tipo

        elif escolha == "2":
            dano = 20
            tipo_ataque = self.tipo

        elif escolha == "3":
            self.hp += 15
            print(self.nome, "se curou!")
            return "continuar"

        elif escolha == "4":
            print(self.nome, "fugiu da batalha!")
            return "fugiu"   # ✅ corrigido aqui

        else:
            print("Opção inválida!")
            return "continuar"

        # vantagem de tipo
        if vantagens.get(self.tipo) == outro.tipo:
            dano *= 2
            print("Super efetivo (tipo)!")

        # fraqueza específica
        if tipo_ataque in outro.fraquezas:
            dano *= 2
            print("Fraqueza explorada!")

        print(self.nome, "atacou", outro.nome, "e causou", dano, "de dano!")
        outro.hp -= dano

        return "continuar"

# =========================
# CLASSE TREINADOR
# =========================

class Treinador:
    def __init__(self, nome):
        self.nome = nome
        self.pokemon = None

    def escolher_pokemon(self, lista):
        print(self.nome, "escolha seu Pokémon:")

        for i, p in enumerate(lista):
            print(i, "-", p.nome, "(", p.tipo, ")")

        escolha = int(input("Número: "))
        self.pokemon = lista.pop(escolha)

# =========================
# BATALHA
# =========================

def batalha(t1, t2):
    while t1.pokemon.hp > 0 and t2.pokemon.hp > 0:
        print("--- BATALHA ---")

        resultado = t1.pokemon.atacar(t2.pokemon)
        if resultado == "fugiu":
            print(t1.nome, "fugiu!")
            print(t2.nome, "venceu a batalha!")
            break

        if t2.pokemon.hp <= 0:
            print(t2.pokemon.nome, "desmaiou!")
            print(t1.nome, "venceu a batalha!")
            break

        resultado = t2.pokemon.atacar(t1.pokemon)
        if resultado == "fugiu":
            print(t2.nome, "fugiu!")
            print(t1.nome, "venceu a batalha!")
            break

        if t1.pokemon.hp <= 0:
            print(t1.pokemon.nome, "desmaiou!")
            print(t2.nome, "venceu a batalha!")
            break

        print("HP", t1.pokemon.nome + ":", t1.pokemon.hp)
        print("HP", t2.pokemon.nome + ":", t2.pokemon.hp)

# =========================
# JOGO
# =========================

pokemons = [
    Pokemon("Charmander", "fogo", ["agua"]),
    Pokemon("Squirtle", "agua", ["eletrico", "planta"]),
    Pokemon("Bulbasaur", "planta", ["fogo"]),
    Pokemon("Pikachu", "eletrico", ["lutador"]),
    Pokemon("Lucario", "lutador", ["psiquico"]),
    Pokemon("Abra", "psiquico", ["noturno"]),
    Pokemon("Umbreon", "noturno", ["lutador"])
]

t1 = Treinador("Jogador 1")
t2 = Treinador("Jogador 2")

t1.escolher_pokemon(pokemons)
t2.escolher_pokemon(pokemons)

batalha(t1, t2) 
