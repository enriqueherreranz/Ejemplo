class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print (self.nombre, ":", sep="")
        print("Fuerza: ", self.fuerza)
        print("Inteligencia: ", self.inteligencia)
        print("Defense: ", self.defensa)
        print("Vida: ", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self): 
        return self.vida > 0 #Retorna True si vida es mayor que 0, de lo contrario, retorna False

    def morir(self):
        self.vida = 0
        print(self.nombre, "Ha muerto")

    def daño(self, enemigo): #El nombre enemigo es genérico, es un nombre de variable que se utiliza para representar al personaje
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a ", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida actual de ", enemigo.nombre, "es de: ", enemigo.vida)
        else:
            enemigo.morir()

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valirio, daño: 8. (2) Matadragones, daño: 10: "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Por favor digite un valor válido")

    def atributos(self):
        super().atributos()
        print("Espada:", self.espada)

    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def cambiar_libro(self):
        opcion = int(input("Elije un libro: (1) Hechizo, con daño: 7. (2) Veneno, con daño: 9: "))
        if opcion == 1:
            self.libro = 7
        elif opcion == 2:
            self.libro = 9
        else:
            print("Por favor digite un valor válido")

    def atributos(self):
        super().atributos()
        print("Libro: ", self.libro)

    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa

personaje_1 = Guerrero("Guts", 20, 10 , 4, 100, 4) #Personaje_# es una variable
personaje_2 = Mago("Vannesa", 5, 15, 4, 100, 3)

def combate(jugador_1, jugador_2): #Pasan a ser argumentos y se puede poner cualquier nombre, solo importa el orden
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        jugador_1.atacar(jugador_2) #Atacar tiene muchas formas de usarse dependiendo la clase o subclase
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\hHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")

combate(personaje_1, personaje_2)