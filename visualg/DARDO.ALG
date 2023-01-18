Algoritmo "dardo"

Var

   d1, d2, d3: Real

Inicio

      escreval("Digite as tres distancias:")
      leia(d1)
      leia(d2)
      leia(d3)
      
      se (d1 > d3) e (d1 > d2) entao
         escreva("MAIOR: ", d1)
      senao
           se d2 > d3 entao
              escreva("MAIOR: ", d2)
           senao
                escreva("MAIOR: ", d3)
           fimse
      fimse
Fimalgoritmo