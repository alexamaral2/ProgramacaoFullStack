Algoritmo "triangulo"
Var

   base, altura, perimetro, diagonal, area : Real

Inicio

      escreva("Base do Retangulo: ")
      leia(base)
      escreva("Altura do Retangulo: ")
      leia(altura)

      area <- base * altura
      perimetro <- 2 * (base + altura)
      diagonal <- RaizQ(Exp(base,2) + Exp(altura,2 ))
      
      escreval("AREA = ", area:8:4)
      escreval("PEIMETRO = ", perimetro:8:4)
      escreval("DIAGONAL = ", diagonal:8:4)

Fimalgoritmo