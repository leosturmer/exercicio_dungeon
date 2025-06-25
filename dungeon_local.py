
# Model do dungeon

objetos = [
        {"nome": "Rocha", "genero": "f", "dano": 0, "protecao": 0},
        {"nome": "Espada", "genero": "f", "dano": 5, "protecao": 0},
        {"nome": "Capa", "genero": "f", "dano": 0, "protecao": 0},
        {"nome": "Foice", "genero": "f", "dano": 2, "protecao": 0},
        {"nome": "Capacete", "genero": "m", "dano": 0, "protecao": 5},
        {"nome": "Peitoral", "genero": "m", "dano": 0, "protecao": 5},
        {"nome": "Calça", "genero": "f", "dano": 0, "protecao": 5},
        {"nome": "Picareta", "genero": "f", "dano": 3, "protecao": 0},
        {"nome": "Machado", "genero": "m", "dano": 4, "protecao": 0},
        {"nome": "Cenoura", "genero": "f", "dano": 0, "protecao": 0},
        {"nome": "Gema", "genero": "f", "dano": 0, "protecao": 0},
        {"nome": "Moeda", "genero": "f", "dano": 0, "protecao": 0}
    ]

adjetivos = [
        {"f": "Feroz", "m": "Feroz", "dano": 5, "protecao": 0},
        {"f": "Fulminante", "m": "Fulminante", "dano": 5, "protecao": 0},
        {"f": "Vingativa", "m": "Vingativo", "dano": 5, "protecao": 0},
        {"f": "Bela como a Lua", "m": "Belo como a Lua", "dano": 0, "protecao": 0},
        {"f": "Reluzente", "m": "Reluzente", "dano": 0, "protecao": 0},
        {"f": "Fervescente", "m": "Fervescente", "dano": 0, "protecao": 0}
    ]

complementos = [
        {"f": "Forjada na lua", "m": "Forjado na lua", "dano": 5, "protecao": 5},
        {"f": "do Minotauro", "m": "do Minotauro", "dano": 5, "protecao": 5},
        {"f": "dos confins do inferno",
            "m": "dos confins do inferno", "dano": 0, "protecao": 0},
        {"f": "Enferrujada", "m": "Enferrujado", "dano": -2, "protecao": -2},
        {"f": "Perfeita", "m": "Perfeito", "dano": 0, "protecao": 0},
        {"f": "Usada pelo Rei de Minas",
            "m": "Usado pelo Rei de Minas", "dano": 0, "protecao": 0}
    ]


import random

class Item:

    def __init__(self):
        self.dano = 0
        self.protecao = 0
        self.nome = str()
       
        self.objeto = random.choice(objetos)
        self.adjetivo = random.choice(adjetivos)
        self.complemento = random.choice(complementos)

        self.dano = self.objeto["dano"] + self.adjetivo["dano"] + self.complemento["dano"]
        
        self.protecao = self.objeto["protecao"] + self.adjetivo["protecao"] + self.complemento["protecao"]
        
        self.genero_objeto = self.objeto["genero"]

        self.nome = f"{self.objeto["nome"]} {self.adjetivo[self.genero_objeto]} {self.complemento[self.genero_objeto]}"
        

    def get_nome(self):
        return self.nome

    def get_quant(self):
        return self.quant

    def set_dano(self, novo_Dano):
        self.dano = novo_Dano

    def get_dano(self):
        return self.dano

    def set_protecao(self, nova_protecao):
        self.protecao = nova_protecao

    def get_protecao(self):
        return self.protecao

    def __str__(self):
        if self.dano > 0:
            return f"Item [Nome: {self.get_nome()}, dano = {self.get_dano()}]"

        if self.protecao > 0:
            return f"Item [Nome: {self.get_nome()}, protecao = {self.protecao}]"

        if self.dano > 0 and self.protecao > 0:
            return f"Item [Nome: {self.get_nome()}, dano = {self.get_dano()}, protecao = {self.protecao}]"

        return f"Item [Nome: {self.get_nome()}"

class Cena():
    def __init__(self, nome="Indefinida"):
        # identificação
        self.nome = nome

        self.itens = dict()

        # Cenas conectadas a esta cena
        self.norte = None
        self.sul = None
        self.leste = None
        self.oeste = None

    def colocar_item(self, nome_item, um_item):
        um_item.nome = nome_item # para testes, sobrescrevemos o nome do item
        self.itens[um_item.get_nome()] = um_item

    def coletar_item(self, nome_item):
        # pegamos o item
        item_coletado = self.itens[nome_item]
        # retirar item da sala
        del self.itens[nome_item]
        # retornamos o item
        return item_coletado

    def __str__(self):
        return f'''
[{self.nome}]
Itens: {self.itens}
'''

