Algoritmo "combustivel"


Var

   distanciaPercorrida : Inteiro
   combustivelGasto, consumoMedio : Real
   
Inicio

      escreva("Distancia percorrida: ")
      leia(distanciaPercorrida)
      
      escreva("Combustível gasto: ")
      leia(combustivelGasto)
      
      consumoMedio <- distanciaPercorrida / combustivelGasto
      
      escreva("Consumo medio = ", consumoMedio:5:3)

Fimalgoritmo