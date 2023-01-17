Algoritmo "medidas"

Var

   a, b, c, areaQuad, areaTrian, areaTrap : Real

Inicio

      escreva("Digite a medida A: ")
      leia(A)
      escreva("Digite a medida B: ")
      leia(B)
      escreva("Digite a medida C: ")
      leia(C)

      areaQuad <- a * a
      areaTrian <- b * a / 2
      areaTrap <- (a + b)* c / 2

      escreval("AREA DO QUADRADO = ", areaQuad:6:4)
      escreval("AREA DO TRIANGULO = ", areaTrian:6:4)
      escreval("AREA DO TRAPEZIO = ", areaTrap:6:4)

Fimalgoritmo