class Personagem():
    def __init__(self):
        self.sala = Cena("Entrada")
        self.inventario = dict()
        self.item_equipado = None

    def coletar(self, nome_item):
        self.inventario[nome_item] = self.sala.coletar_item(nome_item)        
        

    def equipar(self, nome_item):
        self.item_equipado = self.inventario[nome_item]
        

    def desequipar(self):
        self.item_equipado = None
        

    def soltar(self, nome_item):
        # if item está equipado, desequipa
        if self.item_equipado.nome == nome_item:
            self.desequipar()
        
        # coloco item na sala atual
        self.sala.colocar_item(nome_item, self.inventario[nome_item])
        # retirar item do inventario
        del self.inventario[nome_item]
        
        

    def andar_norte(self):
        if self.sala.norte: # norte é uma Sala
            self.sala =self.sala.norte # minha sala atual é a sala que está ao meu norte
            
    
    def andar_sul(self):
        if self.sala.sul: # sul é uma Sala
            self.sala =self.sala.sul # minha sala atual é a sala que está ao meu sul
            

    def andar_leste(self):
        if self.sala.leste: # leste é uma Sala
            self.sala =self.sala.leste # minha sala atual é a sala que está ao meu leste
            

    def andar_oeste(self):
        if self.sala.oeste: # oeste é uma Sala
            self.sala =self.sala.oeste # minha sala atual é a sala que está ao meu oeste
            

    def atacar(self):
        pass

    def __str__(self):        
        return f'''
* {type(self)} *
Inventário: {self.inventario}
Equipado: {self.item_equipado}
{self.sala}
'''

class Mago(Personagem):
    def atacar(self):
        if self.item_equipado.nome == "lança":
            print(f"{self.item_equipado}: Zaaappp! Zuum!")
        

class Guerreiro(Personagem):
    def atacar(self):
        if self.item_equipado.nome == "espada":
            print(f"{self.item_equipado}: Classhh! Smashh!!!")


####################
# Model
# mapa

# Criamos as salas desconectadas

hall = Cena("Hall")
sala = Cena("Sala")
calabouco1 = Cena("Calabouço 1")

item1 = Item()
calabouco1.colocar_item("espada", item1)

item2 = Item()
calabouco1.colocar_item("lança", item2)

cela1 = Cena("Cela 1")
calabouco2 = Cena("Calabouço 2")
cela2 = Cena("Cela 2")
patio = Cena("Patio")

#########################
# Model
# Criação dos personagens
heroi = Guerreiro()

# personagem inicia no Hall
heroi.sala = hall

##
# Model
# Mapa conectando cenas
#
# hall - sala
#       calabouco1 - cela1
#       calabouco2 - cela2 - patio

hall.leste = sala

sala.sul = calabouco1
sala.oeste = hall

calabouco1.leste = cela1
calabouco1.norte = sala
calabouco1.sul = calabouco2

cela1.oeste = calabouco1
cela1.sul = cela2

calabouco2.norte = calabouco1
calabouco2.leste = cela2

cela2.norte = cela1
cela2.oeste = calabouco2
cela2.leste = patio

patio.oeste = cela2

#### Loop do jogo

# receber comando; executar comando; atualizar view

#####

##############################
# View
##############################

from textual.app import App, ComposeResult
from textual.widgets import Input, Button, TextArea

class DungeonView(App):
    def compose(self) -> ComposeResult:
        
        yield Input(id = 'tx_comando')
        yield Button('Executar', id='bt_executar')

        yield TextArea(id = 'txa_log')

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'bt_executar':
            # 1 - receber comando
            # 2 - executar comando
            # 3 - pedir para textual atualizar a view
        

            #### 1 - Receber comando
            comando = self.query_one('#tx_comando', Input).value

            comando = comando.split()

            #### 2 - Executar comando (Controller usando a model)
            match comando:
                case ['sair']:
                    self.exit()
                case ['status']:
                    self.query_one('#txa_log', TextArea).text = heroi.__str__()

                case ['andar', direcao]:
                    match direcao:
                        case 'norte':
                            heroi.andar_norte()
                        case 'sul':
                            heroi.andar_sul()
                        case 'leste':
                            heroi.andar_leste()
                        case 'oeste':
                            heroi.andar_oeste()
                        
                case ['coletar', nome_item]:
                    heroi.coletar(nome_item)
                case ['soltar', nome_item]:
                    heroi.soltar(nome_item)
                case ['equipar', nome_item]:
                    heroi.equipar(nome_item)
                case ['atacar']:
                    heroi.atacar()
                case comando_qualquer:
                    self.query_one('#txa_log', TextArea).text = f'Não entendi {comando_qualquer}'
                    return

            #### 3. atualizar a view (mostrar para o que mudou na aplicação)

        self.query_one('#txa_log', TextArea).text = heroi.__str__()


DungeonView().run()
