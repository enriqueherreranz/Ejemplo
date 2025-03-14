#POO Cuatro pilares
#Atributos = Características de la clase
#Clase = Estructura que permite definir atributos y métodos
#Métodos = Acciones que puede hacer la clase
#Para instanciar de una clase se usa el método constructor, en python es __init__
#Se puede acceder con . a los atributos para consultarlos, modificarlos o usar sus métodos

#Abstracción
#El termino abstracción se refiere a tomar lo necesario de la clase para usarla en la subclase, obviando datos irrelevantes en nuestro caso
#Nos permite elegir cuales serán los atributos y métodos que define la subclase para nosotros
#Ejemplo: La subclase Personaje, poseerá como atributos: nombre, fuerza, defensa y posición y de método atacar, defenderse, turno y constructor

#Encapsulación
#Es necesario indicar que podemos hacer un programa por medio de varias clases que se comuniquen entre sí, esto se llama Modularidad
#Si falla algo en el programa, es más fácil detectar está el error y arreglarlo
#Cada clase debe tener control propio de ella y poseer los métodos adecuados para poder ser utilizada desde afuera
#Advertencia: Tener los atributos y métodos de manera pública y poder acceder por medio de "." es peligroso, por ello debemos declarar
#Los atributos y métodos que serán privados para que no puedan ser accedidos desde afuera, esto se le llama Encapsulación
#Ejemplo: Para la subclase Personaje, solo queremos que sea accesible los métodos de constructor y turno, ninguno más
#Para los atributos que queremos que sean privados podemos poner a contador para que pueda funcionar el atributo turno sin problema
#Entonces getContador y setContador podrán consultarse, y para setContador agregamos una restricción para que no se acepten números negativos
#Recapitulando, si no declaramos los atributos como privados, se pueden usar y configurar desde afuera sin ningún tipo de control
#Y al declararlos como privados, solo se pueden consultar usando get y set, nada más

#Herencia
#A partir de nuestra clase Personaje, se pueden crear nuevas subclases como Guerrero y Mago
#Importante: A una subclase se le pueden agregar más métodos, no es necesario que sean solamente los mismos de la clase

#Polimorfismo
#Permite a un método ser diferente dependiendo de que clase lo esté usando
#Puede tener muchas formas de ser usado como por ejemplo, el método atacar
#Este método puede ser modificado en las subclase
#Por ejemplo, el método atacar de la clase Personaje usaba las manos, pero queremos que la subclase Guerrero use espada y Mago use libro
#O Guerrero ser modificada para que atacar sea fuerza*espada o que Mago su ataque sea inteligencia*libro
#De esta manera al calcular el daño que ha realizado, depende que clase o subclase reciba, y lo calculará de distinta forma
#Así, se puede crear una función que calcule el daño independientemente de que clase o subclase reciba